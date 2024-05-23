# Copyright 2024 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import SUPERUSER_ID, api


def post_init_hook(cr, registry, vals=None):
    env = api.Environment(cr, SUPERUSER_ID, {})
    env.ref("project.project_task_rule_portal").active = False


def uninstall_hook(cr, registry, vals=None):
    env = api.Environment(cr, SUPERUSER_ID, {})
    env.ref("project.project_task_rule_portal").active = True
