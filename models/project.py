from odoo import models, fields, api, _
from odoo.exceptions import UserError
import requests
from openai import OpenAI
from odoo.exceptions import UserError
import logging
_logger = logging.getLogger(__name__)


class ProjectProject(models.Model):
    _inherit = 'project.project'

    # AI辅助字段
    ai_risk_summary = fields.Text(string="AI 风险提示", readonly=True)
    ai_plan_brief = fields.Text(string="AI 任务结构", readonly=True)
    ai_invest_hint = fields.Text(string="AI 投资建议", readonly=True)
    ai_doc_recommend = fields.Text(string="AI 推荐文档", readonly=True)
    ai_analysis_ids = fields.One2many(
        'ai.analysis.log',
        'project_id',
        string='AI 分析记录'
    )

    # 数据字典关联字段（合并去重后）
    project_type_id = fields.Many2one('project.dictionary', string='项目分类',
                                      domain="[('type_id.code', '=', '\1'), ('active', '=', True)]")
    project_status_id = fields.Many2one('project.dictionary', string='项目状态',
                                        domain="[('type','=','project_status'), ('active','=',True)]")
    construction_property_id = fields.Many2one('project.dictionary', string='建设性质',
                                               domain="[('type', '=', 'project_property'), ('active', '=', True)]")
    project_function_id = fields.Many2one('project.dictionary', string='工程用途',
                                          domain="[('type', '=', 'project_function'), ('active', '=', True)]")
    structure_type_id = fields.Many2one('project.dictionary', string='结构体系',
                                        domain="[('type', '=', 'structure_type'), ('active', '=', True)]")
    contract_type_id = fields.Many2one('project.dictionary', string='合同类型',
                                       domain="[('type', '=', 'contract_type'), ('active', '=', True)]")
    tender_class_id = fields.Many2one('project.dictionary', string='招标类型',
                                      domain="[('type', '=', 'tender_class'), ('active', '=', True)]")
    tender_type_id = fields.Many2one('project.dictionary', string='招标方式',
                                     domain="[('type', '=', 'tender_type'), ('active', '=', True)]")
    superviser_role_id = fields.Many2one('project.dictionary', string='监理角色',
                                         domain="[('type', '=', 'superviser_role'), ('active', '=', True)]")
    design_role_id = fields.Many2one('project.dictionary', string='勘察设计角色',
                                     domain="[('type', '=', 'design_role'), ('active', '=', True)]")
    corp_role_id = fields.Many2one('project.dictionary', string='企业角色',
                                   domain="[('type', '=', 'corp_role'), ('active', '=', True)]")
    specialty_id = fields.Many2one('project.dictionary', string='专业名称',
                                   domain="[('type', '=', 'specialty'), ('active', '=', True)]")
    title_level_id = fields.Many2one('project.dictionary', string='职称等级',
                                     domain="[('type', '=', 'title_level'), ('active', '=', True)]")
    project_level_id = fields.Many2one('project.dictionary', string='工程等级',
                                       domain="[('type', '=', 'project_level'), ('active', '=', True)]")
    data_source_id = fields.Many2one('project.dictionary', string='数据来源',
                                     domain="[('type', '=', 'data_source'), ('active', '=', True)]")

    # 项目基础字段
    prj_num = fields.Char(string='项目编号', required=True, readonly=True, default=lambda self: _('New'))
    name = fields.Char(string='项目名称', required=True)
    construction_location = fields.Char(string='建设位置')
    construction_content = fields.Text(string='建设内容及规模')
    project_management_company_id = fields.Many2one('res.company', string='项目管理公司')
    segment_num = fields.Char(string='标段编号')
    segment_name = fields.Char(string='标段名称')
    annual_target = fields.Char(string='年度目标')
    planned_start_date = fields.Date(string='计划开工日期')
    planned_end_date = fields.Date(string='计划竣工日期')
    build_corp_name = fields.Char(string='建设单位', size=200, required=True, default='未填写')
    is_major_project = fields.Boolean(string='是否重点项目', default=False)

    def action_generate_ai_analysis(self):
        # 这里填入调用 AI 接口或生成分析记录的逻辑
        for record in self:
            prompt = f"""
               你是一个经验丰富的工程项目顾问，请基于以下信息给出建议：
               1. 项目任务结构应包括哪些阶段和关键任务？
               2. 项目投资额度是否合理？初步估算应该是多少？
               3. 项目可能存在哪些管理、技术或政策风险？
               4. 推荐需要准备哪些文档？

               项目名称：{record.name}
               项目类型：{getattr(record, 'x_project_type', '')}
               投资金额：{getattr(record, 'x_budget_total', 0)} 万元
               工期：{getattr(record, 'x_duration_days', 180)} 天
               建设位置：{getattr(record, 'x_location', '')}
               """

            api_key = self.env['ir.config_parameter'].get_param('ai_api_key')
            if not api_key:
                raise UserError("AI API 密钥未配置！")

            headers = {
                "Authorization": f"{api_key}",
                "Content-Type": "application/json"
            }
            payload = {
                "model": "deepseek-chat",
                "messages": [
                    {"role": "system", "content": "你是一个工程顾问"},
                    {"role": "user", "content": prompt}
                ],
                "temperature": 0.7
            }

            try:
                _logger.info(f"[AI调用开始] 用户: {self.env.user.name}, 项目: {record.name}")
                _logger.debug(f"[AI请求内容] Prompt: {prompt}")

                response = requests.post(
                    "https://api.deepseek.com/v1/chat/completions",
                    headers=headers,
                    json=payload,
                    timeout=60
                )
                result = response.json()
                content = result.get("choices", [{}])[0].get("message", {}).get("content", "")
                _logger.info(f"[AI返回内容] {content}")

                lines = content.strip().split('\n')
                record.ai_plan_brief = lines[0] if len(lines) > 0 else ''
                record.ai_invest_hint = lines[1] if len(lines) > 1 else ''
                record.ai_risk_summary = lines[2] if len(lines) > 2 else ''
                record.ai_doc_recommend = lines[3] if len(lines) > 3 else ''

                self.env['ai.analysis.log'].create({
                    'project_id': record.id,
                    'ai_plan_brief': record.ai_plan_brief,
                    'ai_invest_hint': record.ai_invest_hint,
                    'ai_risk_summary': record.ai_risk_summary,
                    'ai_doc_recommend': record.ai_doc_recommend,
                })

            except Exception as e:
                _logger.error(f"[AI调用失败] 项目: {record.name}, 错误: {str(e)}", exc_info=True)
                raise UserError(f"AI调用失败：{str(e)}")

    def create_tasks_from_templates(self):
        for stage in self.env['project.project.stage'].search([]):
            for task_template in stage.task_template_ids:
                self.env['project.task'].create({
                    'name': task_template.name,
                    'project_id': self.id,
                    'project_stage_id': stage.id,
                    'description': task_template.description,
                    'sequence': task_template.sequence,
                    'template_id': task_template.id,
                })

    @api.model
    def create(self, vals):
        if vals.get('prj_num', _('New')) == _('New'):
            vals['prj_num'] = self.env['ir.sequence'].next_by_code('project.project') or _('New')
        project = super(ProjectProject, self).create(vals)
        project.create_tasks_from_templates()
        return project

    def action_ai_suggestion(self):
        for record in self:
            prompt = f"""
你是一个经验丰富的工程项目顾问，请基于以下信息给出建议：
1. 项目任务结构应包括哪些阶段和关键任务？
2. 项目投资额度是否合理？初步估算应该是多少？
3. 项目可能存在哪些管理、技术或政策风险？
4. 推荐需要准备哪些文档？

项目名称：{record.name}
项目类型：{getattr(record, 'x_project_type', '')}
投资金额：{getattr(record, 'x_budget_total', 0)} 万元
工期：{getattr(record, 'x_duration_days', 180)} 天
建设位置：{getattr(record, 'x_location', '')}
"""
            headers = {
                "Authorization": "sk-53fbaeb5ebbe46d5a4e5d3a101afa209",
                "Content-Type": "application/json"
            }
            payload = {
                "model": "deepseek-chat",
                "messages": [
                    {"role": "system", "content": "你是一个工程顾问"},
                    {"role": "user", "content": prompt}
                ],
                "temperature": 0.7
            }
            try:
                response = requests.post(
                    "https://api.deepseek.com/v1/chat/completions",
                    headers=headers,
                    json=payload,
                    timeout=60
                )
                result = response.json()
                content = result.get("choices", [{}])[0].get("message", {}).get("content", "")
                lines = content.strip().split('\n')
                record.ai_plan_brief = lines[0] if len(lines) > 0 else ''
                record.ai_invest_hint = lines[1] if len(lines) > 1 else ''
                record.ai_risk_summary = lines[2] if len(lines) > 2 else ''
                record.ai_doc_recommend = lines[3] if len(lines) > 3 else ''
                self.env['ai.analysis.log'].create({
                    'project_id': record.id,
                    'ai_plan_brief': record.ai_plan_brief,
                    'ai_invest_hint': record.ai_invest_hint,
                    'ai_risk_summary': record.ai_risk_summary,
                    'ai_doc_recommend': record.ai_doc_recommend,
                })
                return {
                    'type': 'ir.actions.client',
                    'tag': 'display_ai_advice',
                    'params': {'advice': {"任务建议": content}}
                }
            except Exception as e:
                raise UserError(f"AI调用失败：{str(e)}")

    def action_save_ai_as_template(self):
        for rec in self:
            if not rec.ai_plan_brief:
                raise UserError("当前项目尚无AI任务结构建议，无法保存为模板")
            template = self.env['project.task.template'].create({
                'name': f"{rec.name}_AI模板",
                'project_type': rec.x_project_type or '默认',
                'description': rec.ai_plan_brief,
                'origin_project_id': rec.id
            })
            return {
                'type': 'ir.actions.act_window',
                'name': '任务模板',
                'view_mode': 'form',
                'res_model': 'project.task.template',
                'res_id': template.id,
                'target': 'current'
            }

    def action_export_ai_report(self):
        from docx import Document
        import tempfile
        import base64
        from odoo.tools import misc

        for rec in self:
            template_path = misc.file_open(
                'Engineering_Project_Management/static/report_template/project_ai_report_sample.docx').name
            doc = Document(template_path)
            for p in doc.paragraphs:
                p.text = p.text.replace("{{ai_plan_brief}}", rec.ai_plan_brief or "")
                p.text = p.text.replace("{{ai_invest_hint}}", rec.ai_invest_hint or "")
                p.text = p.text.replace("{{ai_risk_summary}}", rec.ai_risk_summary or "")
                p.text = p.text.replace("{{ai_doc_recommend}}", rec.ai_doc_recommend or "")
            tmp = tempfile.NamedTemporaryFile(delete=False, suffix='.docx')
            doc.save(tmp.name)
            tmp.seek(0)
            content = tmp.read()
            tmp.close()
            attachment = self.env['ir.attachment'].create({
                'name': f"{rec.name}_AI立项建议书.docx",
                'type': 'binary',
                'datas': base64.b64encode(content),
                'res_model': self._name,
                'res_id': rec.id,
                'mimetype': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
            })
            return {
                'type': 'ir.actions.act_url',
                'url': f'/web/content/{attachment.id}?download=true',
                'target': 'new'
            }
