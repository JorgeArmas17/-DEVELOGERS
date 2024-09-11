from odoo import fields, models, api
from datetime import date

class SchoolStudent(models.Model):
    _name = "school.student"

    name = fields.Char(string="Student Name")

    birth_date = fields.Date(string="Birth Date")

    age = fields.Integer(string="Age", compute="_compute_age")

    final_exam_grade = fields.Float(string="Final Exam Grade")

    subject_ids = fields.Many2many(comodel_name='school.subject', string="Subjects")

    @api.depends('birth_date')
    def _compute_age(self):
        for student in self:
            if student.birth_date:
                today = date.today()
                born = student.birth_date
                student.age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
            else:
                student.age = 0