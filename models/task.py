from odoo import models, fields, api

class ProjectTask(models.Model):
    _inherit = 'project.task'

    template_id = fields.Many2one('project.task.template', string="任务模板")
    stage_id = fields.Many2one('project.task.type', string="任务阶段")
    project_stage_id = fields.Many2one('project.project.stage', string="项目阶段")
    progress = fields.Float(string="进度", default=0.0)
    report = fields.Text(string="汇报")
    dependent_task_ids = fields.Many2many('project.task', 'task_dependency_rel', 'task_id', 'dependent_task_id', string="依赖任务")
    department_id = fields.Many2one('hr.department', string='责任部门')
    responsible_user_id = fields.Many2one('res.users', string='责任人')
    task_type_id = fields.Many2one('project.dictionary', string='任务类型',
                                   domain="[('type','=','task_type'), ('active','=',True)]")
    task_status_id = fields.Many2one('project.dictionary', string='任务状态',
                                     domain="[('type','=','task_status'), ('active','=',True)]")
    task_priority_id = fields.Many2one('project.dictionary', string='任务优先级',
                                       domain="[('type','=','task_priority'), ('active','=',True)]")

    @api.model
    def create(self, vals):
        # 处理模板创建逻辑
        template_id = vals.get('template_id')
        if template_id:
            template = self.env['project.task.template'].browse(template_id)
            for task_vals in template.task_ids:
                task_vals.update({
                    'project_id': vals.get('project_id'),
                    'project_stage_id': vals.get('project_stage_id'),
                    'stage_id': template.stage_id.id or vals.get('stage_id'),  # 设置任务阶段
                })
                # 创建任务
                self.env['project.task'].create(task_vals)

        # 调用父类的create方法
        return super(ProjectTask, self).create(vals)

    def create_tasks_from_template(self, vals):
        template_id = vals.get('template_id')
        if template_id:
            template = self.env['project.task.template'].browse(template_id)
            for task_vals in template.task_ids:
                task_vals.update({
                    'project_id': vals.get('project_id'),
                    'project_stage_id': vals.get('project_stage_id'),
                    'stage_id': template.stage_id.id or vals.get('stage_id'),  # 设置任务阶段
                })
                self.env['project.task'].create(task_vals)

class ProjectTaskType(models.Model):
    _inherit = 'project.task.type'

    # 添加一个布尔字段来标识这个任务类型是否从模板创建
    is_template = fields.Boolean(string="是否为模板任务类型")
