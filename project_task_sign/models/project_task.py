# Copyright 2023 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from datetime import datetime

from odoo import SUPERUSER_ID, api, fields, models


class ProjectTask(models.Model):
    _inherit = "project.task"

    allow_customer_signature = fields.Boolean(
        compute="_compute_allow_customer_signature",
        store=True,
        readonly=False,
    )
    send_automatic_signature_mail = fields.Boolean(
        compute="_compute_send_automatic_signature_mail",
        store=True,
        readonly=False,
    )
    signed = fields.Boolean(readonly=True, copy=False)
    signature_name = fields.Char(copy=False, readonly=True)
    signature_img = fields.Binary(copy=False, readonly=True)
    signature_date = fields.Datetime(
        string="Signature Date/Time", copy=False, readonly=True
    )

    @api.depends("project_id.allow_customer_signature")
    def _compute_allow_customer_signature(self):
        for sel in self:
            allow_customer_signature = False
            if sel.project_id:
                allow_customer_signature = sel.project_id.allow_customer_signature
            sel.allow_customer_signature = allow_customer_signature

    @api.depends("project_id.send_automatic_signature_mail")
    def _compute_send_automatic_signature_mail(self):
        for sel in self:
            send_automatic_signature_mail = False
            if sel.project_id:
                send_automatic_signature_mail = (
                    sel.project_id.send_automatic_signature_mail
                )
            sel.send_automatic_signature_mail = send_automatic_signature_mail

    def _send_signature_mail(self):
        if not self:
            return
        if self.env.su:
            self = self.with_user(SUPERUSER_ID)
        for task in self:
            mail_template = self.env.ref(
                "project_task_sign.email_template_project_task_sign",
                raise_if_not_found=False,
            )
            if not mail_template:
                continue
            task.with_context(force_send=True).message_post_with_template(
                mail_template.id, composition_mode="comment"
            )

    def action_sign_task(self, name=False, img=False):
        date_time = datetime.now()
        vals = {"signed": True, "signature_date": date_time}
        if name:
            vals["signature_name"] = name
        if img:
            vals["signature_img"] = img
        self.write(vals)
        attachment = self.env["ir.attachment"].create(
            {
                "name": f"task_{self.name}_signature_{name}_{date_time}",
                "res_id": self.id,
                "res_model": self._name,
                "datas": img,
                "type": "binary",
            }
        )
        self.message_post(
            body=f"Task signed on {date_time} by {name}", attachment_ids=attachment.ids
        )
        if self.send_automatic_signature_mail:
            self._send_signature_mail()

    def needs_signature(self):
        return self.allow_customer_signature and not self.signed

    def action_portal_task(self):
        self.ensure_one()
        return {
            "type": "ir.actions.act_url",
            "target": "current",
            "url": self.get_portal_url(),
        }

    def action_send_task_mail(self):
        self.ensure_one()
        try:
            template_id = self.env.ref(
                "project_task_sign.email_template_project_task_sign"
            ).id
        except ValueError:
            template_id = False
        ctx = {
            "default_model": "project.task",
            "default_res_id": self.id,
            "default_composition_mode": "comment",
            "force_email": True,
            "default_template_id": template_id,
        }
        return {
            "type": "ir.actions.act_window",
            "view_mode": "form",
            "res_model": "mail.compose.message",
            "views": [(False, "form")],
            "view_id": False,
            "target": "new",
            "context": ctx,
        }

    def reset_signature(self):
        self.ensure_one()
        self.write(
            {
                "signed": False,
                "signature_name": False,
                "signature_img": False,
                "signature_date": False,
            }
        )
