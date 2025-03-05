# Copyright 2025 Ángel García de la Chica Herrera <angel.garcia@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ProjectTask(models.Model):
    _inherit = "project.task"

    project_coordinator_id = fields.Many2one(
        comodel_name="res.users",
        related="project_id.project_coordinator_id",
        store=True,
        string="Project Coordinator",
    )
