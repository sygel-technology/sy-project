# Copyright 2025 Ángel García de la Chica Herrera <angel.garcia@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ProjectTask(models.Model):
    _inherit = "project.task"

    odoo_version = fields.Many2one(
        comodel_name="project.odoo.version",
        related="project_id.odoo_version",
        string="Project Odoo Version",
    )
