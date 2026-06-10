# -*- coding: utf-8 -*-
"""
Master data model for helpdesk ticket categories.

Categories classify tickets (e.g. Hardware, Software, Network) and are
maintained by Helpdesk Managers while users select them on tickets.
"""

from odoo import fields, models


class HelpdeskCategory(models.Model):
    """Ticket category used to classify helpdesk requests."""

    _name = 'helpdesk.category'
    _description = 'Helpdesk Category'
    _order = 'name'

    name = fields.Char(
        string='Name',
        required=True,
    )
    description = fields.Text(
        string='Description',
    )
