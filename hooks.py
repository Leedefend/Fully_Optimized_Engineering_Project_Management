"""from odoo import api, SUPERUSER_ID

def _project_post_init(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    module_name = 'Engineering_Project_Management'
    lang = 'zh_CN'
    translations = env['ir.translation'].search([('lang', '=', lang)])
    for entry in translations:
        match = re.match(r"(module[s]?): (\w+)", entry.comment)
        if match:
            _, module = match.groups()
            if module == module_name:
              env['ir.translation'].load_module_terms([module], [lang])
"""