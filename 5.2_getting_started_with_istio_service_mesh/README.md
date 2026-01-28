# Exercise 5.2 - Getting Started with Istio Service Mesh

## Setup
- **Platform**: k3d (Traefik disabled)
- **Istio Mode**: Ambient mesh
- **Sample App**: Bookinfo

---

## Evidence

### 1. k3d Cluster Created (no Traefik)
![k3d cluster](screenshots/terminal_start_k3d_no_trafik.png)

### 2. Istio CLI Installed
![istio cli](screenshots/terminal_install_istio_cli.png)

### 3. Ambient Mesh Installed
![ambient mesh](screenshots/terminal_installed_ambient_mesh.png)

### 4. Bookinfo App Deployed
![bookinfo pods](screenshots/app_install_step_1_getpods_after_apply_Bookinfo.png)

### 5. Bookinfo Accessible
![bookinfo browser](screenshots/app_install_step_2_browser_Bookinfo_accessing.png)

### 6. Kiali Dashboard
![kiali](screenshots/app_install_step_3_browser_viewing_kiali.png)

### 7. Kiali Traffic View
![kiali traffic](screenshots/app_install_step_4_browser_viewing_kiali_traffic.png)

### 8. Kiali After Full Config
![kiali final](screenshots/app_install_step_5_browser_viewing_kiali_traffic_final_after_all_config.png)

### 9. Cleanup
![cleanup](screenshots/app_install_step_6_terminal_cleanup_all.png)
