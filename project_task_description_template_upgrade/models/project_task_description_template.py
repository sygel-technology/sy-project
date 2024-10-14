# Copyright 2024 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import datetime

from odoo import api, fields, models


class ProjectTaskDescriptionTemplate(models.Model):
    _inherit = "project.task.description.template"

    template_order = fields.Selection(
        selection=[("Up", "Up"), ("Down", "Down")],
        default="Down",
        required=True,
    )
    section = fields.Boolean()
    section_name = fields.Char()
    section_with_date = fields.Boolean()
    section_delimiter_style = fields.Selection(
        selection=[
            ("dashed", "Dashed"),
            ("solid", "Solid"),
        ],
        default="dashed",
        required=True,
    )
    section_delimiter_header = fields.Html(compute="_compute_section_delimiter")
    section_delimiter_footer = fields.Html(compute="_compute_section_delimiter")

    @api.depends("section", "section_name", "section_with_date")
    def _compute_section_delimiter(self):
        for rec in self:
            if rec.section:
                centered_text = (
                    f" {rec.section_name} {datetime.date.today().strftime('%d/%m/%Y')} "
                    if rec.section_with_date
                    else f" {rec.section_name} "
                )
                style = rec.section_delimiter_style
                rec.section_delimiter_header = f"""
                    <p><br/><p>
                    <div style="display: flex; align-items: center;">
                        <hr style="flex-grow: 1; border-top: 1px {style} black;"/>
                        <span style="padding: 0 10px;">{centered_text}</span>
                        <hr style="flex-grow: 1; border-top: 1px {style} black;"/>
                    </div>
                """
                rec.section_delimiter_footer = f"""
                    <div style="display: flex; align-items: center;">
                        <hr style="flex-grow: 1; border-top: 1px {style} black;"/>
                    </div>
                    <p><br/><p>
                """
            else:
                rec.section_delimiter_header = ""
                rec.section_delimiter_footer = ""
