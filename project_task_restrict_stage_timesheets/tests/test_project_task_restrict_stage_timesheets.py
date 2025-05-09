# Copyright 2025 Ángel García de la Chica Herrera <angel.garcia@sygel.es>
# License AGPL-3 - See https://www.gnu.org/licenses/agpl-3.0

from odoo.exceptions import ValidationError
from odoo.tests import tagged
from odoo.tests.common import users

from odoo.addons.project.tests.test_project_base import TestProjectCommon


@tagged("post_install", "-at_install")
class TestProjectTaskRestrictStageTimesheets(TestProjectCommon):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        res_group_all_stages = cls.env.ref(
            "project_task_restrict_stage_timesheets.res_group_all_stages"
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
        cls.employee_standard = cls.env["hr.employee"].create(
            {
                "name": "Employee Standard",
                "user_id": cls.standard_user.id,
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
        cls.employee_manager = cls.env["hr.employee"].create(
            {
                "name": "Employee Manager",
                "user_id": cls.manager_user.id,
            }
        )
        cls.task_stage_close = cls.env["project.task.type"].create(
            {"name": "Close", "restrict_stage_timesheets": True}
        )
        cls.task_1.write({"stage_id": cls.task_stage_close.id})

        cls.timesheet_test = cls.env["account.analytic.line"].create(
            [
                {
                    "name": "Test 1",
                    "unit_amount": 2,
                    "task_id": cls.task_1.id,
                    "employee_id": cls.employee_standard.id,
                }
            ]
        )

    @users("standard_user")
    def test_create_timesheet_in_stage_not_allowed(self):
        with self.assertRaises(ValidationError):
            self.env["account.analytic.line"].create(
                [
                    {
                        "name": "Test 2",
                        "unit_amount": 4,
                        "project_id": self.project_pigs.id,
                        "task_id": self.task_1.id,
                    }
                ]
            )

    @users("standard_user")
    def test_edit_timesheet_in_stage_not_allowed(self):
        with self.assertRaises(ValidationError):
            self.timesheet_test.with_user(self.env.user).write({"unit_amount": 10})

    @users("standard_user")
    def test_remove_timesheet_in_stage_not_allowed(self):
        with self.assertRaises(ValidationError):
            self.timesheet_test.with_user(self.env.user).unlink()

    @users("manager_user")
    def test_create_edit_remove_timesheet_user_allowed(self):
        timesheet_id = self.env["account.analytic.line"].create(
            [
                {
                    "name": "Test 2",
                    "unit_amount": 4,
                    "project_id": self.project_pigs.id,
                    "task_id": self.task_1.id,
                }
            ]
        )
        timesheet_id.with_user(self.env.user).write({"unit_amount": 10})
        timesheet_id.with_user(self.env.user).unlink()
