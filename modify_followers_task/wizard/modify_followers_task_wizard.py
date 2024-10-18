# Copyright 2019 Joan Segui <joan.segui@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ModifyFollowersTaskWizard(models.TransientModel):
    _name = "modify.followers.task.wizard"
    _description = "modify.followers.task.wizard"

    follower_ids = fields.Many2many(
        comodel_name="res.partner",
        string="Followers",
        default=lambda self: self.env["project.task"]
        .browse(self._context.get("active_id"))
        .message_partner_ids.ids,
    )

    def modify_followers(self):
        active_id = self.env["project.task"].browse(self._context.get("active_id"))
        active_id.message_subscribe(
            partner_ids=list(
                set(self.follower_ids.ids) - set(active_id.message_partner_ids.ids)
            )
        )
        active_id.message_unsubscribe(
            partner_ids=list(
                filter(
                    lambda x: x not in self.follower_ids.ids,
                    active_id.message_partner_ids.ids,
                )
            )
        )
