# Create Project

> **Module:** `ssi_project`\
> **Extends:** project — model `project.project`, aksi `01-create`

## Additional Pre-Condition

- **Data:** A partner exists for each client unit (an organization, or a department or
  contact below the client).

## Additional Fields

- **Units**: On the **Settings** tab, select the client-side units of the project (below
  **Customer**). Units may be organization partners or child contacts. They are the
  denominator of the project Definition of Done. Optional.
- **Next Reporting Date**: Read-only. Shows the earliest reporting date of the pending
  reporting point milestones of the project. It is empty when there is none.

## Modified Flow

- Anchor: none. No base work instruction exists for the Odoo core model
  `project.project`, so the steps below are self-contained.
- Open the **Project > Projects** menu, click the **New** button **(14.0: "Create")**,
  and fill in the **Project Name**.
- On the **Settings** tab, select the **Units** below **Customer**.
- Click **Save**.

## Related Views

- **Phases** stat button (`action_open_phase`): opens the list of phases of the project.
  Navigation only.
- **Deliverables** stat button (`action_open_deliverable`): opens the list of
  deliverables of the project. Navigation only.

## Additional Post-Condition

- The selected units are listed in the **Units** field of the project.
