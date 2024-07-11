# Copyright 2023 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models


class AccountAnalyticLine(models.Model):
    _inherit = "account.analytic.line"

    def _signature_timesheet_get_portal_domain(self):
        return [
            "|",
            ("task_id.project_id.privacy_visibility", "=", "portal"),
            "&",
            ("task_id", "=", False),
            "&",
            (
                "project_id.message_partner_ids",
                "child_of",
                [self.env.user.partner_id.commercial_partner_id.id],
            ),
            ("project_id.privacy_visibility", "=", "portal"),
        ]
