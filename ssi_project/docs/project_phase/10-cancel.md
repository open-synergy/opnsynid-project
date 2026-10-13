# Cancel Project Phase

> **Module:** `ssi_project`\
> **Model:** `project_phase`\
> **Menu:** Project > Project > Phases\
> **Actor:** user in group _Project Phase Validator_\
> **State:** `draft` | `open` | `done` → `cancel`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** Status is **Draft**, **On Progress**, or **Done**.
- **Config:** An active `policy.template` for `project_phase` grants `cancel_ok` for
  state **Draft, On Progress, or Done** to the actor's group.

- **Access:** User is in group _Project Phase Validator_.
- **Data:** At least one cancellation reason is available for `project_phase`.

## Flow

1. Open the **Project > Project > Phases** menu.
2. Open the record to cancel.
3. Click the **Cancel** button.
4. In the wizard that appears, select the **Cancel Reason**.
5. Click **Confirm**.
6. Click **OK** on the confirmation dialog.

## Post-Condition

- Status changes to **Cancelled**.
- The selected cancellation reason is shown on the record.
