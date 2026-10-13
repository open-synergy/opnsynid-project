# Restart Project Phase

> **Module:** `ssi_project`\
> **Model:** `project_phase`\
> **Menu:** Project > Project > Phases\
> **Actor:** user in group _Project Phase Validator_\
> **State:** `cancel` | `reject` → `draft`\
> **Requires:** `10-cancel`

## Pre-Condition

- **Record:** Status is **Cancelled** or **Rejected**.
- **Config:** An active `policy.template` for `project_phase` grants `restart_ok` for
  state **Cancelled or Rejected** to the actor's group.

- **Access:** User is in group _Project Phase Validator_.

## Flow

1. Open the **Project > Project > Phases** menu.
2. Open the record to restart.
3. Click the **Restart** button.
4. Click **OK** on the confirmation dialog.

## Post-Condition

- Status returns to **Draft**.
- All approval records are removed and the approval template is cleared. A later Confirm
  starts the approval process from the beginning.
