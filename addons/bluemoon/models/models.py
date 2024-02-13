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
            if record.user and record.user.name:
                record.name = record.user.name + " Simulation - " + str(record.id)
            else:
                record.name = "Simulation - " + str(record.id)


class User(models.Model):
    _name = 'bluemoon.user'
    _description = 'User'

    name = fields.Char(string="Name", required=True)
    email = fields.Char(string="Email", required=True)
    phone = fields.Char(string="Phone", required=True)
    address = fields.Char(string="Address", required=True)


    simulations = fields.One2many('bluemoon.simulation', 'user', string="Simulations")
    simulation_count = fields.Integer(string="Simulation Count", compute="_compute_simulation_count", store=True)
    intercambios_exitosos = fields.Integer(string="Intercambios Exitosos",
                                           compute="_compute_intercambios_exitosos_y_fallidos", store=True)
    intercambios_fallidos = fields.Integer(string="Intercambios Fallidos",
                                           compute="_compute_intercambios_exitosos_y_fallidos", store=True)
    porcentaje_exitosos = fields.Float(string="Porcentaje de Intercambios Exitosos", compute="_compute_porcentajes",
                                       store=True)
    porcentaje_fallidos = fields.Float(string="Porcentaje de Intercambios Fallidos", compute="_compute_porcentajes",
                                       store=True)

    @api.depends('simulations')
    def _compute_simulation_count(self):
        for user in self:
            user.simulation_count = len(user.simulations)

    @api.depends('simulations.total')
    def _compute_intercambios_exitosos_y_fallidos(self):
        for user in self:
            simulations = user.simulations.filtered(lambda s: s.total != 0)
            user.intercambios_exitosos = len(simulations)
            user.intercambios_fallidos = user.simulation_count - user.intercambios_exitosos

    @api.depends('simulation_count', 'intercambios_exitosos')
    def _compute_porcentajes(self):
        for user in self:
            user.porcentaje_exitosos = (user.intercambios_exitosos / user.simulation_count) * 100 if user.simulation_count > 0 else 0
            user.porcentaje_fallidos = 100 - user.porcentaje_exitosos




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

    total_sold_count = fields.Integer(string="Total Sold Count", compute='_compute_total_sold_count', store=True)
    sold_count = fields.Integer(string="Sold Count", compute="_compute_sold_count", store=True)
    @api.depends('material_type', 'silver_quality')
    def _compute_total_sold_count(self):
        for product in self:
            product.total_sold_count = self.env['bluemoon.catalogue'].search_count([
                ('material_type', '=', product.material_type),
                ('silver_quality', '=', product.silver_quality),
                ('price', '=', product.price),
                ('size', '=', product.size)
            ])

    @api.depends('total_sold_count')
    def _compute_sold_count(self):
        self.sold_count = self.env['bluemoon.catalogue'].search_count([('total_sold_count', '>', 0)])
