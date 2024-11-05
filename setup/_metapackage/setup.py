import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo12-addons-sygel-technology-sy-project",
    description="Meta package for sygel-technology-sy-project Odoo addons",
    version=version,
    install_requires=[
        'odoo12-addon-easy_search_task_ticket',
        'odoo12-addon-project_task_restrict_stage_changes',
        'odoo12-addon-project_task_restrict_stage_timesheets',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 12.0',
    ]
)
