# Automatic Done of Project Phase

> **Module:** `ssi_project`\
> **Model:** `project_phase`\
> **Menu:** Project > Project > Phases\
> **Actor:** system (`base.automation` _project_phase_open_2_done_)\
> **State:** `open` → `done`\
> **Requires:** `05-approve`

## Pre-Condition

- **Record:** Status is **On Progress**.
- **Config:** The automated action `project_phase_open_2_done` is active.
- **Record:** **Completion Percentage** is below 100%.

## Flow

This transition has no button. It is triggered by the system:

- While the phase is **On Progress**, users complete the tasks and deliverables and
  child records of the phase.
- When **Completion Percentage** changes to 100%, the automated action
  `project_phase_open_2_done` runs by itself.
- To check the result, open the **Project > Project > Phases** menu and open the record.

## Post-Condition

- Status changes to **Done** without any user clicking the **Done** button.
