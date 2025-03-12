# Copyright 2025 Ángel García de la Chica Herrera <angel.garcia@sygel.es>
# License AGPL-3 - See https://www.gnu.org/licenses/agpl-3.0

from odoo.tests.common import Form

from odoo.addons.project.tests.test_project_base import TestProjectCommon


class TestProjectSubtaskDefaultDisplayProject(TestProjectCommon):
    def test_create_subtask(self):
        """It is necessary to remove the many2many widget to be able to
        create a subtask directly from the tree view and to check that
        the display_project field is correctly passed.
        """
        view = self.env["ir.ui.view"].create(
            {
                "name": "Inherited Test View",
                "type": "form",
                "model": "project.task",
                "inherit_id": self.env.ref("project.view_task_form2").id,
                "mode": "extension",
                "arch": """
                <xpath expr="//field[@name='child_ids']" position='attributes'>
                    <attribute name="widget">one2many</attribute>
                </xpath>
            """,
            }
        )
        self.task_1.project_id.allow_subtasks = True
        with Form(self.task_1, view) as f:
            with f.child_ids.new() as line:
                line.name = "subtask"
        f.save()
        self.assertEqual(self.task_1.project_id, line.project_id)
        self.assertEqual(self.task_1.project_id, line.display_project_id)
