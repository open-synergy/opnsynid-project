# Restart Project

> **Module:** `ssi_project`\
> **Model:** `project.project`\
> **Menu:** Project > Projects\
> **Actor:** user in group _Project Validator_\
> **State:** `cancel` → `draft`\
> **Extends:** project — model `project.project`, aksi `12-restart`

## Pre-Condition

- **Record:** Status is **Cancel**.
- **Access:** User is in group _Project Validator_ (or _Project User_).

## Flow

1. Open the **Project > Projects** menu.
2. Open the record to restart.
3. Click the **Restart** button.
4. Click **OK** on the confirmation dialog.

## Post-Condition

- Status changes to **New**.
