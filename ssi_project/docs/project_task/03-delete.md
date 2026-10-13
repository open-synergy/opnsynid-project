# Delete Task

> **Module:** `ssi_project`\
> **Model:** `project.task`\
> **Menu:** Project > Tasks\
> **Actor:** user in group _Task User_ (or _Task Validator_)\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** The task is not archived.
- **Access:** User is in group _Task User_ (or _Task Validator_).

## Flow

1. Open the **Project > Tasks** menu.
2. Find and open the record to delete.
3. Click the **Action** menu, then click **Delete**.
4. Click **OK** on the confirmation dialog.

## Post-Condition

- The record is removed from the Tasks list.
