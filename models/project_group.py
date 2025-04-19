from odoo import models, fields, api

class ProjectGroup(models.Model):
    _name = 'project.group'
    _description = 'Project Group'

    name = fields.Char(string='Project Group Name', required=True)
    project_ids = fields.One2many('project.project', 'project_group_id', string='Projects')
    description = fields.Text(string='Description')
