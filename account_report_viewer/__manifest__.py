# -*- coding: utf-8 -*-
# Copyright 2018 Akretion (http://www.akretion.com)
# @author Alexis de Lattre <alexis.delattre@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Account Report Viewer',
    'summary': """Access Report submenu to Viewers""",
    'version': '10.0.1.0.0',
    'category': 'Accounting',
    'license': 'AGPL-3',
    'description': """
Account Report Viewer
=====================

This module adds access to the menu *Accounting > Reports > Business Intelligence* to Invoice Viewers.

This module has been written by Alexis de Lattre from Akretion
<alexis.delattre@akretion.com>.
    """,
    'author': 'Akretion',
    'website': 'http://www.akretion.com',
    'depends': ['account_viewer'],
    'data': [
        'views/account.xml',
    ],
    'installable': True,
}
