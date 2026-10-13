# Delete Project Milestone

> **Module:** `ssi_project`\
> **Model:** `project_milestone`\
> **Menu:** Project > Project > Milestones\
> **Actor:** user in group _Project Milestone User_\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** Status is **Draft**.
- **Record:** Document number is still **/** (not yet generated).
- **Access:** User is in group _Project Milestone User_ (or _Project Milestone
  Validator_).

## Flow

1. Open the **Project > Project > Milestones** menu.
2. Find and open the record to delete.
3. Click the **Action** menu, then click **Delete**.
4. Click **OK** on the confirmation dialog.
5. Click **Project Milestones** in the breadcrumb to return to the list.

## Post-Condition

- The record is removed from the Project Milestones list.
