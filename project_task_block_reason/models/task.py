# Copyright 2021 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class Task(models.Model):
    _inherit = "project.task"

    task_blocked_reason = fields.Text(string="Blocked Reason")
