# Deactivate Task Stage

> **Module:** `ssi_project`\
> **Model:** `project.task.type`\
> **Menu:** Project > Configuration > Project > Stages\
> **Actor:** user in group _Project Stage_\
> **Active:** `true` → `false`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** The record is currently active.
- **Access:** User is in group _Project Stage_.

## Flow

1. Open the **Project > Configuration > Project > Stages** menu.
2. Find and open the record to deactivate.
3. Click the **Action** menu, then click **Archive**.
4. Click **OK** on the confirmation dialog.

## Post-Condition

- The stage is archived and no longer appears in the default Stages list.
- Existing tasks keep the stage and can still be viewed.
