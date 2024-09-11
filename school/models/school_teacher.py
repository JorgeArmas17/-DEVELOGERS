from odoo import fields, models

class SchoolTeacher(models.Model):
    _name = "school.teacher"

    name = fields.Char(string="Teacher Name")
    
    profile = fields.Text(string="Profile")
    
    subject_ids = fields.One2many(comodel_name='school.subject', inverse_name='teacher_id', string="Subjects")
