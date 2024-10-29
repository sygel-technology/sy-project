# Copyright 2023 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class HrExpense(models.Model):
    _inherit = "hr.expense"

    project_task_id = fields.Many2one(
        comodel_name="project.task", domain="[('allow_tasks_expenses', '=', True)]"
    )

    def _compute_analytic_distribution(self):
        for sel in self:
            res = analytic_distribution = super()._compute_analytic_distribution()
            if (
                self.project_task_id
                and self.project_task_id.project_id
                and self.project_task_id.project_id.analytic_account_id
            ):
                analytic_distribution = {
                    self.project_task_id.project_id.analytic_account_id.id: 100
                }
            sel.analytic_distribution = analytic_distribution
        return res

    @api.onchange("project_task_id")
    def _onchange_project_task_id(self):
        if (
            self.project_task_id
            and self.project_task_id.project_id
            and self.project_task_id.project_id.analytic_account_id
        ):
            self.analytic_distribution = {
                self.project_task_id.project_id.analytic_account_id.id: 100
            }
