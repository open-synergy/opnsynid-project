# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase

from odoo.tests import tagged


@tagged("post_install", "-at_install")
class TestTaskDependency(YamlTransactionCase):
    """Unit tests for the ``task.dependency`` model."""

    def test_task_dependency(self):
        """Run the task dependency YAML scenarios.

        Covers the four dependency types, the two negative constraints
        and the cascade delete of the successor task.
        """
        self.run_yaml_scenario("test_data_task_dependency.yaml")
