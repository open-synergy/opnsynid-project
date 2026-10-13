# Finish Project Milestone

> **Module:** `ssi_project`\
> **Model:** `project_milestone`\
> **Menu:** Project > Project > Milestones\
> **Actor:** user in group _Project Milestone User_\
> **State:** `open` → `done`\
> **Requires:** `05-approve`

## Pre-Condition

- **Record:** Status is **On Progress**.
- **Config:** An active `policy.template` for `project_milestone` grants `done_ok` for
  state **On Progress** to the actor's group.

- **Access:** User is in group _Project Milestone User_ (or _Project Milestone
  Validator_).

## Flow

1. Open the **Project > Project > Milestones** menu.
2. Open the record to finish.
3. Click the **Done** button.
4. Click **OK** on the confirmation dialog.

## Post-Condition

- Status changes to **Done**.
- If **Reporting Point** is checked, the milestone no longer counts toward the **Next
  Reporting Date** of the project.
