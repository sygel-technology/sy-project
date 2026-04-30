# Copyright 2021 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class Task(models.Model):
    _inherit = "project.task"

    task_blocked_reason = fields.Text(
        string="Blocked Reason",
        compute="_compute_blocked_reason",
        store=True,
        readonly=False,
    )
    blocked = fields.Boolean(
        compute="_compute_blocked",
        store=True,
    )

    @api.depends("blocked", "parent_id.blocked")
    def _compute_state(self):
        blocked_tasks = self.filtered("blocked")
        for task in blocked_tasks:
            task.state = "04_waiting_normal"
        return super(Task, self - blocked_tasks)._compute_state()

    def _inverse_state(self):
        res = super()._inverse_state()
        for task in self.filtered(lambda task: task.state != "04_waiting_normal"):
            task.blocked = False
        return res

    @api.depends("parent_id.blocked")
    def _compute_blocked(self):
        for task in self.filtered("parent_id"):
            task.blocked = task.parent_id.blocked

    @api.depends("parent_id.task_blocked_reason")
    def _compute_blocked_reason(self):
        for task in self.filtered("parent_id"):
            task.task_blocked_reason = task.parent_id.task_blocked_reason

    def action_block(self):
        self.filtered(lambda t: not t.blocked).write({"blocked": True})

    def action_unblock(self):
        self.filtered(lambda t: t.state != "01_in_progress").write(
            {"state": "01_in_progress"}
        )
