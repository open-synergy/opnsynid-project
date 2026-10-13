# Create Project Milestone

> **Module:** `ssi_project`\
> **Model:** `project_milestone`\
> **Menu:** Project > Project > Milestones\
> **Actor:** user in group _Project Milestone User_\
> **State:** `—` → `draft`

## Pre-Condition

- **Data:** A project exists.
- **Data:** Optionally, a phase of that project exists, if the milestone closes a phase.
- **Access:** User is in group _Project Milestone User_ (or _Project Milestone
  Validator_).

## Flow

1. Open the **Project > Project > Milestones** menu.
2. Click the **New** button. **(14.0: "Create")**
3. Fill in the required fields:
   - **Project** _(required)_: Select the project of the milestone.
   - **Phase**: Select the phase that is closed by this milestone. Only phases of the
     selected **Project** are offered. Changing the **Project** clears this field.
   - **Reporting Point**: Check this box if the project is reported at this milestone.
   - **Reporting Date** _(required if **Reporting Point** is checked)_: Enter the date
     on which the project is reported for this milestone.
4. Click **Save**.

## Post-Condition

- A new record is created in **Draft** status.
- If **Reporting Point** is checked, the milestone counts toward the **Next Reporting
  Date** of the project until it is done, cancelled, or terminated.
