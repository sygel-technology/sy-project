.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
	:target: http://www.gnu.org/licenses/agpl
	:alt: License: AGPL-3

======================================
Project Task Restrict Stage Timesheets
======================================

This module allows you to configure task stages in which users cound not create, edit, or delete timesheets 
unless they are part of a permission group


Installation
============

To install this module, you need to:

#. Only install


Configuration
=============

To configure this module, you need to:

#. Go to Project / Configuration / Stages and mark the "Restrict Timesheets" field in the desired stages
#. Go to Settings / User & Companies / Users and mark the "Skip task stage timesheet restriction" group.
   Only that users will have permission create, edit, or delete the timesheets of tasks with that stage


Usage
=====

To use this module, you need to:

#. Create, edit, or delete a timesheet of a task on a restricted stage with a user without permissions. A warning will be displayed



Bug Tracker
===========

Bugs and errors are managed in `issues of GitHub <https://github.com/sygel-technology/sy-project/issues>`_.
In case of problems, please check if your problem has already been
reported. If you are the first to discover it, help us solving it by indicating
a detailed description `here <https://github.com/sygel-technology/sy-project/issues/new>`_.

Do not contact contributors directly about support or help with technical issues.


Credits
=======

Authors
~~~~~~~

* Sygel, Odoo Community Association (OCA)


Contributors
~~~~~~~~~~~~

* Valentin Vinagre <valentin.vinagre@sygel.es>
* Alberto Martínez <alberto.martinez@sygel.es>


Maintainer
~~~~~~~~~~

This module is maintained by Sygel.

.. image:: https://www.sygel.es/logo.png
   :alt: Sygel
   :target: https://www.sygel.es

This module is part of the `Sygel/sy-project <https://github.com/sygel-technology/sy-project>`_.

To contribute to this module, please visit https://github.com/sygel-technology/.

