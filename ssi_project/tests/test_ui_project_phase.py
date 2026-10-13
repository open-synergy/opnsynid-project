# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# HttpSavepointCase, not HttpCase: HttpCase has no cls.env in 14.0.
from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiProjectPhase(HttpSavepointCase):
    """Tour tests for the ``project_phase`` work instructions."""

    @classmethod
    def setUpClass(cls):
        """Create the projects and phases used by the tours."""
        super().setUpClass()
        # user_id is explicit: cls.env runs as SUPERUSER and the record rules
        # would otherwise hide these fixtures from the tour's admin session.
        cls.admin = cls.env.ref("base.user_admin")
        Project = cls.env["project.project"]
        Phase = cls.env["project_phase"]
        cls.project_new = Project.create(
            {"name": "TOURPH-NEWPROJECT", "user_id": cls.admin.id}
        )
        cls.project_flow = Project.create(
            {"name": "TOURPH-FLOWPROJECT", "user_id": cls.admin.id}
        )

        def _phase(title):
            """Create a draft single phase owned by the tour user.

            :param title: unique phase title
            :return: the created phase
            """
            return Phase.create(
                {
                    "title": title,
                    "ttype": "single",
                    "project_id": cls.project_flow.id,
                    "date": "2026-01-01",
                    "date_due": "2026-12-31",
                    "user_id": cls.admin.id,
                }
            )

        # Pre-Conditions for 04-confirm / 05-approve / 09-finish / 10-cancel.
        # The approval chain runs through action methods as the admin user
        # with a cache flush in between (T-04), never through write().
        cls.phase_confirm = _phase("TOURPH-CONFIRM")
        cls.phase_cancel = _phase("TOURPH-CANCEL")
        cls.phase_approve = _phase("TOURPH-APPROVE")
        cls.phase_approve.with_user(cls.admin).action_confirm()
        cls.phase_approve.invalidate_cache()
        cls.phase_finish = _phase("TOURPH-FINISH")
        cls.phase_finish.with_user(cls.admin).action_confirm()
        cls.phase_finish.invalidate_cache()
        cls.phase_finish.with_user(cls.admin).action_approve_approval()
        cls.phase_finish.invalidate_cache()
        cls.env["base.cancel_reason"].create(
            {
                "name": "Tour Phase Cancel Reason",
                "code": "TOURPHCR",
                # Only reasons in ir.model.all_cancel_reason_ids reach the
                # wizard radio; global_use=True puts this one there.
                "global_use": True,
            }
        )

    def test_create(self):
        """Run the create tour for ``project_phase``.

        IK: docs/project_phase/01-create.md
        """
        self.start_tour("/web", "ssi_project_project_phase_create", login="admin")

    def test_confirm(self):
        """Run the confirm tour for ``project_phase``.

        IK: docs/project_phase/04-confirm.md
        """
        self.start_tour("/web", "ssi_project_project_phase_confirm", login="admin")

    def test_approve(self):
        """Run the approve tour for ``project_phase``.

        IK: docs/project_phase/05-approve.md
        """
        self.start_tour("/web", "ssi_project_project_phase_approve", login="admin")

    def test_finish(self):
        """Run the finish tour for ``project_phase``.

        IK: docs/project_phase/09-finish.md
        """
        self.start_tour("/web", "ssi_project_project_phase_finish", login="admin")

    def test_cancel(self):
        """Run the cancel tour for ``project_phase``.

        IK: docs/project_phase/10-cancel.md
        """
        self.start_tour("/web", "ssi_project_project_phase_cancel", login="admin")
