# Finish Project Phase

> **Module:** `ssi_project`\
> **Model:** `project_phase`\
> **Menu:** Project > Project > Phases\
> **Actor:** user in group _Project Phase User_\
> **State:** `open` → `done`\
> **Requires:** `05-approve`

## Pre-Condition

- **Record:** Status is **On Progress**.
- **Record:** The phase is a **Group of Phase** without child phases, or a **Single
  Phase** without tasks.
- **Config:** An active `policy.template` for `project_phase` grants `done_ok` for state
  **On Progress** to the actor's group, with the additional condition above.

- **Access:** User is in group _Project Phase User_ (or _Project Phase Validator_).

## Flow

1. Open the **Project > Project > Phases** menu.
2. Open the record to finish.
3. Click the **Done** button.
4. Click **OK** on the confirmation dialog.

## Post-Condition

- Status changes to **Done**.
