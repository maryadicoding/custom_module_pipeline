# -*- coding: utf-8 -*-

from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    x_type = fields.Selection([
        ('key acc client', 'Key Acc Client'),
        ('existing small client', 'Existing Small Client'), 
        ('referral', 'Referral')], string='Customer Group')