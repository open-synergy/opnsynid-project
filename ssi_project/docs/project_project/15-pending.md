# Pending Project

> **Module:** `ssi_project`\
> **Model:** `project.project`\
> **Menu:** Project > Projects\
> **Actor:** user in group _Project Validator_\
> **State:** `open` → `pending`\
> **Requires:** `07-start`

## Pre-Condition

- **Record:** Status is **In Progress**.
- **Access:** User is in group _Project Validator_.

## Flow

1. Open the **Project > Projects** menu.
2. Open the record to put on hold.
3. Click the **Pending** button.
4. Click **OK** on the confirmation dialog.

## Post-Condition

- Status changes to **Pending**.
