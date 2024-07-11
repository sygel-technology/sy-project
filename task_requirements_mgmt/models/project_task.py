# Copyright 2021 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ProjectTask(models.Model):
    _inherit = "project.task"

    task_requirement_ids = fields.One2many(
        string="Requirements",
        comodel_name="task.requirement",
        inverse_name="project_task_id",
    )
