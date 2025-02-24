# Copyright 2025 Ángel García de la Chica Herrera <angel.garcia@sygel.es>
# License AGPL-3 - See https://www.gnu.org/licenses/agpl-3.0

from odoo.tests import Form, tagged

from odoo.addons.project.tests.test_project_base import TestProjectCommon


@tagged("post_install", "-at_install")
class TestProjectTaskBlockReason(TestProjectCommon):
    def test_add_task_blocked_reason_task_not_blocked(self):
        self.assertEqual(False, self.task_1.task_blocked_reason)
        with self.assertRaises(AssertionError):
            with Form(self.task_1) as form:
                form.task_blocked_reason = "Test"
            form = form.save()
        self.assertEqual(False, self.task_1.task_blocked_reason)

    def test_add_task_blocked_reason_task_blocked(self):
        self.assertEqual(False, self.task_1.task_blocked_reason)
        self.task_1.kanban_state = "blocked"
        with Form(self.task_1) as form:
            form.task_blocked_reason = "Test"
        form = form.save()
        self.assertEqual("Test", self.task_1.task_blocked_reason)
