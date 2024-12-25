# Kubernetes Deployment with Istio on Minikube --> Release 1.0

This folder provides YAML files to set up a Minikube cluster with Istio and deploy multiple applications with specific configurations.
This is Release 1.0 and you can find more details about it in [Release Notes](RELEASE-NOTES.md) 

## Prerequisites

1. Ensure **Minikube** is installed and running on your local machine.
2. Start Minikube with the following resources:
   ```bash
   minikube start --memory=4096 --cpus=2
   ```
   (You can increase `--cpus=4` if required.)
3. Install `kubectl` and ensure it is configured to work with the Minikube cluster.

## Deployment Steps

### General Instructions

- Install each file sequentially using the command:
  ```bash
  kubectl apply -f <filename>
  ```
- After applying the second file (`2-istio-minikube.yaml`), run the following command to ensure all containers are running before proceeding to the next step:
  ```bash
  kubectl get po -A
  ```
  Wait until all containers are in the `Running` state.

- **Note:** Step 3 is optional and can be skipped if not required.

---

### Deployment Sequence

1. **Initialize Istio**  
   Deploy the initial Istio components:
   ```bash
   kubectl apply -f 1-istio-init.yaml
   ```

2. **Deploy Istio on Minikube**  
   Apply the core Istio configurations for the Minikube cluster:
   ```bash
   kubectl apply -f 2-istio-minikube.yaml
   ```
   After this step, wait for all Istio-related pods to be in the `Running` state:
   ```bash
   kubectl get po -A
   ```

3. **(Optional) Configure Kiali Secret**  
   Skip this step if Kiali is not required:
   ```bash
   kubectl apply -f 3-kiali-secret.yaml
   ```

4. **Create Namespaces with Istio Injection**  
   Set up namespaces for all applications and enable Istio sidecar injection:
   ```bash
   kubectl apply -f 4-create-namespace.yaml
   ```

5. **Deploy Control Plane**  
   - Apply the ConfigMap for the control plane application:
     ```bash
     kubectl apply -f 5.1-controlplane-configmap.yaml
     ```
   - Deploy the control plane application:
     ```bash
     kubectl apply -f 5.2-controlplane-app.yaml
     ```

6. **Deploy Guardrails Application**  
   Deploy the guardrails service:
   ```bash
   kubectl apply -f 6-guardrails-app.yaml
   ```

7. **Deploy Mock LLM Application**  
   Deploy the mock LLM application:
   ```bash
   kubectl apply -f 7-mockllm-app.yaml
   ```

8. **Deploy Summariser Application**  
   - Apply the ConfigMap for the summariser application:
     ```bash
     kubectl apply -f 8.1-summariser-configmap.yaml
     ```
   - Deploy the summariser application:
     ```bash
     kubectl apply -f 8.2-summariser-app.yaml
     ```

9. **Configure Istio Routing Rules**  
   Set up Istio virtual services, gateways, and routing rules:
   ```bash
   kubectl apply -f 9-istio-rules-config.yaml
   ```

10. **Enable Circuit Breaking**  
    Configure circuit-breaking rules:
    ```bash
    kubectl apply -f 10-circuit-breaking.yaml
    ```

11. **Enforce mTLS Security**  
    Enforce mutual TLS (mTLS) for communication:
    ```bash
    kubectl apply -f 11-enforce-mtls-only.yaml
    ```

---

## Notes

- Ensure you have sufficient resources allocated to Minikube (`4GB memory`, `2+ CPUs`).
- The files in this repository must be applied in the exact sequence mentioned above for proper functionality.
- Use the following command to verify resources in all namespaces:
  ```bash
  kubectl get all -A
  ```

## Troubleshooting

- If pods are not running, check their status and logs:
  ```bash
  kubectl get po -A
  kubectl logs <pod-name> -n <namespace>
  ```
- To debug Istio, check the Istio proxy logs:
  ```bash
  kubectl logs <pod-name> -c istio-proxy -n <namespace>
  ```
