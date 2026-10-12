# Cancel Project

> **Module:** `ssi_project`\
> **Model:** `project.project`\
> **Menu:** Project > Projects\
> **Actor:** user in group _Project Validator_\
> **State:** `draft` → `cancel`\
> **Extends:** project — model `project.project`, aksi `10-cancel`

## Pre-Condition

- **Record:** Status is **New**.
- **Access:** User is in group _Project Validator_ (or _Project User_).

## Flow

1. Open the **Project > Projects** menu.
2. Open the record to cancel.
3. Click the **Cancel** button.
4. Click **OK** on the confirmation dialog.

## Post-Condition

- Status changes to **Cancel**.
