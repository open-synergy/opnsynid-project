# Reset Document Number — Project Deliverable

> **Module:** `ssi_project`\
> **Model:** `project_deliverable`\
> **Menu:** Project > Project > Deliverables\
> **Actor:** user in group _Project Deliverable Validator_\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** Status is **Draft**.
- **Config:** An active `policy.template` for `project_deliverable` grants
  `manual_number_ok` for state **Draft** to the actor's group.

- **Config:** An active `sequence.template` for `project_deliverable` exists.
- **Access:** User is in group _Project Deliverable Validator_.

## Flow

1. Open the **Project > Project > Deliverables** menu.
2. Open the record whose document number will be reset.
3. Click the **Reset Document Number** button.
4. Click **OK** on the confirmation dialog.

## Post-Condition

- Document number returns to **/**.
- The record receives an automatic number again when it is confirmed or started,
  according to the sequence template configuration.
