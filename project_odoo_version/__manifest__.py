# Copyright 2025 Ángel García de la Chica <angel.garcia@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Project Odoo Version",
    "summary": "Project Odoo Version",
    "version": "16.0.1.0.0",
    "category": "Porject",
    "website": "https://github.com/sygel-technology/sy-project",
    "author": "Sygel, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": ["project"],
    "data": [
        "data/data.xml",
        "security/ir.model.access.csv",
        "views/project_views.xml",
        "views/project_task_views.xml",
        "views/project_odoo_version_views.xml",
    ],
}
