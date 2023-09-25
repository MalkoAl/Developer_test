# -*- coding: utf-8 -*-

from odoo import models, fields, api


class developers_management(models.Model):
    _name = 'developers_management.developers_management'
    _description = 'developers_management.developers_management'

    name = fields.Char(required=True, unique=True)
    type = fields.Selection([
        ('front-end', 'Front-end'),
        ('backend', 'Backend'),
        ('fullstack', 'Fullstack'),
        ('out-stuff', 'Out Stuff')
    ], string="Type")

    global_identification = fields.Char(compute="_compute_global_identification", store=True)
    address = fields.Text()
    email = fields.Char()
    phone = fields.Char()
    birthday = fields.Date()
    rank = fields.Char()
    company_id = fields.Many2one('developers_management.company', string="Company")

    @api.depends('name', 'type')
    def _compute_global_identification(self):
        for record in self:
            if record.name and record.type:
                record.global_identification = str(record.name) + '-' + str(record.type)
            else:
                record.global_identification = ''


class Company(models.Model):
    _name = 'developers_management.company'

    name = fields.Char()
    address = fields.Text()
    developer_id = fields.One2many('developers_management.developers_management', 'company_id', string="Developer's")
