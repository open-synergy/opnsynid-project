# Automatic Reopen of Project Deliverable

> **Module:** `ssi_project`\
> **Model:** `project_deliverable`\
> **Menu:** Project > Project > Deliverables\
> **Actor:** system (`base.automation` _project_deliverable_done_2_open_)\
> **State:** `done` → `open`\
> **Requires:** `16-auto-done`

## Pre-Condition

- **Record:** Status is **Done**.
- **Config:** The automated action `project_deliverable_done_2_open` is active.
- **Record:** **Completion Percentage** is 100%.

## Flow

This transition has no button. It is triggered by the system:

- While the deliverable is **Done**, users add work to it, for example a task that is
  not done.
- When **Completion Percentage** changes away from 100%, the automated action
  `project_deliverable_done_2_open` runs by itself.
- To check the result, open the **Project > Project > Deliverables** menu and open the
  record.

## Post-Condition

- Status returns to **On Progress** without any user clicking a button.
