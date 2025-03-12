# Copyright 2025 Ángel García de la Chica Herrera <angel.garcia@sygel.es>
# License AGPL-3 - See https://www.gnu.org/licenses/agpl-3.0

from odoo import fields
from odoo.tests import tagged

from odoo.addons.project.tests.test_project_base import TestProjectCommon


@tagged("post_install", "-at_install")
class TestTaskRequirementsMgmt(TestProjectCommon):
    @classmethod
    def setUpClass(cls):
        super(TestTaskRequirementsMgmt, cls).setUpClass()
        cls.requirement_test_1 = cls.env["task.requirement"].create(
            {
                "description": "Test Requirement",
                "project_task_id": cls.task_1.id,
            }
        )

    def test_add_new_requirement(self):
        requirement_test_2 = self.env["task.requirement"].create(
            {
                "description": "Test Requirement 2",
                "project_task_id": self.task_1.id,
            }
        )
        self.assertEqual(
            fields.Date.context_today(self.task_1),
            requirement_test_2.specification_date,
        )
        self.assertEqual(2, len(self.task_1.task_requirement_ids))

    def test_completed_requirement(self):
        self.requirement_test_1.completed = True
        self.assertEqual(
            fields.Date.context_today(self.task_1),
            self.requirement_test_1.completed_date,
        )

    def test_tested_requirement(self):
        self.requirement_test_1.tested = True
        self.assertEqual(
            fields.Date.context_today(self.task_1), self.requirement_test_1.tested_date
        )
