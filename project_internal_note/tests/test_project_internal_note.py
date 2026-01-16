# Copyright 2025 Ángel García de la Chica Herrera <angel.garcia@sygel.es>
# License AGPL-3 - See https://www.gnu.org/licenses/agpl-3.0

from odoo.tests import common


class TestProjectInternalNote(common.TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user_projectmanager_01 = cls.env["res.users"].create(
            {
                "name": "ProjectManager01",
                "login": "ProjectManager01",
                "email": "ProjectManager01@example.com",
            }
        )
        cls.project_01 = (
            cls.env["project.project"]
            .with_context(**{"mail_create_nolog": True})
            .create(
                {
                    "name": "Project",
                    "user_id": cls.user_projectmanager_01.id,
                    "project_internal_note": "Test Internal note Project 01",
                }
            )
        )
        cls.project_02 = (
            cls.env["project.project"]
            .with_context(**{"mail_create_nolog": True})
            .create(
                {
                    "name": "Project",
                    "user_id": cls.user_projectmanager_01.id,
                    "project_internal_note": "Test Internal note Project 02",
                }
            )
        )

    def test_create_task(self):
        task = self.env["project.task"].create(
            {"name": "Task Test", "project_id": self.project_01.id}
        )
        self.assertEqual(
            self.project_01.project_internal_note, task.project_internal_note
        )

    def test_edit_task(self):
        task = self.env["project.task"].create(
            {"name": "Task Test", "project_id": self.project_01.id}
        )
        task.write({"project_id": self.project_02.id})
        self.assertEqual(
            self.project_02.project_internal_note, task.project_internal_note
        )
