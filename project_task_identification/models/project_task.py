# Copyright 2025 Ángel García de la Chica Herrera <angel.garcia@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ProjectTask(models.Model):
    _inherit = "project.task"

    sy_id = fields.Char(
        compute="_compute_sy_id",
        compute_sudo=True,
        string="ID",
    )

    def _compute_sy_id(self):
        for sel in self:
            sel.sy_id = "T-{}".format(sel.id)
