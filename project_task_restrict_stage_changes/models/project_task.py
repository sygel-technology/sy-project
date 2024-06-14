# Copyright 2024 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import _, models, exceptions


class ProjectTask(models.Model):
    _inherit = "project.task"

    def write(self, vals):
        if (
            'stage_id' in vals
        ):
            new_stage_id = self.env["project.task.type"].browse(vals['stage_id'])
            if (
                new_stage_id.exists()
                and new_stage_id.restrict_stage_assignment
                and not self.env.user.has_group(
                    "project_task_restrict_stage_changes.res_group_all_stages")
            ):
                raise exceptions.ValidationError(_(
                    "You are not allowed to move tasks to '{}' stage".format(
                        new_stage_id.name
                    )
                ))
            old_restricted_stage_ids = self.mapped('stage_id').filtered(
                lambda s: s.restrict_stage_deallocation
            )
            if (
                any(old_restricted_stage_ids)
                and not self.env.user.has_group(
                    "project_task_restrict_stage_changes.res_group_all_stages")
            ):
                raise exceptions.ValidationError(_(
                    "You are not allowed to remove tasks from {} stage(s)".format(
                        old_restricted_stage_ids.mapped('name')
                    )
                ))
        return super().write(vals)
