# Confirm Project Deliverable

> **Module:** `ssi_project`\
> **Model:** `project_deliverable`\
> **Menu:** Project > Project > Deliverables\
> **Actor:** user in group _Project Deliverable User_\
> **State:** `draft` → `confirm`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** Status is **Draft**.
- **Config:** An active `policy.template` for `project_deliverable` grants `confirm_ok`
  for state **Draft** to the actor's group.

- **Config:** An active `approval.template` for `project_deliverable` matches this
  record and has at least one approver level (the standard template approves with group
  _Project Deliverable Validator_).
- **Config:** An active `sequence.template` for `project_deliverable` exists.
- **Access:** User is in group _Project Deliverable User_ (or _Project Deliverable
  Validator_).

## Flow

1. Open the **Project > Project > Deliverables** menu.
2. Open the record to confirm.
3. Click the **Confirm** button.
4. Click **OK** on the confirmation dialog.

## Post-Condition

- Status changes to **Waiting for Approval**.
- Approval records are created for each approver level defined by the approval template.
