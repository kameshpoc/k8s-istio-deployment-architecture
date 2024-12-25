# Repository: k8s-istio-deployment-architecture

This repository is public for reference purposes only. Contributions in the form of issues, pull requests, or feature requests are not accepted. If you'd like to use or modify this project, please fork it.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

# Repository Overview

## Motivation

This repository is dedicated to demonstrating the process of establishing a robust **application architecture** on a Minikube cluster using **Istio**. The focus is on configuring and deploying infrastructure components to ensure secure communication, namespace isolation, and effective traffic routing with Istio's advanced capabilities like **path-based routing**.

### Key Objectives:
1. Establish secure namespaces for application components.
2. Deploy and configure core services with a focus on architecture rather than application logic.
3. Utilize Istio for:
   - Path-based routing for service traffic.
   - Enabling observability and secure communication.
4. Showcase foundational setups that can scale with additional features like **circuit-breaking** and **mTLS enforcement**.

---

## Intended Audience

This repository is for developers and architects who:
- Want to learn how to implement Kubernetes and Istio for application deployment.
- Need a starting point for designing secure and scalable service architectures.
- Are looking for examples of Istio configurations on a local Minikube setup.

---

## Repository Structure

### 1. **App Development**
   - Contains individual application files for four apps:
     - **Python source files (`.py`)**: (Dummy)Application logic for each app.
     - **`requirements.txt`**: Dependencies for each app.
     - **Dockerfile**: Used to containerize each app.
   - Apps included:
     1. Control Plane
     2. Guardrails
     3. Summariser
     4. Mock LLM

### 2. **App Deployment**
   - Houses the core infrastructure setup for deploying the application architecture on Minikube, including:
     - Istio installation and configuration.
     - Namespace creation with Istio injection enabled.
     - Ingress gateway setup for path-based routing.

---

## Focus of the Repository

This repository does **not** focus on the development of application business logic. Instead, it serves as a guide to:
- Set up a Kubernetes environment with Istio.
- Manage secure and scalable application deployment.
- Configure essential Istio features for traffic management and security.

For detailed application logic, users are encouraged to integrate their own business requirements into the provided deployment architecture.
---

