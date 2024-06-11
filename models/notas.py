from random import randint
from odoo import api, fields, models


class notas(models.Model):   # hereda de models.models
    _name = 'oe.school.notas'
    codigo = fields.Char(string='codigo', required=True ,size=10)
    name = fields.Char(string='nombre_estudiante', required=True)
    descripcion = fields.Text(string='descripcion')
    gestion = fields.Integer(string='gestion', required=True)
    materia_id = fields.Many2one('oe.school.materia', string='materia_id', required=True)
    student_id = fields.Many2one('res.partner', string='Student', required=True, ondelete='cascade', index=True, copy=False)
    nota = fields.Float(string='Nota', digits=(3, 2), required=True, help="Inserte la nota (máximo 100)")