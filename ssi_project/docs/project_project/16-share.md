# Share Project

> **Module:** `ssi_project`\
> **Model:** `project.project`\
> **Menu:** Project > Projects\
> **Actor:** user in group _Project User_ (or _Project Validator_)\
> **Requires:** `01-create`

## Pre-Condition

- **Data:** A partner with an email address exists to receive the shared link.
- **Access:** User is in group _Project User_ (or _Project Validator_).

## Flow

1. Open the **Project > Projects** menu.
2. Open the record to share.
3. Click the **Share** button.
4. In the wizard that appears, fill in the fields:
   - **Recipients**: Select the contacts to share the project with.
   - **Note**: Enter a message to include in the email. Optional.
5. Click **Send**.

## Post-Condition

- An email with the link to the project is sent to the selected recipients.
- The wizard closes and the project is unchanged.
