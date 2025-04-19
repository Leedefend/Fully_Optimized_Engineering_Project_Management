from odoo import models, fields

class ProjectTaskTemplate(models.Model):
    _name = 'project.task.template'
    _description = '项目任务模版'

    name = fields.Char(string='任务名称', required=True)
    description = fields.Text(string='任务描述')
    stage_id = fields.Many2one('project.project.stage', string='项目阶段', required=True)
    task_stage_id = fields.Many2one('project.task.type', string='任务状态')
    sequence = fields.Integer(string='序号', default=10)
    task_ids = fields.One2many('project.task', 'template_id', string="模板任务")
