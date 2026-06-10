{
    'name': 'Helpdesk Ticketing',
    'version': '18.0.2.0.0',
    'category': 'Services/Helpdesk',
    'summary': 'Track internal IT support requests with categories and chatter',
    'description': """
Helpdesk Ticketing
==================

Track internal IT support requests with ticket numbers, priorities,
assignments, categories, lifecycle statuses, chatter, and activities.
    """,
    'author': 'Muhammad Rishal Mansoor',
    'website': 'https://github.com/rishalmansoor',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'mail',
    ],
    'data': [
        'security/helpdesk_security.xml',
        'security/ir.model.access.csv',
        'data/helpdesk_sequence.xml',
        'views/helpdesk_category_views.xml',
        'views/helpdesk_ticket_views.xml',
        'views/helpdesk_menu.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
