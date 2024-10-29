# Copyright 2023 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Project Stock Portal",
    "version": "16.0.1.0.0",
    "category": "Project",
    "summary": """
        Show task's stock materials in portal.
    """,
    "author": "Sygel",
    "website": "https://github.com/sygel-technology/sy-project",
    "license": "AGPL-3",
    "depends": ["project_stock", "hr_timesheet"],
    "data": [
        "views/project_portal_templates.xml",
    ],
    "auto_install": False,
    "installable": True,
}
