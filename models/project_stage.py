from odoo import models, fields

class ProjectStage(models.Model):
    _inherit = 'project.project.stage'
    _description = 'Project Stage'

    project_id = fields.Many2one('project.project', string='Project', ondelete='cascade')
    task_ids = fields.One2many('project.task', 'name', string='Tasks')
    task_template_ids = fields.One2many('project.task.template', 'stage_id', string='任务模版')
