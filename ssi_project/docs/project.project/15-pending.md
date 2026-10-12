# Pending Project

> **Module:** `ssi_project`\
> **Model:** `project.project`\
> **Menu:** Project > Projects\
> **Actor:** user in group _Project Validator_\
> **State:** `open` → `pending`\
> **Extends:** project — model `project.project`, aksi `15-pending`

## Pre-Condition

- **Record:** Status is **In Progress**.
- **Access:** User is in group _Project Validator_ (or _Project User_).

## Flow

1. Open the **Project > Projects** menu.
2. Open the record to put on hold.
3. Click the **Pending** button.
4. Click **OK** on the confirmation dialog.

## Post-Condition

- Status changes to **Pending**.
