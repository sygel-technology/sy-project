# Copyright 2025 Ángel García de la Chica Herrera <angel.garcia@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class Project(models.Model):
    _inherit = "project.project"

    odoo_version = fields.Many2one(
        comodel_name="project.odoo.version",
        string="Project Odoo Version",
    )

    @api.constrains("odoo_version")
    def _check_active_odoo_version(self):
        for sel in self:
            if not sel.odoo_version.active:
                raise ValidationError(
                    _(
                        "You can choose only one active version. "
                        "If you want to select it, activate it first."
                    )
                )
