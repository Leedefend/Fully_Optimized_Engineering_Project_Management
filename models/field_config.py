from odoo import models, fields

class CustomFieldConfig(models.Model):
    _name = 'custom.field.config'
    _description = '自定义字段配置'

    model_name = fields.Char('模型名称', required=True)
    field_name = fields.Char('字段名称', required=True)
    field_label = fields.Char('字段标签', required=True)
    field_type = fields.Selection([
        ('char', '字符'),
        ('text', '文本'),
        ('date', '日期'),
        ('integer', '整数'),
        ('float', '浮动'),
        ('boolean', '布尔'),
        ('many2one', '多对一'),
        ('one2many', '一对多'),
        ('many2many', '多对多')
    ], string='字段类型', required=True)
    is_required = fields.Boolean('是否必填', default=False)
    model_id = fields.Many2one('ir.model', string="模型", required=True)
    active = fields.Boolean('是否启用', default=True)
