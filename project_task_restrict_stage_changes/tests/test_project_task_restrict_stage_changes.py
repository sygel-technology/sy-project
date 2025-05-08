# Copyright 2025 Ángel García de la Chica Herrera <angel.garcia@sygel.es>
# License AGPL-3 - See https://www.gnu.org/licenses/agpl-3.0

from odoo.exceptions import ValidationError
from odoo.tests import tagged
from odoo.tests.common import users

from odoo.addons.project.tests.test_project_base import TestProjectCommon


@tagged("post_install", "-at_install")
class TestProjectTaskRestrictStageChanges(TestProjectCommon):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        res_group_all_stages = cls.env.ref(
            "project_task_restrict_stage_changes.res_group_all_stages"
        )
        user_group_project_user = cls.env.ref("project.group_project_user")
        user_group_project_manager = cls.env.ref("project.group_project_manager")
        users = cls.env["res.users"].with_context(**{"no_reset_password": True})
        cls.standard_user = users.create(
            {
                "name": "StandardUser",
                "login": "standard_user",
                "email": "StandardUser@example.com",
                "groups_id": [
                    (6, 0, [user_group_project_user.id, user_group_project_manager.id])
                ],
            }
        )
        cls.manager_user = users.create(
            {
                "name": "ManagerUser",
                "login": "manager_user",
                "email": "ManagerUser@example.com",
                "groups_id": [
                    (
                        6,
                        0,
                        [
                            user_group_project_user.id,
                            user_group_project_manager.id,
                            res_group_all_stages.id,
                        ],
                    )
                ],
            }
        )
        cls.task_stage_new = cls.env["project.task.type"].create(
            {
                "name": "New",
            }
        )
        cls.task_stage_close = cls.env["project.task.type"].create(
            {
                "name": "Close",
            }
        )
        cls.task_1.write({"stage_id": cls.task_stage_new.id})

    @users("standard_user")
    def test_move_task_to_stage_not_allowed(self):
        self.task_stage_close.write({"restrict_stage_assignment": True})
        with self.assertRaises(ValidationError):
            self.task_1.with_user(self.env.user).write(
                {"stage_id": self.task_stage_close.id}
            )

    @users("standard_user")
    def test_move_task_from_stage_not_allowed(self):
        self.task_stage_close.write({"restrict_stage_deallocation": True})
        self.task_1.with_user(self.env.user).write(
            {"stage_id": self.task_stage_close.id}
        )
        with self.assertRaises(ValidationError):
            self.task_1.with_user(self.env.user).write(
                {"stage_id": self.task_stage_new.id}
            )

    @users("manager_user")
    def test_move_task_user_allowed(self):
        self.task_stage_close.write(
            {"restrict_stage_assignment": True, "restrict_stage_deallocation": True}
        )
        self.task_1.with_user(self.env.user).write(
            {"stage_id": self.task_stage_close.id}
        )
        self.task_1.with_user(self.env.user).write({"stage_id": self.task_stage_new.id})
