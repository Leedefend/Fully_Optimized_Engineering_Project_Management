from odoo import models, fields, api

class ProjectStageBatchCreate(models.TransientModel):
    _name = 'project.stage.batch.create'
    _description = 'Batch Create Project Stages'

    name = fields.Char(string='阶段名称', required=True)
    sequence = fields.Integer(string='序号', default=10)
    count = fields.Integer(string='数量', required=True, default=1)

    @api.model
    def create_stages(self):
        for i in range(self.count):
            self.env['project.stage'].create({
                'name': f'{self.name} {i+1}',
                'sequence': self.sequence + i
            })

    def action_create_stages(self):
        self.create_stages()
        return {'type': 'ir.actions.act_window_close'}
