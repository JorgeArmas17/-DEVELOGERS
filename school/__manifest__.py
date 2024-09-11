{
    "name": "School",
    "version": "16.0.1.0.1",
    "author": "Jorge Armas",
    "category": "Tools",
    "summary": "Relate Sign Item Type and IR Sequence",
    "depends": ["base", "sign"],
    "data": [
        'security/ir.model.access.csv',
        'views/school_teacher_views.xml',
        'views/school_subject_views.xml',
        'views/school_student_views.xml',
        'views/menu_item.xml',
    ],
    'installable': True,
    'application': True,
    "license": "OPL-1",
}
