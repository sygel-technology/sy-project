# Copyright 2025 Ángel García de la Chica Herrera <angel.garcia@sygel.es>
# License AGPL-3 - See https://www.gnu.org/licenses/agpl-3.0

from odoo.addons.project.tests.test_project_base import TestProjectCommon


class TestProjectSubtaskParentIdentification(TestProjectCommon):
    def test_create_and_edit_new_subtask(self):
        subtask = self.env["project.task"].create(
            {
                "name": "Task test",
                "project_id": self.project_pigs.id,
                "parent_id": self.task_1.id,
            }
        )
        self.assertEqual(subtask.sy_parent_id, " -> {}".format(self.task_1.sy_id))
        subtask.write({"parent_id": self.task_2.id})
        self.assertEqual(subtask.sy_parent_id, " -> {}".format(self.task_2.sy_id))
