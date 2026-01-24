# Exercise 3.6: The Project Step 15 - Automatic Deployment

## Goal
Set up a **GitHub Actions** workflow to automatically deploy the application to **Google Kubernetes Engine (GKE)** whenever code is pushed to the repository.

## Changes
- **Directory**: `3.6_the_project_step15`
- **Workflow**: Created `.github/workflows/project_deployment.yaml`.
- **Infrastructure**: Configured to run on a **self-hosted runner**.

## 1. deployment Workflow

The workflow `Deploy Project Application` triggers on:
- `push` events.
- `workflow_dispatch` (manual trigger).

It performs the following steps:
1.  **Validation**: Checks if all required environment variables/secrets are present.
2.  **Authentication**: Authenticates with Google Cloud using a Service Account Key.
3.  **Setup**: Installs `gcloud`, `kubectl`, and `kustomize`.
4.  **Deploy**:
    - Uses `kustomize build` to generate manifests from `3.6_the_project_step15/manifests`.
    - Applies the manifests to the cluster using `kubectl apply -f -`.
    - Verifies the rollout status of the deployments.

## 2. Configuration

The workflow is dynamic and relies on the following **GitHub Secrets**:

| Secret | Description |
| :--- | :--- |
| `GKE_PROJECT` | Your Google Cloud Project ID. |
| `GKE_SA_KEY` | The JSON key for your Service Account (needs `Kubernetes Engine Service Agent`, `Storage Admin`, `Artifact Registry Administrator` roles). |
| `GKE_CLUSTER` | The name of your GKE cluster (e.g., `dwk-cluster`). |
| `GKE_ZONE` | The zone of your GKE cluster (e.g., `europe-north1-b`). |

## 3. Usage

1.  Ensure a self-hosted runner is active for the repository.
2.  Push changes to the repository.
3.  Monitor the "Actions" tab in GitHub to see the deployment progress.
