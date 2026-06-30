# Copyright 2023 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class AccountAnalyticLine(models.Model):
    _inherit = "account.analytic.line"

    expense_id = fields.Many2one(
        string="Expense", related="move_line_id.expense_id", store=True
    )

    def _timesheet_postprocess_values(self, values):
        res = super()._timesheet_postprocess_values(values)
        for key in self.filtered(
            lambda x: x.move_line_id and x.move_line_id.expense_id
        ).ids:
            res[key].pop("amount", None)
        return res
