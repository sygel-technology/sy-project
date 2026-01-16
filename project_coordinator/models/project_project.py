# Copyright 2025 Ángel García de la Chica Herrera <angel.garcia@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class Project(models.Model):
    _inherit = "project.project"

    project_coordinator_id = fields.Many2one(
        comodel_name="res.users",
        copy=False,
        tracking=True,
        string="Project Coordinator",
    )
