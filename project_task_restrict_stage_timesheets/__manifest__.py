# Copyright 2024 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': 'Project Task Restrict Stage Timesheets',
    'summary': 'Configure task stages with a timesheet edition restriction',
    'version': '12.0.1.0.0',
    'category': 'Project',
    'website': 'https://sygel.es',
    'author': 'Sygel',
    'license': 'AGPL-3',
    'application': False,
    'installable': True,
    'depends': [
        'project',
    ],
    'data': [
        'security/project_task_restrict_stage_timesheets_security.xml',
        'views/project_task_type_views.xml',
    ],
}
