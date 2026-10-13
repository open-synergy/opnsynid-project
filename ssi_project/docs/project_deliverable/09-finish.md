# Finish Project Deliverable

> **Module:** `ssi_project`\
> **Model:** `project_deliverable`\
> **Menu:** Project > Project > Deliverables\
> **Actor:** user in group _Project Deliverable User_\
> **State:** `open` → `done`\
> **Requires:** `05-approve`

## Pre-Condition

- **Record:** Status is **On Progress**.
- **Record:** The deliverable is a **Group of Deliverable** without child deliverables,
  or a **Single Deliverable** without tasks.
- **Config:** An active `policy.template` for `project_deliverable` grants `done_ok` for
  state **On Progress** to the actor's group, with the additional condition above.

- **Access:** User is in group _Project Deliverable User_ (or _Project Deliverable
  Validator_).

## Flow

1. Open the **Project > Project > Deliverables** menu.
2. Open the record to finish.
3. Click the **Done** button.
4. Click **OK** on the confirmation dialog.

## Post-Condition

- Status changes to **Done**.
