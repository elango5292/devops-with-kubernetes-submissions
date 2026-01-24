# Exercise 3.8: The Project Step 17 - Automatic Cleanup

## Goal
Automatically delete the Kubernetes Environment when a branch is deleted.

## Changes
- **Directory**: `3.8_the_project_step17`
- **Project Path**: `3.8_the_project_step17/manifests` (configured via `PROJECT_PATH` in workflow)

## 1. Automatic Cleanup

Workflow **Delete Project NS** triggers on branch deletion:
- **Action**: Deletes the namespace matching the branch name.
- **Trigger**: `git push origin --delete <branch>`

## 2. Usage

1.  **Create**: `git push origin feature-branch` -> Deploys to `feature-branch` namespace.
2.  **Delete**: `git push origin --delete feature-branch` -> Deletes `feature-branch` namespace.
