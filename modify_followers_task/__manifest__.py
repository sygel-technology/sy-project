# Copyright 2019 Joan Segui <joan.segui@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Modify Followers Task",
    "summary": "Modify list of followers from a project task",
    "version": "15.0.1.0.0",
    "category": "Project",
    "website": "https://github.com/sygel-technology/sy-project",
    "author": "QubiQ, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": ["project"],
    "data": [
        "security/ir.model.access.csv",
        "wizard/modify_followers_task_wizard.xml",
        "views/project_task_view.xml",
    ],
}
