# Create Deliverable Type

> **Module:** `ssi_project`\
> **Model:** `project_deliverable_type`\
> **Menu:** Project > Configuration > Project > Deliverable Types\
> **Actor:** user in group _Project Deliverable Type_

## Pre-Condition

- **Data:** A deliverable type category exists.
- **Access:** User is in group _Project Deliverable Type_.

## Flow

1. Open the **Project > Configuration > Project > Deliverable Types** menu.
2. Click the **New** button. **(14.0: "Create")**
3. Fill in the required fields:
   - **Name** _(required)_: Enter the name of the deliverable type.
   - **Code** _(required)_: Enter a unique code, or click **Generate Code** in the form
     header to fill it from the configured sequence.
   - **Category** _(required)_: Select the deliverable type category of the type.
4. Click **Save**.

## Post-Condition

- A new deliverable type is created and is listed in **Deliverable Types**.
