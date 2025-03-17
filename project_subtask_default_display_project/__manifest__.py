# Copyright 2025 Ángel García de la Chica <angel.garcia@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Project Subtask Default Display Project",
    "summary": "Project Subtask Default Display Project",
    "version": "16.0.1.1.0",
    "category": "Project",
    "website": "https://github.com/sygel-technology/sy-project",
    "author": "Sygel, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": ["project", "base_view_inheritance_extension"],
    "data": [
        "views/project_task_views.xml",
    ],
}
