# Create Task

> **Module:** `ssi_project`\
> **Model:** `project.task`\
> **Menu:** Project > Tasks\
> **Actor:** user in group _Task User_ (or _Task Validator_)\
> **State:** `—` → `draft`\
> **Inline Actions:** `action_assign_to_me` (Assign to Me)

## Pre-Condition

- **Data:** A project exists.
- **Data:** Optionally, a deliverable, a phase, and predecessor tasks of that project
  exist.
- **Access:** User is in group _Task User_ (or _Task Validator_).

## Flow

1. Open the **Project > Tasks** menu.
2. Click the **New** button. **(14.0: "Create")**
3. Fill in the required fields:
   - **Title** _(required)_: Enter the title of the task.
   - **Project**: Select the project of the task.
4. If **Assigned to** was cleared, click **Assign to Me** to set yourself as the
   assignee. The field defaults to you, and the button is hidden while the task is
   assigned.
5. Click **Save**.

## Post-Condition

- A new record is created in the default stage of the project. The stage is highlighted
  in the stage bar.

## Related Views

Optional data that can be entered before saving:

- **Deliverable** and **Phase** fields: select the deliverable produced by the task and
  the phase of the task. Only open single deliverables and phases of the selected
  **Project** are offered. Optional.
- **Specification** tab: describe the specification of the task. Optional.
- **Dependency** tab > **Predecessors**: add a row per predecessor with **Project**,
  **Predecessor Task**, and **Dependency Type**. Optional.
- **Instruction** tab: add a row per instruction with **Instruction Name** and
  **Instruction URL**. Optional.
