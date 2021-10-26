from openerp.osv import osv, fields

# Student Module
class school_students(osv.Model):
    _name = "school.students"
    _columns = {
        'name': fields.char('Name', size=64),
        'birthdate': fields.date('Birth Date'),
        'class_id': fields.many2one('school.class', 'Class'),
        'teachers_id': fields.many2one('school.teachers', 'Teachers'),
        'subjects_id': fields.many2many('school.subjects', 'rel_students_subjects', 'students_id', 'subjects_id', string="Subjects"),
        'history': fields.text("History"),
        'activity': fields.text("Activity"),
        'res_partner_id': fields.many2one('res.partner', 'Parents'),
        'image': fields.binary("Image"),
    }
school_students()


class school_res_partner(osv.Model):
    _inherit = "res.partner"
    _columns = {
        # 'name': fields.char('Name', size=64),
        'students_id': fields.one2many('school.students', 'res_partner_id', string="Children")

    }

class school_class(osv.Model):
    _name = "school.class"
    _columns = {
        'name': fields.char('Name', size=64),
        'teachers_id': fields.many2one('school.teachers', 'Teachers')
    }


class school_teachers(osv.Model):
    _name = "school.teachers"
    _columns = {
        'name': fields.char('Name', size=64),
        'class_id': fields.one2many('school.class', 'teachers_id', string='Class')
    }


class school_subjects(osv.Model):
    _name = "school.subjects"
    _columns = {
            'name': fields.char('Name', size=64)
    }