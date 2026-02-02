# Copyright 2024 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).


from odoo import api, models


class ProjectTask(models.Model):
    _inherit = "project.task"

    @api.onchange("description_template_id")
    def _onchange_description_template_id(self):
        res = None
        if self.description_template_id:
            description = self.description if self.description else ""
            if self.description_template_id.template_order == "Down":
                self.description = (
                    description + self.description_template_id.section_delimiter_header
                )
                res = super()._onchange_description_template_id()
                self.description = (
                    self.description
                    + self.description_template_id.section_delimiter_footer
                )
            elif self.description_template_id.template_order == "Up":
                self.description = (
                    self.description_template_id.section_delimiter_header
                    + self.description_template_id.description
                    + self.description_template_id.section_delimiter_footer
                    + description
                )
        else:
            res = super()._onchange_description_template_id()
        return res
