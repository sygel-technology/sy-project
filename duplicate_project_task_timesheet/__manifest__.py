# Copyright 2021 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Duplicate Project Task Timesheet",
    "summary": "Button to duplicate project task timesheet lines",
    "version": "15.0.1.0.0",
    "category": "Timesheets",
    "website": "https://github.com/sygel-technology/sy-project",
    "author": "Sygel",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "hr_timesheet",
    ],
    "data": ["views/project_views.xml"],
}
