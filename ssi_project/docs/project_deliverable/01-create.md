# Create Project Deliverable

> **Module:** `ssi_project`\
> **Model:** `project_deliverable`\
> **Menu:** Project > Project > Deliverables\
> **Actor:** user in group _Project Deliverable User_\
> **State:** `—` → `draft`

## Pre-Condition

- **Data:** A project exists.
- **Data:** A deliverable type category and a deliverable type of that category exist.
- **Data:** Optionally, a phase of that project that is **On Progress** exists.
- **Access:** User is in group _Project Deliverable User_ (or _Project Deliverable
  Validator_).

## Flow

1. Open the **Project > Project > Deliverables** menu.
2. Click the **New** button. **(14.0: "Create")**
3. Fill in the required fields:
   - **Project** _(required)_: Select the project of the deliverable.
   - **Phase**: Select the phase that holds this deliverable. Only phases of the
     selected **Project** that are **On Progress** are offered. Changing the **Project**
     clears this field.
   - **Group/Single?** _(required)_: Select **Group of Deliverable** if the deliverable
     has child deliverables, or **Single Deliverable** if it has its own tasks. Changing
     this field clears **Parent Deliverable**.
   - **Category** _(required)_: Select the deliverable type category. Changing it clears
     **Type**.
   - **Type** _(required)_: Select the deliverable type. Only types of the selected
     **Category** are offered.
   - **Parent Deliverable**: Select the group deliverable that contains this one. Only
     deliverables of the selected **Project** are offered.
   - **Title** _(required)_: Enter the title of the deliverable.
   - **Date** _(required)_: Enter the start date of the deliverable. It defaults to
     today.
   - **Duration**: Select a duration to calculate **Date Due** from **Date**.
   - **Date Due** _(required)_: Enter the due date of the deliverable.
4. Click **Save**.

## Post-Condition

- A new record is created in **Draft** status.
- The document number is still **/**; it is generated when the deliverable is approved
  and starts.
