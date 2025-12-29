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
        self.task_1.action_block()
        with Form(self.task_1) as form:
            form.task_blocked_reason = "Test"
        form = form.save()
        self.assertEqual("Test", self.task_1.task_blocked_reason)

    def test_block_buttons(self):
        self.task_1.action_block()
        self.assertTrue(self.task_1.blocked)
        self.assertEqual("04_waiting_normal", self.task_1.state)

        self.task_1.action_unblock()
        self.assertFalse(self.task_1.blocked)
        self.assertEqual("01_in_progress", self.task_1.state)

    def test_block_buttons_w_children(self):
        children_task = self.env["project.task"].create(
            {
                "name": "Test Task Name Match",
                "user_ids": self.user_projectuser,
                "project_id": self.project_pigs.id,
                "parent_id": self.task_1.id,
            }
        )

        self.task_1.action_block()
        self.assertTrue(children_task.blocked)
        self.assertEqual("04_waiting_normal", children_task.state)

        with Form(self.task_1) as form:
            form.task_blocked_reason = "Test"
        form = form.save()
        self.assertEqual("Test", children_task.task_blocked_reason)

        self.task_1.action_unblock()
        self.assertFalse(children_task.blocked)
        self.assertEqual("01_in_progress", children_task.state)
