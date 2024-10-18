# Copyright 2024 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import datetime

from odoo.tests.common import Form, TransactionCase


class TestProjectTaskDescriptionTemplateSection(TransactionCase):
    def setUp(cls):
        super().setUp()
        cls.task_id = cls.env["project.task"].create(
            {"name": "Test task", "description": "Task Description"}
        )
        cls.template_id = cls.env["project.task.description.template"].create(
            {
                "name": "Test Template 1",
                "description": "Template Description",
            }
        )

    def test_base(self):
        with Form(self.task_id) as task:
            task.description_template_id = self.template_id
        self.assertIn(self.template_id.description, self.task_id.description)

    def test_down(self):
        self.template_id.update(
            {
                "template_order": "Down",
            }
        )
        old_task_description = self.task_id.description

        with Form(self.task_id) as task:
            task.description_template_id = self.template_id

        task_desc_index = self.task_id.description.index(old_task_description)
        template_index = self.task_id.description.index(self.template_id.description)
        self.assertTrue(task_desc_index < template_index)

    def test_up(self):
        self.template_id.write(
            {
                "template_order": "Up",
            }
        )
        old_task_description = self.task_id.description

        with Form(self.task_id) as task:
            task.description_template_id = self.template_id

        task_desc_index = self.task_id.description.index(old_task_description)
        template_index = self.task_id.description.index(self.template_id.description)
        self.assertTrue(task_desc_index > template_index)

    def test_delimiter(self):
        self.template_id.write(
            {
                "section": True,
                "section_name": "Test Section",
                "section_with_date": True,
            }
        )

        with Form(self.task_id) as task:
            task.description_template_id = self.template_id

        self.assertIn(self.template_id.description, self.task_id.description)
        self.assertIn(
            self.template_id.section_delimiter_header, self.task_id.description
        )
        self.assertIn(
            self.template_id.section_delimiter_footer, self.task_id.description
        )

        self.assertIn(
            self.template_id.section_name, self.template_id.section_delimiter_header
        )
        self.assertIn(
            str(datetime.date.today().year), self.template_id.section_delimiter_header
        )
        self.assertIn(
            str(datetime.date.today().month), self.template_id.section_delimiter_header
        )
        self.assertIn(
            str(datetime.date.today().day), self.template_id.section_delimiter_header
        )
