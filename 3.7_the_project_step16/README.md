# Exercise 3.7: The Project Step 16 - Dynamic Environments

## Goal
Improve the deployment workflow to creating a separate environment (namespace) for each branch. The `main` branch should still deploy to the `project` namespace.

## Changes
- **Directory**: `3.7_the_project_step16`
- **Workflow**: Updated `.github/workflows/project_deployment.yaml`.
- **Feature**: Branch-based namespace generation.

## 1. Dynamic Deployment Logic

The workflow now calculates the target namespace dynamically:

| Branch Name | Target Namespace | Description |
| :--- | :--- | :--- |
| `main` | `project` | Production environment. |
| `<branch-name>` | `<branch-name>` | Feature/Development environment (e.g. `feat-login` -> `feat-login`). |

## 2. Implementation

The **Deploy Application** step in the workflow handles this logic:
1.  Checks `github.ref_name`.
2.  Sets the `NAMESPACE` environment variable.
3.  Creates the namespace if it does not exist.
4.  Updates `kustomization.yaml` on the fly to use the new namespace.
5.  Deploys the application.

## 3. Usage

To create a new environment:
1.  Create a new branch: `git checkout -b feature/dynamic-env`.
2.  Push the branch: `git push origin feature/dynamic-env`.
3.  The workflow will trigger and deploy to the `feature/dynamic-env` namespace.

## 4. Cleanup (Manual Trigger)

You can manually trigger the workflow to delete an environment:
1.  Go to the **Actions** tab.
2.  Select **Deploy Project Application**.
3.  Click **Run workflow**.
4.  Select the **Branch** you want to clean up.
5.  In the **Action to perform** dropdown, select `delete`.
6.  Click **Run workflow**.

This will delete the namespace corresponding to that branch.

## 5. Deployment Naming

**Note:** Starting from this step, the deployment and service name has been changed from `project-step<number>` to a generic **`project-todo`**.

This change simplifies configuration and avoids the need to update the name with every exercise step.
