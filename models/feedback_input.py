from odoo import api, fields, models, _


class FeedbackInput(models.Model):
    _name = "feedback.input"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Feedback From"
    _rec_name = 'employee_id'

    # name = fields.Char(String="Employee Reference", required=True, copy=False,
    #                    readonly=True, default= lambda self: _('New'))
    employee_id = fields.Many2one("hr.employee", String="Employee Name", required=True)

    mobile_phone = fields.Char(related="employee_id.mobile_phone")
    work_email = fields.Char(related="employee_id.work_email")
    manager = fields.Char(related="employee_id.parent_id.name")
    coach = fields.Char(related="employee_id.coach_id.name")

    input_status = fields.Selection([
        ('draft', 'Draft'),
        ('employee_approved', 'Employee Approved'),
        ('manager_approved', 'Manager Approved'),
        ('ceo_approved', 'CEO Approved'),
        ('cancel', 'Cancel')
    ], String="Status", default="draft", trackig=True)

    def action_employee(self):
        for rec in self:
            rec.input_status = 'employee_approved'

    def action_manager(self):
        for rec in self:
            rec.input_status = 'manager_approved'

    def action_ceo(self):
        for rec in self:
            rec.input_status = 'ceo_approved'

    def action_cancel(self):
        for rec in self:
            rec.input_status = 'cancel'
