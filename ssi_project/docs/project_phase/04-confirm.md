# Confirm Project Phase

> **Module:** `ssi_project`\
> **Model:** `project_phase`\
> **Menu:** Project > Project > Phases\
> **Actor:** user in group _Project Phase User_\
> **State:** `draft` → `confirm`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** Status is **Draft**.
- **Config:** An active `policy.template` for `project_phase` grants `confirm_ok` for
  state **Draft** to the actor's group.

- **Config:** An active `approval.template` for `project_phase` matches this record and
  has at least one approver level (the standard template approves with group _Project
  Phase Validator_).
- **Config:** An active `sequence.template` for `project_phase` exists.
- **Access:** User is in group _Project Phase User_ (or _Project Phase Validator_).

## Flow

1. Open the **Project > Project > Phases** menu.
2. Open the record to confirm.
3. Click the **Confirm** button.
4. Click **OK** on the confirmation dialog.

## Post-Condition

- Status changes to **Waiting for Approval**.
- Approval records are created for each approver level defined by the approval template.
