from odoo import api, fields, models, _


class FeedbackInput(models.Model):
    _name = "feedback.input"
    _description = "Feedback From"

    name = fields.Char(String="Employee Name", help="Employee Name")
