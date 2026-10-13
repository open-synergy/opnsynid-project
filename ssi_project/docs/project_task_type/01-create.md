# Create Task Stage

> **Module:** `ssi_project`\
> **Model:** `project.task.type`\
> **Menu:** Project > Configuration > Project > Stages\
> **Actor:** user in group _Project Stage_

## Pre-Condition

- **Access:** User is in group _Project Stage_.

## Flow

1. Open the **Project > Configuration > Project > Stages** menu.
2. Click the **New** button. **(14.0: "Create")**
3. Fill in the required fields:
   - **Stage Name** _(required)_: Enter the name of the stage.
   - **State**: Select the task status that is set when a task moves to this stage.
4. Optionally, check **Is Default?** if new tasks start in this stage, or **Folded in
   Kanban** to fold the stage in the kanban view.
5. Click **Save**.

## Post-Condition

- A new stage is created and is listed in **Stages**.
