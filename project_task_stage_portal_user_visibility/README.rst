.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
    :target: http://www.gnu.org/licenses/agpl
    :alt: License: AGPL-3

====================================
Project Task Stage Portal Visibility
====================================

This module allows to hide tasks for portal users depending on the task's stage.


Installation
============

To install this module, you need to:

#. Only install


Configuration
=============

To configure this module, you need to:

#. Go to Project > Configuration > Task Stages.
#. Activate the "View In Portal" option in the Task Stage form view in order to make the tasks in that stage visible to portal users.


Usage
=====

To use this module, you need to:

#. The "View In Portal" option in Task Stages is disabled by default, which means that portal users will be unable to see any task in portal until the "View In Portal" option is activated in one or more Task Stages.
#. It is important to keep in mind that this module adds a new condition to the standard tasks access rule for portal users: even if the Task Stage has the "View In Portal" option activated, portal users will only be able to view the tasks if they belong to the followers list of the project or the the followers list of the task.


ROADMAP
=======

[ Enumerate known caveats and future potential improvements.
  It is mostly intended for end-users, and can also help
  potential new contributors discovering new features to implement. ]

* ...


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

* Manuel Regidor <manuel.regidor@sygel.es>


Maintainer
~~~~~~~~~~

This module is maintained by Sygel.

.. image:: https://www.sygel.es/logo.png
   :alt: Sygel
   :target: https://www.sygel.es

This module is part of the `Sygel/sy-project <https://github.com/sygel-technology/sy-project>`_.

To contribute to this module, please visit https://github.com/sygel.
