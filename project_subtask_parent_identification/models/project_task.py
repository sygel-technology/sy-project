# Copyright 2025 Ángel García de la Chica Herrera <angel.garcia@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class ProjectTask(models.Model):
    _inherit = "project.task"

    sy_parent_id = fields.Char(
        compute="_compute_sy_parent_id",
        compute_sudo=True,
        store=True,
        string="Parent ID",
    )

    @api.depends("parent_id")
    def _compute_sy_parent_id(self):
        for task in self:
            res = ""
            if task.parent_id:
                res = " -> {}".format(task.parent_id.sy_id)
            task.sy_parent_id = res
