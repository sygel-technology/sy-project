# Copyright 2023 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).


import binascii

from odoo import _, http
from odoo.exceptions import AccessError, MissingError
from odoo.http import request

from odoo.addons.portal.controllers import portal


class CustomerPortal(portal.CustomerPortal):
    @http.route(
        ["/my/tasks/<int:task_id>/project_task/sign/<string:source>"],
        type="json",
        auth="public",
        website=True,
    )
    def project_task_sign(
        self, task_id, access_token=None, source=False, name=None, signature=None
    ):
        access_token = access_token or request.httprequest.args.get("access_token")
        try:
            task_sudo = self._document_check_access(
                "project.task", task_id, access_token=access_token
            )
        except (AccessError, MissingError):
            return {"error": _("Invalid Task.")}

        if not task_sudo.needs_signature():
            return {
                "error": _("The task is not in a state requiring customer signature.")
            }
        elif task_sudo.signed:
            return {"error": _("The task is already signed.")}
        if not signature:
            return {"error": _("Signature is missing.")}
        if not name:
            return {"error": _("Name is missing.")}

        try:
            task_sudo.action_sign_task(name, signature)
        except (TypeError, binascii.Error):
            return {"error": _("Invalid signature data.")}
        return {
            "force_refresh": True,
            "redirect_url": task_sudo.get_portal_url(query_string=f"&source={source}"),
        }
