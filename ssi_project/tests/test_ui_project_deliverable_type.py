# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# HttpSavepointCase, not HttpCase: HttpCase has no cls.env in 14.0.
from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiProjectDeliverableType(HttpSavepointCase):
    """Tour tests for the ``project_deliverable_type`` work instructions."""

    @classmethod
    def setUpClass(cls):
        """Create the category offered by the create tour."""
        super().setUpClass()
        cls.category = cls.env["project_deliverable_type_category"].create(
            {"name": "TOURDT-CATEGORY", "code": "TOURDTCAT"}
        )

    def test_create(self):
        """Run the create tour for ``project_deliverable_type``.

        IK: docs/project_deliverable_type/01-create.md
        """
        self.start_tour(
            "/web", "ssi_project_project_deliverable_type_create", login="admin"
        )
