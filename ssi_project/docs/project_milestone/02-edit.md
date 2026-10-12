# Edit Project Milestone

> **Module:** `ssi_project`\
> **Model:** `project_milestone`\
> **Menu:** Project > Configuration > Project > Milestones\
> **Actor:** user in group _Project Milestone_ (configurator)\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** Status is **Draft**.
- **Access:** User is in group _Project Milestone_.

## Flow

1. Open the **Project > Configuration > Project > Milestones** menu.
2. Find and open the record to edit.
3. Click the **Edit** button.
4. Change the required fields:
   - **Reporting Point**: Check or uncheck the box.
   - **Reporting Date** _(required if **Reporting Point** is checked)_: Enter the
     reporting date.
5. Click **Save**.

## Post-Condition

- The record is updated with the new values.
