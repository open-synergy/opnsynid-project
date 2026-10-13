# Change Task Stage

> **Module:** `ssi_project`\
> **Model:** `project.task`\
> **Menu:** Project > Tasks\
> **Actor:** user in group _Task User_ (or _Task Validator_)\
> **State:** `draft` | `open` | `done` | `pending` | `cancelled` → the state of the
> target stage\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** The task belongs to a project, so the stage bar is shown.
- **Data:** At least two stages are available for the project.
- **Data:** Every predecessor that blocks the target stage is already handled. Moving to
  a stage that starts the task requires the start-to-start and finish-to-start
  predecessors to be started, finished, or cancelled; moving to a stage that finishes
  the task requires the start-to-finish and finish-to-finish predecessors to be started,
  finished, or cancelled.
- **Access:** User is in group _Task User_ (or _Task Validator_).

## Flow

1. Open the **Project > Tasks** menu.
2. Find and open the record.
3. In the stage bar at the top of the form, click the stage to move the task to.

## Post-Condition

- The clicked stage is highlighted in the stage bar.
- The status of the task follows the status that is set on the new stage.
