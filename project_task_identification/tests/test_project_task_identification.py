# Copyright 2025 Ángel García de la Chica Herrera <angel.garcia@sygel.es>
# License AGPL-3 - See https://www.gnu.org/licenses/agpl-3.0

from odoo.addons.project.tests.test_project_base import TestProjectCommon


class TestProjectTaskIdentification(TestProjectCommon):
    def test_create_new_task(self):
        task = self.env["project.task"].create(
            {"name": "Task test", "project_id": self.project_pigs.id}
        )
        self.assertEqual(task.sy_id, "T-{}".format(task.id))
