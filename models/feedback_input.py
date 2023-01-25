from odoo import api, fields, models, _


class FeedbackInput(models.Model):
    _name = "feedback.input"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Feedback From"
    _rec_name = 'employee_id'

    reference = fields.Char(String="Input Reference", required=True, copy=False,
                            readonly=True, default=lambda self: _('New'))
    employee_id = fields.Many2one("hr.employee", String="Employee Name", required=True)
    name = fields.Char(related="employee_id.name")
    photo = fields.Image(related="employee_id.image_1920")
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

    # Evaluation Points

    brand_dev_awarness = fields.Selection([
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    ], String="Brand Development and Awareness", tracking=True)

    website_and_social = fields.Selection([
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    ], String="Website and Social Media Management", tracking=True)

    seo_opt = fields.Selection([
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    ], String="SEO Optimization", tracking=True)

    report_gen = fields.Selection([
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    ], String="Report Generation", tracking=True)

    community_management = fields.Selection([
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    ], String="Community Management", tracking=True)

    client_acquisition = fields.Selection([
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    ], String="Client Acquisition", tracking=True)

    employee_evaluation = fields.Char(compute="_compute_employee_evaluation")

    # Direct Manager Ratings

    m_attendance = fields.Selection([
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    ], String="Attendance & Punctuality", tracking=True)

    m_leaves = fields.Selection([
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    ], String="Leaves", tracking=True)

    m_attitude = fields.Selection([
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    ], String="Attitude", tracking=True)

    m_office_discipline = fields.Selection([
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    ], String="Office Discipline", tracking=True)

    m_compliance = fields.Selection([
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    ], String="Compliance with Organization Policies", tracking=True)

    m_office_decorum = fields.Selection([
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    ], String="Office Decorum", tracking=True)

    m_proactiveness = fields.Selection([
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    ], String="Proactiveness", tracking=True)

    manager_rating = fields.Char(compute="_compute_manager_rating")

    # HR Rating

    hr_attendance = fields.Selection([
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    ], String="Attendance & Punctuality", tracking=True)

    hr_leaves = fields.Selection([
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    ], String="Leaves", tracking=True)

    hr_attitude = fields.Selection([
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    ], String="Attitude", tracking=True)

    hr_office_discipline = fields.Selection([
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    ], String="Office Discipline", tracking=True)

    hr_compliance = fields.Selection([
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    ], String="Compliance with Organization Policies", tracking=True)

    hr_office_decorum = fields.Selection([
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    ], String="Office Decorum", tracking=True)

    hr_proactiveness = fields.Selection([
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    ], String="Proactiveness", tracking=True)

    hr_rating = fields.Char(compute="_compute_hr_rating")

    # CEO Rating

    ceo_attendance = fields.Selection([
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    ], String="Attendance & Punctuality", tracking=True)

    ceo_leaves = fields.Selection([
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    ], String="Leaves", tracking=True)

    ceo_attitude = fields.Selection([
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    ], String="Attitude", tracking=True)

    ceo_office_discipline = fields.Selection([
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    ], String="Office Discipline", tracking=True)

    ceo_compliance = fields.Selection([
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    ], String="Compliance with Organization Policies", tracking=True)

    ceo_office_decorum = fields.Selection([
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    ], String="Office Decorum", tracking=True)

    ceo_proactiveness = fields.Selection([
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    ], String="Proactiveness", tracking=True)

    ceo_rating = fields.Char(compute="_compute_ceo_rating")

    # Logic

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

    # Employee Rating
    @api.depends('brand_dev_awarness', 'website_and_social', 'seo_opt',
                 'report_gen', 'community_management', 'client_acquisition')
    def _compute_employee_evaluation(self):
        for rec in self:
            rec.employee_evaluation = int(rec.brand_dev_awarness) + int(rec.website_and_social)\
                                   + int(rec.seo_opt) + int(rec.report_gen) + int(rec.community_management)\
                                   + int(rec.client_acquisition)

    # Direct Manager Rating
    @api.depends('m_attendance', 'm_leaves', 'm_attitude',
                 'm_office_discipline', 'm_compliance', 'm_office_decorum', "m_proactiveness")
    def _compute_manager_rating(self):
        for rec in self:
            rec.manager_rating = int(rec.m_attendance) + int(rec.m_leaves) \
                                      + int(rec.m_attitude) + int(rec.m_office_discipline) + int(rec.m_compliance) \
                                      + int(rec.m_office_decorum) + int(rec.m_proactiveness)

    # HR Rating
    @api.depends('hr_attendance', 'hr_leaves', 'hr_attitude',
                 'hr_office_discipline', 'hr_compliance', 'hr_office_decorum', "hr_proactiveness")
    def _compute_hr_rating(self):
        for rec in self:
            rec.hr_rating = int(rec.hr_attendance) + int(rec.hr_leaves) \
                                      + int(rec.hr_attitude) + int(rec.hr_office_discipline) + int(rec.hr_compliance) \
                                      + int(rec.hr_office_decorum) + int(rec.hr_proactiveness)

    # CEO Rating
    @api.depends('ceo_attendance', 'ceo_leaves', 'ceo_attitude',
                 'ceo_office_discipline', 'ceo_compliance', 'ceo_office_decorum', "ceo_proactiveness")
    def _compute_ceo_rating(self):
        for rec in self:
            rec.ceo_rating = int(rec.ceo_attendance) + int(rec.ceo_leaves) \
                                      + int(rec.ceo_attitude) + int(rec.ceo_office_discipline) + int(rec.ceo_compliance) \
                                      + int(rec.ceo_office_decorum) + int(rec.ceo_proactiveness)

    @api.model
    def create(self, vals):
        if vals.get('reference', _("New")) == _("New"):
            vals['reference'] = self.env['ir.sequence'].next_by_code(
                'feedback.input') or _("New")
        res = super(FeedbackInput, self).create(vals)
        return res
