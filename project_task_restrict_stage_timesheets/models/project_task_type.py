# Copyright 2024 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ProjectTask(models.Model):
    _inherit = "project.task.type"

    restrict_stage_timesheets = fields.Boolean(
        string='Restrict Timesheets',
        help='Restrict creating timesheets for tasks in this stage'
    )
