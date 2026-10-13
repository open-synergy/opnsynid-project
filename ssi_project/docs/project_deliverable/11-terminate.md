# Terminate Project Deliverable

> **Module:** `ssi_project`\
> **Model:** `project_deliverable`\
> **Menu:** Project > Project > Deliverables\
> **Actor:** user in group _Project Deliverable User_\
> **State:** `open` → `terminate`\
> **Requires:** `05-approve`

## Pre-Condition

- **Record:** Status is **On Progress**.
- **Config:** An active `policy.template` for `project_deliverable` grants
  `terminate_ok` for state **On Progress** to the actor's group.

- **Access:** User is in group _Project Deliverable User_ (or _Project Deliverable
  Validator_).
- **Data:** At least one termination reason is available for `project_deliverable`.

## Flow

1. Open the **Project > Project > Deliverables** menu.
2. Open the record to terminate.
3. Click the **Terminate** button.
4. In the wizard that appears, select the **Terminate Reason**.
5. Click **Confirm**.
6. Click **OK** on the confirmation dialog.

## Post-Condition

- Status changes to **Terminated**.
