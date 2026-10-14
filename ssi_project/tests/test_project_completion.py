# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase

from odoo.tests import tagged


@tagged("post_install", "-at_install")
class TestProjectCompletion(YamlTransactionCase):
    """Unit tests for task and child completion of phase and deliverable."""

    def test_project_completion(self):
        """Run the task and child completion YAML scenarios.

        Covers counters and percentages of task and child on both
        ``project_phase`` and ``project_deliverable``, including the
        empty case and the exclusion of draft children.
        """
        self.run_yaml_scenario("test_data_project_completion.yaml")
