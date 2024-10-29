# Copyright 2023 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import _, fields, models


class ProjectTask(models.Model):
    _inherit = "project.task"

    hr_expense_ids = fields.One2many(
        string="Expenses", comodel_name="hr.expense", inverse_name="project_task_id"
    )
    expenses_count = fields.Integer(compute="_compute_expenses_count")
    allow_tasks_expenses = fields.Boolean(related="project_id.allow_tasks_expenses")

    def _compute_expenses_count(self):
        for sel in self:
            sel.expenses_count = self.env["hr.expense"].search_count(
                [("project_task_id", "=", self.id), ("state", "!=", "refused")]
            )

    def action_view_expenses(self):
        return {
            "type": "ir.actions.act_window",
            "res_model": "hr.expense",
            "domain": [("project_task_id", "=", self.id)],
            "view_mode": "tree,form",
            "target": "current",
            "name": _("Expenses"),
            "context": {"default_project_task_id": self.id},
        }
