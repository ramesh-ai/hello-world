from odoo import models,fields,api
class test1(models.Model):
    _name = 'test.example'
    name=fields.Char('name')
    age=fields.Integer('age')
