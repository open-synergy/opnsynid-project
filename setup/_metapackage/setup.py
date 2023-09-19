import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-open-synergy-opnsynid-project",
    description="Meta package for open-synergy-opnsynid-project Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-ssi_batch_project_assignment',
        'odoo14-addon-ssi_project',
        'odoo14-addon-ssi_project_assignment',
        'odoo14-addon-ssi_project_autocreate_analytic_account',
        'odoo14-addon-ssi_project_code',
        'odoo14-addon-ssi_project_custom_information',
        'odoo14-addon-ssi_project_template',
        'odoo14-addon-ssi_project_type',
        'odoo14-addon-ssi_project_work_log',
        'odoo14-addon-ssi_task_code',
        'odoo14-addon-ssi_task_data_requirement',
        'odoo14-addon-ssi_task_mixin',
        'odoo14-addon-ssi_task_project_manager',
        'odoo14-addon-ssi_task_quality_control',
        'odoo14-addon-ssi_task_timebox',
        'odoo14-addon-ssi_task_type',
        'odoo14-addon-ssi_task_work_log',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 14.0',
    ]
)
