from odoo import models, fields

class ProjectDictionaryType(models.Model):
    _name = 'project.dictionary.type'
    _description = '数据字典类型'

    name = fields.Char(string='名称', required=True)
    code = fields.Char(string='编码', required=True)
    active = fields.Boolean(string='启用', default=True)


class ProjectDictionary(models.Model):
    _name = 'project.dictionary'
    _description = '项目管理数据字典'

    name = fields.Char(string='名称', required=True)
    code = fields.Char(string='编码', required=True)
    type_id = fields.Many2one('project.dictionary.type', string='字典类型', required=True, ondelete='restrict')
    active = fields.Boolean(string='启用', default=True)
