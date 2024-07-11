# Copyright 2024 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Project Task Stage Portal Visibility",
    "summary": "Hide tasks in portal according to task's stage",
    "version": "16.0.1.0.0",
    "category": "Project",
    "website": "https://github.com/sygel-technology/sy-project",
    "author": "Sygel, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "project",
    ],
    "data": [
        "views/project_views.xml",
        "security/ir_rule.xml",
    ],
    "post_init_hook": "post_init_hook",
    "uninstall_hook": "uninstall_hook",
}
