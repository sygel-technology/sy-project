# Copyright 2023 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo.http import request
from odoo.osv import expression

from odoo.addons.hr_timesheet.controllers import project


class TaskSignCustomerPortal(project.ProjectCustomerPortal):
    def _task_get_page_view_values(self, task, access_token, **kwargs):
        values = super()._task_get_page_view_values(task, access_token, **kwargs)
        if (
            access_token
            and task
            and task.allow_customer_signature
            and request.env.user._is_public()
        ):
            domain = request.env[
                "account.analytic.line"
            ]._signature_timesheet_get_portal_domain()
            task_domain = expression.AND([domain, [("task_id", "=", task.id)]])
            timesheets = request.env["account.analytic.line"].sudo().search(task_domain)
            values["timesheets"] = timesheets
        return values
