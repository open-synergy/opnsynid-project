# Create Project

> **Module:** `ssi_project`\
> **Model:** `project.project`\
> **Menu:** Project > Projects\
> **Actor:** user in group _Project User_ (or _Project Validator_)\
> **State:** `—` → `draft`

## Pre-Condition

- **Data:** Optionally, a partner exists for each client unit (an organization, or a
  department or contact below the client).
- **Access:** User is in group _Project User_ (or _Project Validator_).

## Flow

1. Open the **Project > Projects** menu.
2. Click the **New** button. **(14.0: "Create")**
3. Fill in the required field:
   - **Project Name** _(required)_: Enter the name of the project.
4. On the **Settings** tab, select the **Units** below **Customer**:
   - **Units**: Select the client-side units of the project. Units may be organization
     partners or child contacts. They are the denominator of the project Definition of
     Done. Optional.
5. Click **Save**.

## Post-Condition

- A new record is created in **New** status.
- The selected units are listed in the **Units** field of the project.
- **Next Reporting Date** is read-only. It shows the earliest reporting date of the
  pending reporting point milestones of the project, and is empty when there is none.

## Related Views

- **Phases** stat button (`action_open_phase`): opens the list of phases of the project.
  Navigation only.
- **Deliverables** stat button (`action_open_deliverable`): opens the list of
  deliverables of the project. Navigation only.
- **Tasks**, **Documents**, and **Rating** stat buttons: open the related records of the
  project. Navigation only.
