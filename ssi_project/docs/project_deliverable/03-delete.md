# Delete Project Deliverable

> **Module:** `ssi_project`\
> **Model:** `project_deliverable`\
> **Menu:** Project > Project > Deliverables\
> **Actor:** user in group _Project Deliverable User_\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** Status is **Draft**.
- **Record:** Document number is still **/** (not yet generated).
- **Access:** User is in group _Project Deliverable User_ (or _Project Deliverable
  Validator_).

## Flow

1. Open the **Project > Project > Deliverables** menu.
2. Find and open the record to delete.
3. Click the **Action** menu, then click **Delete**.
4. Click **OK** on the confirmation dialog.
5. Click **Project Deliverables** in the breadcrumb to return to the list.

## Post-Condition

- The record is removed from the Project Deliverables list.
