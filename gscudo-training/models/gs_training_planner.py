from odoo import api, fields, models


class GSTrainingPlanner(models.Model):
    _name = 'gs_training_planner'
    _description = 'Planner Formazione'

    name = fields.Char(string='Name')