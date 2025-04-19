from odoo import models, fields

class ProjectPartner(models.Model):
    _name = 'project.partner'
    _description = '参建单位'

    name = fields.Many2one('res.partner', string="名称", required=True)
    partner_type = fields.Selection([
        ('survey', '地勘单位'),
        ('design', '设计单位'),
        ('construction', '施工单位'),
        ('supervision', '监理单位'),
        ('owner', '建设单位'),
        ('other', '其他单位')
    ], string="单位类型", required=True)
    project_id = fields.Many2one('project.project', string="项目")
    manager = fields.Many2one('res.partner', string="负责人")
    contact_info = fields.Text(string="联系方式")
