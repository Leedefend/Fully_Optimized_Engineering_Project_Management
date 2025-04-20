{
    'name': '智能工程项目管理系统',
    'version': '1.0',
    'summary': '综合项目管理，包含计划编制、执行、监控和分析功能。',
    'description': '此模块扩展了项目管理功能，包含工程项目的综合计划管理。',
    'category': 'Project Management',
    'author': 'Lidefend',
    'depends': ['project', 'base', 'web','hr'],
    'data': [
        'security/ir.model.access.csv',
        'security/project_security.xml',
        'data/project_sequence.xml',
        'views/project_views.xml',
        'views/ai_analysis_log_views.xml',
        'views/plan_views.xml',
        'views/project_stage_views.xml',
        'views/project_task_template_views.xml',
        #'views/wizard_views.xml',
        'views/actions.xml',
        'views/menus.xml',
        'views/dictionary_views.xml',
        'data/project_stage_data.xml',
        'data/project_task_template_data.xml',
        'views/project_dictionary_fields_views.xml',
        'views/ai_analysis_log_views.xml',

    ],
    'installable': True,
    'application': True,

    'assets': {
        'web.assets_backend': [
            'Engineering_Project_Management/static/src/js/display_ai_advice.js',
        ],
    },
    
}
