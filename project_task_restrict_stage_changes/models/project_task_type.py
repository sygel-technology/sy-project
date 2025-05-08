# Copyright 2024 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ProjectTask(models.Model):
    _inherit = "project.task.type"

    restrict_stage_assignment = fields.Boolean(
        string="Restrict Stage Assignment",
    )
    restrict_stage_deallocation = fields.Boolean(
        string="Restrict Stage Deallocation",
    )
