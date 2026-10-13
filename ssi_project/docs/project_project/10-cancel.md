# Cancel Project

> **Module:** `ssi_project`\
> **Model:** `project.project`\
> **Menu:** Project > Projects\
> **Actor:** user in group _Project Validator_\
> **State:** `draft` | `open` | `pending` | `done` → `cancel`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** Status is **New**, **In Progress**, **Pending**, or **Done**.
- **Access:** User is in group _Project Validator_.

## Flow

1. Open the **Project > Projects** menu.
2. Open the record to cancel.
3. Click the **Cancel** button.
4. Click **OK** on the confirmation dialog.

## Post-Condition

- Status changes to **Cancel**.
