from odoo import models, fields

class ProjectDictionary(models.Model):
    _name = 'project.dictionary'
    _description = '项目管理数据字典'

    name = fields.Char(string='名称', required=True)
    code = fields.Char(string='编码', required=True)
    type = fields.Selection([
        ('project_type', '项目类型'),
        ('project_status', '项目状态'),
        ('task_type', '任务类型'),
        ('task_status', '任务状态'),
        ('task_priority', '任务优先级'),
    ], string='字典类型', required=True)
    active = fields.Boolean(string='启用', default=True)
