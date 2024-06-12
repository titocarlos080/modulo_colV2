from random import randint
from odoo import api, fields, models


class Nivel(models.Model):
    _name = 'oe.school.comunicados'
    
    name = fields.Char(string='nombre', required=True)
    descripcion = fields.Text(string='descripcion')
    
     
 