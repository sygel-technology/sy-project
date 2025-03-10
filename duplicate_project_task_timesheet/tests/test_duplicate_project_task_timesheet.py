# Copyright 2025 Ángel García de la Chica Herrera <angel.garcia@sygel.es>
# License AGPL-3 - See https://www.gnu.org/licenses/agpl-3.0

from odoo.tests import tagged

from odoo.addons.project.tests.test_project_base import TestProjectCommon


@tagged("post_install", "-at_install")
class TestDuplicateTaskTimesheet(TestProjectCommon):
    @classmethod
    def setUpClass(cls):
        super(TestDuplicateTaskTimesheet, cls).setUpClass()
        cls.employee = cls.env["hr.employee"].create(
            {
                "name": "Employee Test",
            }
        )
        cls.timesheet = cls.env["account.analytic.line"].create(
            {
                "name": "Test Timesheet",
                "unit_amount": 2,
                "project_id": cls.project_pigs.id,
                "task_id": cls.task_1.id,
                "employee_id": cls.employee.id,
            }
        )

    def test_duplicate_task_timesheet(self):
        self.assertEqual(1, len(self.task_1.timesheet_ids))
        self.timesheet.copy()
        self.assertEqual(2, len(self.task_1.timesheet_ids))
        self.assertEqual(
            2,
            len(
                self.task_1.timesheet_ids.filtered(lambda x: x.name == "Test Timesheet")
            ),
        )
        self.assertEqual(4, self.task_1.effective_hours)
