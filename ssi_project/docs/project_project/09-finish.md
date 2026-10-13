# Done Project

> **Module:** `ssi_project`\
> **Model:** `project.project`\
> **Menu:** Project > Projects\
> **Actor:** user in group _Project Validator_\
> **State:** `open` | `pending` → `done`\
> **Requires:** `07-start`

## Pre-Condition

- **Record:** Status is **In Progress** or **Pending**.
- **Access:** User is in group _Project Validator_.

## Flow

1. Open the **Project > Projects** menu.
2. Open the record to finish.
3. Click the **Done** button.
4. Click **OK** on the confirmation dialog.

## Post-Condition

- Status changes to **Done**.
