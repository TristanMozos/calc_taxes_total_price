# -*- coding: utf-8 -*-
# Copyright 2021 Halltic Tech S.L. ()
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name':'Calculate taxes with price included',
    'version':'0.1.0',
    'category':'Accounting',
    'author':'Halltic Tech S.L.',
    'maintainer':'Halltic Tech S.L.',
    'website':'https://www.halltic.com',
    'summary':'Module for calculate taxes from total price',
    'description':"""
.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

Installation
============

To install this module, you need to:

#. Do this ...



Usage
=====

To use this module, you only need to install it 

Credits
=======

Contributors
------------

* Tristán Mozos Pérez <tristan.mozos@halltic.com>

Funders
-------

The development of this module has been financially supported by:

* Halltic Tech S.L.

Maintainer
----------
This module is maintained by the Halltic Tech S.L.
""",

    # any module necessary for this one to work correctly
    'depends':['account'],

    # always loaded
    'data':[],

    'js':[],
    'css':[],
    'qweb':[],

    'installable':True,
    # Install this module automatically if all dependency have been previously
    # and independently installed.  Used for synergetic or glue modules.
    'auto_install':False,
    'application':False,
}
