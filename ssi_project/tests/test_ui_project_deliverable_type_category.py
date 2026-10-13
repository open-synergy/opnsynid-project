# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# HttpSavepointCase, not HttpCase: HttpCase has no cls.env in 14.0.
from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiProjectDeliverableTypeCategory(HttpSavepointCase):
    """Tour tests for the ``project_deliverable_type_category`` work instructions."""

    def test_create(self):
        """Run the create tour for ``project_deliverable_type_category``.

        IK: docs/project_deliverable_type_category/01-create.md
        """
        self.start_tour(
            "/web",
            "ssi_project_project_deliverable_type_category_create",
            login="admin",
        )
