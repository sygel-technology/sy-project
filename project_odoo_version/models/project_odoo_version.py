# Copyright 2025 Ángel García de la Chica Herrera <angel.garcia@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class ProjectOdooVersion(models.Model):
    _name = "project.odoo.version"
    _description = "Project Odoo Version"
    _order = "id desc"

    name = fields.Char(string="Odoo Version")
    description = fields.Char(
        translate=True,
        string="Version Description",
    )
    active = fields.Boolean(
        default=True,
        string="Active Odoo Version",
    )

    @api.constrains("name")
    def _check_name(self):
        for sel in self:
            res = self.search_count([("id", "!=", sel.id), ("name", "=", sel.name)])
            if res:
                raise ValidationError(
                    _("There cannot be two Odoo version with the same name.")
                )

    def _active_records(self, record):
        """To facilitate inheritances and to be able to add
        all the models where the Odoo version can appear.
        """
        res = ""
        records = self.env["project.project"].search(
            [("odoo_version", "=", record.id), ("active", "=", True)]
        )
        if records:
            res = _("Projects ids: {}").format(records.ids)
        return res

    @api.constrains("active")
    def _check_archived_odoo_version(self):
        for record in self.filtered(lambda x: not x.active):
            res = self._active_records(record)
            if res:
                raise ValidationError(
                    _(
                        "You cannot archive a version of Odoo "
                        "associated with an active record.\n{}"
                    ).format(res)
                )

    def _associated_records(self, record):
        """To facilitate inheritances and to be able to add
        all the models where the Odoo version can appear.
        """
        res = ""
        records = self.env["project.project"].search(
            [("odoo_version", "=", record.id), ("active", "in", [True, False])]
        )
        if records:
            res = _("Projects ids: {}").format(records.ids)
        return res

    def unlink(self):
        for record in self:
            res = self._associated_records(record)
            if res:
                raise ValidationError(
                    _(
                        "You cannot delete a version of Odoo "
                        "associated with an active record.\n{}"
                    ).format(res)
                )
        return super(ProjectOdooVersion, self).unlink()
