A simple Web Application for testing out ArgoCD and ArgoRollouts. This outlines the process of deploying the application using a GitOps pipeline with Argo CD and managing releases with Argo Rollouts for canary deployments.

### Setup and Configuration
1. **Git Repository:** Create a Github repository to store the application's source code and Kubernetes manifests.
2. **MiniKube Setup**: Setup Minkube locally by following the [Minikube docs](https://minikube.sigs.k8s.io/docs/start/)
3. **Argo CD Installation:** Follow the official Argo CD documentation to install and configure Argo CD on the Kubernetes cluster. Refer to the documentation for your specific environment.
4. **Argo Rollouts Installation:** Install the Argo Rollouts controller on the Kubernetes cluster using the official installation guide.

### Creating the GitOps Pipeline

1. **GitHub Actions**: Setup Workflows to create and push Images to DockerHub. Setup another workflow to update Kubernetes manifests with the latest pushed image on completion.
2. **Argo CD Integration:** Configure Argo CD to monitor the Git repository for changes. Define an Application resource in Argo CD that points to the repository and instructs it to deploy the manifests to the Kubernetes cluster upon detecting changes. Follow the [ArgoCD Tutorial](https://argo-cd.readthedocs.io/en/stable/getting_started/)for this.

### Implementing a Canary Release with Argo Rollouts 

1. **Rollout Strategy:** Modify the deployment manifest to leverage Argo Rollouts. Define a rollout object that specifies a canary release strategy. This strategy allows us to deploy the new version to a small subset of users first, and gradually increase traffic to it if everything seems stable. Follow the [ArgoRollouts Tutorial](https://argo-rollouts.readthedocs.io/en/stable/getting-started/) for this.
2. **Trigger a Rollout:** Make a change to the application's code. Update the Dockerfile and rebuild the image. Push the new image to the container registry. Finally, modify the rollout definition in the Git repository to reference the new image and trigger a new rollout.
3. **Monitor the Rollout:** Use Argo CD and Argo Rollouts to monitor the deployment of the new version. Argo Rollouts will gradually increase traffic to the canary version while monitoring pre-defined health checks. Progress can be tracked within the Argo Rollouts UI or using `kubectl argo rollouts get rollout testapp-rollout --watch`

<img width="1038" alt="image" src="https://github.com/NXPY123/k8s/assets/46917698/899bbc49-4f49-4396-9248-94b3f82927da">
<img width="997" alt="image" src="https://github.com/NXPY123/k8s/assets/46917698/b8fdeef7-9ea5-4db6-a4ec-ca646f85aa07">
<img width="1042" alt="image" src="https://github.com/NXPY123/k8s/assets/46917698/0e6da770-2076-4243-8864-dace87a7b618">



### Cleaning Up Resources

- Use `kubectl get deployments, pods, services, rollout -A` to list all deployments, pods, services, and Rollout objects across all namespaces.

- Once the resources have been identified, they can be deleted  individually using `kubectl delete <resource_type> <resource_name>`.

- Or delete all resources within that namespace using `kubectl delete --all -n <namespace_name>`.

- After deleting the resources, use `kubectl get deployments, pods, services, rollout -A` again to verify that all the resources are gone.


### Challenges
1. CI/CD Integration
2. Image Build Platform Manifest Issues
3. Manifest Configuration for ArgoCD and ArgoRollouts
4. Setting up Kubernetes Cluster and Integrating ArgoCD and ArgoRollouts
5. Configuring Ingress for the Cluster
6. Monitoring Rollout Strategy
