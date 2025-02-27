import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-sygel-technology-sy-project",
    description="Meta package for sygel-technology-sy-project Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-duplicate_project_task_timesheet>=15.0dev,<15.1dev',
        'odoo-addon-modify_followers_task>=15.0dev,<15.1dev',
        'odoo-addon-project_subtask_default_display_project>=15.0dev,<15.1dev',
        'odoo-addon-project_task_block_reason>=15.0dev,<15.1dev',
        'odoo-addon-project_task_description_template_section>=15.0dev,<15.1dev',
        'odoo-addon-project_task_show_project_manager>=15.0dev,<15.1dev',
        'odoo-addon-task_requirements_mgmt>=15.0dev,<15.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 15.0',
    ]
)
