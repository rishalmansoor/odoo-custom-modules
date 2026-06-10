# -*- coding: utf-8 -*-
"""
Module manifest for helpdesk_ticketing.

Declares metadata, dependencies, and the ordered list of data files
that Odoo loads when the module is installed or upgraded.
"""

{
    'name': 'Helpdesk Ticketing',
    'version': '18.0.1.0.0',
    'category': 'Services/Helpdesk',
    'summary': 'Track internal IT support requests',
    'description': """
Helpdesk Ticketing
==================

Track internal IT support requests with ticket numbers, priorities,
assignments, and lifecycle statuses.
    """,
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'license': 'LGPL-3',
    'depends': [
        'base',
    ],
    'data': [
        # Security must load before views and menus.
        'security/helpdesk_security.xml',
        'security/ir.model.access.csv',
        # Sequence must exist before tickets are created.
        'data/helpdesk_sequence.xml',
        'views/helpdesk_ticket_views.xml',
        'views/helpdesk_menu.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
