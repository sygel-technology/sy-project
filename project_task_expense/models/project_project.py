# Copyright 2023 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).


from odoo import models, fields


class ProjectProject(models.Model):
    _inherit = "project.project"

    allow_tasks_expenses = fields.Boolean(
        string="Allow Tasks Expenses"
    )
