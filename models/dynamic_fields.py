from odoo import models, fields
from odoo.exceptions import UserError


class DynamicField(models.Model):
    _inherit = 'project.project'  # 这里可以是任何模型

    def create_dynamic_field(self, field_config):
        # 动态创建字段
        if field_config.active:
            model = self.env['ir.model'].search([('model', '=', field_config.model_name)], limit=1)
            if not model:
                raise UserError("找不到指定的模型: %s" % field_config.model_name)

            field_data = {
                'name': field_config.field_name,
                'field_description': field_config.field_label,
                'ttype': field_config.field_type,
                'required': field_config.is_required,
                'model_id': model.id
            }

            # 使用 Odoo 的 ORM 动态创建字段
            self.env['ir.model.fields'].create(field_data)
