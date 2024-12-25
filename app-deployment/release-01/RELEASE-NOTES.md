# Release Notes: Version 1.0

## Overview
The initial release of the application (Release 1) introduces the foundational setup, deployment of core services, and basic Istio configurations. This release focuses on establishing the application architecture, ensuring secure namespaces, and enabling path-based routing using Istio.

---

## Features and Implementations

### 1. **Istio Installation**
   - Installed and configured Istio on the Minikube cluster using the following files:
     - `1-istio-init.yaml`: Initialized Istio components.
     - `2-istio-minikube.yaml`: Deployed Istio on Minikube.

### 2. **Namespace Creation**
   - Created dedicated namespaces for application components with Istio injection enabled using:
     - `4-create-namespace.yaml`: Ensures proper isolation and Istio proxy injection for the services.

### 3. **Application Deployment**
   - Deployed the following core components:
     - **Control Plane Service**
       - Configured using `5.1-controlplane-configmap.yaml` for environment-specific settings.
       - Application deployed with `5.2-controlplane-app.yaml`.
     - **Guardrails Service**
       - Deployment defined in `6-guardrails-app.yaml`.
     - **Mock LLM Service**
       - Deployment configured using `7-mockllm-app.yaml`.
     - **Summariser Service**
       - Configured with `8.1-summariser-configmap.yaml`.
       - Deployment defined in `8.2-summariser-app.yaml`.

### 4. **Ingress Gateway and Path-Based Routing**
   - Configured a shared Istio Ingress Gateway to enable external traffic access.
   - Implemented path-based routing for `/generatetext` and `/summariser` paths:
     - `9-istio-rules-config.yaml`: Defines routing logic to respective services based on the request path.

### 5. **Secure Communication**
   - Introduced `3-kiali-secret.yaml` for secret management, ensuring secure access to the Kiali dashboard.

---

## Planned Features for Release 2
   - **Circuit Breaking**
     - To introduce resilience and manage traffic spikes using:
       - `10-circuit-breaking.yaml`
   - **Enforce mTLS**
     - To enforce mutual TLS for secure communication between services using:
       - `11-enforce-mtls-only.yaml`
   - **Enabling Wirhtes routing to support Canary Release (A/B testing)**
     - TBD    

---

## Known Limitations
   - Weighted routing for risky service versions is not yet implemented but can be added in future iterations.
   - Circuit-breaking and mTLS enforcement are not part of Release 1 but will be introduced in Release 2.

---

## How to Use
1. Follow the step-by-step instructions in the corresponding [README](README.md) files for setup and deployment.
2. Test path-based routing by sending requests to:
   - `/generatetext`
   - `/summariser` through the shared ingress gateway.
3. Monitor services using the Kiali dashboard secured with the provided secret.

---

## Release Summary
Release 1 establishes the foundation for the application, with key components deployed and a robust networking layer configured through Istio. Subsequent releases will build on this groundwork to enhance resilience, security, and advanced routing capabilities.
