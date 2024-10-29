# Copyright 2024 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ProjectTaskType(models.Model):
    _inherit = "project.task.type"

    view_in_portal = fields.Boolean(
        help="Activate this option so portal users can have acces to the"
        " tasks in this stage.",
    )
