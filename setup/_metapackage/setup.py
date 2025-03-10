import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-sygel-technology-sy-project",
    description="Meta package for sygel-technology-sy-project Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-duplicate_project_task_timesheet>=16.0dev,<16.1dev',
        'odoo-addon-project_stock_portal>=16.0dev,<16.1dev',
        'odoo-addon-project_task_description_template_section>=16.0dev,<16.1dev',
        'odoo-addon-project_task_expense>=16.0dev,<16.1dev',
        'odoo-addon-project_task_identification>=16.0dev,<16.1dev',
        'odoo-addon-project_task_sign>=16.0dev,<16.1dev',
        'odoo-addon-project_task_stage_portal_user_visibility>=16.0dev,<16.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 16.0',
    ]
)
