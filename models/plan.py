from odoo import models, fields, api

class Plan(models.Model):
    _name = 'project.plan'
    _description = 'Project Plan'

    name = fields.Char(string="计划名称", required=True)
    project_id = fields.Many2one('project.project', string="项目", required=True)
    department_id = fields.Many2one('hr.department', string="部门")
    start_date = fields.Date(string="开始日期")
    end_date = fields.Date(string="结束日期")
    task_type_id = fields.Many2one('project.dictionary', string='任务类型',
                                   domain="[('type','=','task_type'), ('active','=',True)]")
    task_status_id = fields.Many2one('project.dictionary', string='任务状态',
                                     domain="[('type','=','task_status'), ('active','=',True)]")
    task_priority_id = fields.Many2one('project.dictionary', string='任务优先级',
                                       domain="[('type','=','task_priority'), ('active','=',True)]")



