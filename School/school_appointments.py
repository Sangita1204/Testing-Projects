from openerp.osv import fields, osv

class school_appointments(osv.Model):
    _name = "school.appointment"
    _columns = {
        'student_id': fields.many2one('school.students', 'Appointments'),
        'appointment_date': fields.date()
    }