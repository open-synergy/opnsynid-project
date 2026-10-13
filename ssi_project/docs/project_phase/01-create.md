# Create Project Phase

> **Module:** `ssi_project`\
> **Model:** `project_phase`\
> **Menu:** Project > Project > Phases\
> **Actor:** user in group _Project Phase User_\
> **State:** `—` → `draft`

## Pre-Condition

- **Data:** A project exists.
- **Data:** Optionally, a group phase of that project exists, if the phase is a child
  phase.
- **Access:** User is in group _Project Phase User_ (or _Project Phase Validator_).

## Flow

1. Open the **Project > Project > Phases** menu.
2. Click the **New** button. **(14.0: "Create")**
3. Fill in the required fields:
   - **Project** _(required)_: Select the project of the phase.
   - **Group/Single?** _(required)_: Select **Group of Phase** if the phase has child
     phases, or **Single Phase** if the phase has its own tasks and deliverables.
     Changing this field clears **Parent Phase**.
   - **Parent Phase**: Select the group phase that contains this phase. Only phases of
     the selected **Project** are offered. Changing the **Project** clears this field.
   - **Title** _(required)_: Enter the title of the phase.
   - **Date** _(required)_: Enter the start date of the phase. It defaults to today.
   - **Duration**: Select a duration to calculate **Date Due** from **Date**.
   - **Date Due** _(required)_: Enter the due date of the phase.
4. Click **Save**.

## Post-Condition

- A new record is created in **Draft** status.
- The document number is still **/**; it is generated when the phase is approved and
  starts.
