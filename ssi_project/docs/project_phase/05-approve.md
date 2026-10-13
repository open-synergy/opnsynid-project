# Approve Project Phase

> **Module:** `ssi_project`\
> **Model:** `project_phase`\
> **Menu:** Project > Project > Phases\
> **Actor:** approver on the pending approval level (members of group _Project Phase Validator_
> with the standard template)\
> **State:** `confirm` → `open`\
> **Requires:** `04-confirm`

## Pre-Condition

- **Record:** Status is **Waiting for Approval**.
- **Config:** An active `policy.template` for `project_phase` grants `approve_ok` for
  state **Waiting for Approval** to the actor's group.

- **Access:** User is registered as an approver on the approval level that is currently
  pending.

## Flow

1. Open the **Project > Project > Phases** menu.
2. Open the record to approve.
3. Click the **Approve** button.
4. Click **OK** on the confirmation dialog.

## Post-Condition

- If all approval levels are fulfilled, status changes to **On Progress**.
- If there are still pending approval levels, status remains **Waiting for Approval**
  and the next level becomes pending.
