# Deactivate Task

> **Module:** `ssi_project`\
> **Model:** `project.task`\
> **Menu:** Project > Tasks\
> **Actor:** user in group _Task User_ (or _Task Validator_)\
> **Active:** `true` → `false`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** The record is currently active.
- **Access:** User is in group _Task User_ (or _Task Validator_).

## Flow

1. Open the **Project > Tasks** menu.
2. Find and open the record to deactivate.
3. Click the **Action** menu, then click **Archive**.
4. Click **OK** on the confirmation dialog.

## Post-Condition

- The task is archived and no longer appears in the default Tasks list.
