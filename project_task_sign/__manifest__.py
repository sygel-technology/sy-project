# Copyright 2023 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Project Task Sign",
    "version": "16.0.1.0.0",
    "category": "Project",
    "summary": """
        Sign tasks from portal.
    """,
    "author": "Sygel",
    "website": "https://github.com/sygel-technology/sy-project",
    "license": "AGPL-3",
    "depends": ["project", "hr_timesheet", "project_stock"],
    "data": [
        "data/mail_template_data.xml",
        "views/project_views.xml",
        "views/project_portal_templates.xml",
        "report/report_timesheet_template.xml",
    ],
    "auto_install": False,
    "installable": True,
}
