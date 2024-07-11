# Copyright 2021 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Task Requirements Management",
    "summary": "Manage requirements related to a task",
    "version": "15.0.1.0.0",
    "category": "Project",
    "website": "https://github.com/sygel-technology/sy-project",
    "author": "Sygel",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "project",
    ],
    "data": ["views/project_views.xml", "security/ir.model.access.csv"],
}
