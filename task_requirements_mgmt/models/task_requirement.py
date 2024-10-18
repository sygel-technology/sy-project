# Copyright 2021 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class TaskRequirement(models.Model):
    _name = "task.requirement"
    _description = "Task Requirement"

    specification_date = fields.Date(default=fields.Date.today())
    description = fields.Char()
    completed = fields.Boolean()
    completed_date = fields.Date(
        string="·Completed Date",
        compute="_compute_completed_date",
        readonly=False,
        store=True,
    )
    tested = fields.Boolean()
    tested_date = fields.Date(
        compute="_compute_tested_date", readonly=False, store=True
    )
    project_task_id = fields.Many2one(string="Task", comodel_name="project.task")

    @api.depends("completed")
    def _compute_completed_date(self):
        today = fields.Date.today()
        for sel in self:
            sel.completed_date = (
                today if sel.completed and not sel.completed_date else False
            )

    @api.depends("tested")
    def _compute_tested_date(self):
        today = fields.Date.today()
        for sel in self:
            sel.tested_date = today if sel.tested and not sel.tested_date else False
