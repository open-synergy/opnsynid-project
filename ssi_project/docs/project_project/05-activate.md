# Activate Project

> **Module:** `ssi_project`\
> **Model:** `project.project`\
> **Menu:** Project > Projects\
> **Actor:** user in group _Project User_ (or _Project Validator_)\
> **Active:** `false` → `true`\
> **Requires:** `04-deactivate`

## Pre-Condition

- **Record:** The record is currently archived.
- **Access:** User is in group _Project User_ (or _Project Validator_).

## Flow

1. Open the **Project > Projects** menu.
2. Enable the **Archived** filter in the search bar.
3. Find and open the record to reactivate.
4. Click the **Action** menu, then click **Unarchive**.

## Post-Condition

- The project is restored and appears again in the default Projects list.
