# Copyright 2020 Valentin Vinagre <valentin.vinagre@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Easy Search Task/Tickets",
    "summary": "Allow search task/tickets in the main bar by id.",
    "version": "12.0.1.0.0",
    "category": "Project",
    "website": "https://www.sygel.es",
    "author": "Sygel, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "web",
        "project",
        "helpdesk"
    ],
    "data": [
        'views/assets.xml',
    ],
    'qweb': [
        'static/src/xml/quick_task_ticket_navigation.xml',
    ]
}
