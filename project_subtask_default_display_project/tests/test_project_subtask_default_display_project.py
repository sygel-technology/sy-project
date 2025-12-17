# Copyright 2025 Ángel García de la Chica Herrera <angel.garcia@sygel.es>
# License AGPL-3 - See https://www.gnu.org/licenses/agpl-3.0

from odoo.tests.common import Form

from odoo.addons.project.tests.test_project_base import TestProjectCommon


class TestProjectSubtaskDefaultDisplayProject(TestProjectCommon):
    def test_create_subtask(self):
        """It is necessary to remove the many2many widget to be able to
        create a subtask directly from the tree view and to check that
        the display_project field is correctly passed.
        """
        with Form(self.task_1) as f:
            with f.child_ids.new() as line:
                line.name = "subtask"
        f.save()
        self.assertEqual(self.task_1.project_id, line.project_id)
        self.assertTrue(line.display_in_project)
