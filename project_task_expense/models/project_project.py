# Copyright 2023 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import _, fields, models


class ProjectProject(models.Model):
    _inherit = "project.project"

    allow_tasks_expenses = fields.Boolean()
    expenses_count = fields.Integer(compute="_compute_expenses_count")

    def _compute_expenses_count(self):
        for sel in self:
            sel.expenses_count = self.env["hr.expense"].search_count(
                [
                    ("project_task_id.project_id", "=", self.id),
                    ("state", "!=", "refused"),
                ]
            )

    def action_view_expenses(self):
        task_ids = self.mapped("task_ids").ids
        view_id = self.env.ref(
            "project_task_expense.project_task_expense_hr_expense_view_expenses_analysis_tree"
        ).id
        return {
            "type": "ir.actions.act_window",
            "res_model": "hr.expense",
            "domain": [("project_task_id", "in", task_ids)],
            "view_id": view_id,
            "views": [(view_id, "tree"), (False, "form")],
            "view_mode": "tree,form",
            "target": "current",
            "name": _("Expenses"),
        }
