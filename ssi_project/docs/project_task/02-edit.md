# Edit Task

> **Module:** `ssi_project`\
> **Model:** `project.task`\
> **Menu:** Project > Tasks\
> **Actor:** user in group _Task User_ (or _Task Validator_)\
> **Requires:** `01-create`\
> **Inline Actions:** `action_assign_to_me` (Assign to Me)

## Pre-Condition

- **Record:** The task is not archived.
- **Access:** User is in group _Task User_ (or _Task Validator_).

## Flow

1. Open the **Project > Tasks** menu.
2. Find and open the record to edit.
3. Click the **Edit** button.
4. Change the required fields. If the task has no assignee, click **Assign to Me** to
   assign it to yourself.
5. Click **Save**.

## Post-Condition

- The record is updated with the new values.
