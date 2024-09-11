from odoo import fields, models

class SchoolSubject(models.Model):
    _name = "school.subject"

    name = fields.Char(string="Subject Name")
    
    credits = fields.Integer(string="Credits")
    
    max_students = fields.Integer(string="Max Students")
    
    active = fields.Boolean(string="Active", default=True)
    
    student_ids = fields.Many2many(comodel_name='school.student', string="Students")
    
    teacher_id = fields.Many2one(comodel_name='school.teacher', string="Teacher")
