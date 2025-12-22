# Copyright 2025 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ProjectTask(models.Model):
    _inherit = "project.task"

    manager_id = fields.Many2one(
        comodel_name="res.users",
        string="Project Manager",
        related="project_id.user_id",
        readonly=True,
    )
