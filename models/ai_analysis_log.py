
from odoo import models, fields

class AIAnalysisLog(models.Model):
    _name = 'ai.analysis.log'
    _description = 'AI 分析记录'

    project_id = fields.Many2one('project.project', string='所属项目', required=True, ondelete='cascade')
    analyzed_by = fields.Many2one('res.users', string='分析发起人', default=lambda self: self.env.uid)
    analyzed_at = fields.Datetime(string='分析时间', default=fields.Datetime.now)
    ai_plan_brief = fields.Text(string='任务结构建议')
    ai_invest_hint = fields.Text(string='投资建议')
    ai_risk_summary = fields.Text(string='风险提示')
    ai_doc_recommend = fields.Text(string='推荐文档')
