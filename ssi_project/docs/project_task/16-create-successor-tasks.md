# Create Successor Tasks

> **Module:** `ssi_project`\
> **Model:** `project.task`\
> **Menu:** Project > Tasks\
> **Actor:** user in group _Task User_ (or _Task Validator_)\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** The task is saved.
- **Access:** User is in group _Task User_ (or _Task Validator_).

## Flow

1. Open the **Project > Tasks** menu.
2. Find and open the record.
3. Open the **Dependency** tab.
4. Click the **Sucessor Tasks** button.
5. In the wizard that appears, add a row for each successor task:
   - **Name**: Enter the title of the successor task.
   - **Project**: Select the project of the successor task.
   - **Dependency Type**: Select the type of dependency.
   - **Assigned to**: Select the assignee. Optional.
6. Click **Confirm**.
7. Click **OK** on the confirmation dialog.

## Post-Condition

- A new task is created for each row, and the current task is its predecessor.
- The new tasks are listed under **Sucessors** on the **Dependency** tab.
