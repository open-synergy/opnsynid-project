# Activate Task Stage

> **Module:** `ssi_project`\
> **Model:** `project.task.type`\
> **Menu:** Project > Configuration > Project > Stages\
> **Actor:** user in group _Project Stage_\
> **Active:** `false` → `true`\
> **Requires:** `04-deactivate`

## Pre-Condition

- **Record:** The record is currently archived.
- **Access:** User is in group _Project Stage_.

## Flow

1. Open the **Project > Configuration > Project > Stages** menu.
2. Enable the **Archived** filter in the search bar.
3. Find and open the record to reactivate.
4. Click the **Action** menu, then click **Unarchive**.

## Post-Condition

- The stage is restored and appears again in the default Stages list.
