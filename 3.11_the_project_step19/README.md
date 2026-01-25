# Exercise 3.11: The Project Step 19 - Resource Limits

This directory contains the solution for Exercise 3.11.

## Overview
Sensible resource requests and limits have been added to the application components to ensure stable scheduling and prevent resource contention on the GKE cluster.

## Configuration Details

### 1. Project Todo (Frontend)
- **Requests**: 150m CPU, 100Mi Memory
- **Limits**: 300m CPU, 200Mi Memory

### 2. Todo Backend
- **Requests**: 50m CPU, 64Mi Memory
- **Limits**: 100m CPU, 128Mi Memory

### 3. Postgres Database
- **Requests**: 50m CPU, 128Mi Memory
- **Limits**: 500m CPU, 512Mi Memory

These values ensure that:
- The backend and frontend have guaranteed resources to start up.
- The database, which is more resource-intensive, has slightly higher allocations.
