# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Simulation(models.Model):
    _name = 'bluemoon.simulation'
    _description = 'Simulation'

    name = fields.Char(string="Name", compute="_compute_name", store=True)
    silverQuantity = fields.Float(string="Silver Quantity", required=True)
    silverPrice = fields.Float(string="Silver Price", required=True)
    user = fields.Many2one('bluemoon.user', string="User", required=True)

    total = fields.Float(string="Total", compute="_compute_total", store=True)

    @api.depends('silverQuantity', 'silverPrice')
    def _compute_total(self):
        for record in self:
            record.total = record.silverQuantity * record.silverPrice

    @api.depends('user')
    def _compute_name(self):
        for record in self:
            record.name = record.user.name + " Simulation - " + str(record.id)

class User(models.Model):
    _name = 'bluemoon.user'
    _description = 'User'

    name = fields.Char(string="Name", required=True)
    email = fields.Char(string="Email", required=True)
    phone = fields.Char(string="Phone", required=True)
    address = fields.Char(string="Address", required=True)

    simulations = fields.One2many('bluemoon.simulation', 'user', string="Simulations")

class Bluemoon_Catalogue(models.Model):
    _name = 'bluemoon.catalogue'
    _description = 'Catalogue for Blue Moon'

    name = fields.Char(string="Name", required=True, help="Introduce the name of material")
    material_type = fields.Selection([
        ('0', 'Steel'),
        ('1', 'Silver'),
        ('2', 'Other')
    ], string="Material Type", required=True)
    price = fields.Float(string="Price")
    size = fields.Integer(string="Size")
    silver_quality = fields.Selection([
        ('800', '800 (80% purity)'),
        ('900', '900 (90% purity)'),
        ('925', '925 (92.5% purity)'),
        ('999', '999 (100% purity)')
    ], help="Select the purity level for silver")