from openerp.osv import osv, fields
from openerp import api
from openerp.tools.translate import _


class CreateAppointment(osv.TransientModel):
    _name = "create.appointment"
    _columns = {
        'student_id': fields.many2one('school.students', string='Student'),
        'appointment_date': fields.date(string="Appointment Date")
    }

    @api.multi
    def action_create_appointment(self):
        vals = {
            'student_id': self.student_id.id,
            'date_appointment': self.appointment_date,

        }

        appointment_rec = self.env['school.appointment'].create(vals)
        print("appointment", appointment_rec.id)
        return {
            'name': _('Appointment'),
            'type': 'ir.actions.act.window',
            'view_mode': 'form',
            'res_model': 'school.appointment',
            'res_id': appointment_rec.id,
            'target': 'new'

        }
