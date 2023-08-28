# Copyright 2023 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).


from odoo import models, fields, api


class HrExpense(models.Model):
    _inherit = "hr.expense"

    project_task_id = fields.Many2one(
        comodel_name="project.task",
        domain="[('allow_tasks_expenses', '=', True)]"
    )

    @api.onchange('project_task_id')
    def _onchange_project_task_id(self):
        if self.project_task_id and \
                self.project_task_id.project_id and \
                self.project_task_id.project_id.analytic_account_id:
            self.analytic_distribution = {
                self.project_task_id.project_id.analytic_account_id.id: 100
            }
