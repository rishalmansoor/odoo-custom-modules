# -*- coding: utf-8 -*-
"""
Business model for internal IT support tickets.

Defines the helpdesk.ticket model with fields for subject, priority,
status, assignment, category, and automatic ticket number generation
via ir.sequence. Inherits mail.thread and mail.activity.mixin for
chatter, followers, and scheduled activities.
"""

from odoo import api, fields, models, _


class HelpdeskTicket(models.Model):
    """Internal IT support request."""

    _name = 'helpdesk.ticket'
    _description = 'Helpdesk Ticket'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'create_date desc, id desc'

    ticket_no = fields.Char(
        string='Ticket Number',
        required=True,
        copy=False,
        readonly=True,
        default=lambda self: _('New'),
    )
    subject = fields.Char(
        string='Subject',
        required=True,
    )
    description = fields.Text(
        string='Description',
    )
    category_id = fields.Many2one(
        comodel_name='helpdesk.category',
        string='Category',
        ondelete='restrict',
    )
    priority = fields.Selection(
        selection=[
            ('0', 'Low'),
            ('1', 'Medium'),
            ('2', 'High'),
        ],
        string='Priority',
        default='1',
        required=True,
        tracking=True,
    )
    status = fields.Selection(
        selection=[
            ('new', 'New'),
            ('in_progress', 'In Progress'),
            ('resolved', 'Resolved'),
            ('closed', 'Closed'),
        ],
        string='Status',
        default='new',
        required=True,
        tracking=True,
    )
    assigned_user_id = fields.Many2one(
        comodel_name='res.users',
        string='Assigned To',
        tracking=True,
    )
    resolution_date = fields.Datetime(
        string='Resolution Date',
    )

    @api.model_create_multi
    def create(self, vals_list):
        """Assign a sequence number to each new ticket."""
        for vals in vals_list:
            if vals.get('ticket_no', _('New')) == _('New'):
                vals['ticket_no'] = (
                    self.env['ir.sequence'].next_by_code('helpdesk.ticket')
                    or _('New')
                )
        return super().create(vals_list)
