# Copyright 2023 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Project Task Expense",
    "summary": "Create expenses related to project tasks",
    "version": "16.0.1.0.0",
    "category": "Project",
    "website": "https://github.com/sygel-technology/sy-project",
    "author": "Sygel, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": ["project", "hr_expense", "hr_timesheet"],
    "data": ["views/project_views.xml", "views/hr_expense_view.xml"],
}
