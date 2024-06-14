# Copyright 2024 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import _, models, exceptions


class AccountAnalyticLine(models.Model):
    _inherit = "account.analytic.line"

    def _check_is_restricted_task_timesheet_creation(self, vals):
        if (
            'task_id' in vals
        ):
            new_task_id = self.env["project.task"].browse(vals['task_id'])
            if (
                new_task_id.exists()
                and new_task_id.stage_id.restrict_stage_timesheets
                and not self.env.user.has_group(
                    "project_task_restrict_stage_timesheets.res_group_all_stages")
            ):
                raise exceptions.ValidationError(_(
                    "You are not allowed to create timesheets in tasks that have the '{}' stage".format(
                        new_task_id.stage_id.name
                    )
                ))

    def _check_is_restricted_task_timesheet_edition(self, vals={}):
        restricted_stages = self.mapped('task_id.stage_id').filtered(
            lambda s: s.restrict_stage_timesheets
        )
        is_restricted_task_timesheet = any(restricted_stages)
        protected_vals = {
            'task_id',
            'unit_amount',
            'date',
        }
        if (
            is_restricted_task_timesheet
            and protected_vals.intersection(vals)
            and not self.env.user.has_group(
                "project_task_restrict_stage_timesheets.res_group_all_stages")
        ):
            raise exceptions.ValidationError(_(
                "You are not allowed to edit timesheets from tasks that have the {} stage(s)".format(
                    restricted_stages.mapped("name")
                )
            ))

    def create(self, vals):
        self._check_is_restricted_task_timesheet_creation(vals)
        return super().create(vals)

    def write(self, vals):
        self._check_is_restricted_task_timesheet_creation(vals)
        self._check_is_restricted_task_timesheet_edition(vals)
        return super().write(vals)

    def unlink(self):
        self._check_is_restricted_task_timesheet_edition({'task_id'})
        return super().unlink()
