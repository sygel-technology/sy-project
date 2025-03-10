# Copyright 2025 Ángel García de la Chica Herrera <angel.garcia@sygel.es>
# License AGPL-3 - See https://www.gnu.org/licenses/agpl-3.0

from odoo.exceptions import UserError
from odoo.tests import common


class TestProjectOdooVersion(common.TransactionCase):
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
                    "odoo_version": cls.env.ref("project_odoo_version.odoo_v17").id,
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
                    "odoo_version": cls.env.ref("project_odoo_version.odoo_v18").id,
                }
            )
        )

    def test_create_task(self):
        task = self.env["project.task"].create(
            {"name": "Task Test", "project_id": self.project_01.id}
        )
        self.assertEqual(self.project_01.odoo_version, task.odoo_version)

    def test_edit_task(self):
        task = self.env["project.task"].create(
            {"name": "Task Test", "project_id": self.project_01.id}
        )
        task.write({"project_id": self.project_02.id})
        self.assertEqual(self.project_02.odoo_version, task.odoo_version)

    def test_unique_odoo_version_name(self):
        with self.assertRaises(UserError):
            self.env["project.odoo.version"].create({"name": "18"})

    def test_select_archived_odoo_version(self):
        v10_id = self.env.ref("project_odoo_version.odoo_v10")
        v10_id.active = False
        with self.assertRaises(UserError):
            self.project_01.odoo_version = v10_id

    def test_archive_used_odoo_version(self):
        with self.assertRaises(UserError):
            self.env.ref("project_odoo_version.odoo_v18").active = False

    def test_delete_used_odoo_version(self):
        with self.assertRaises(UserError):
            self.env.ref("project_odoo_version.odoo_v18").unlink()
