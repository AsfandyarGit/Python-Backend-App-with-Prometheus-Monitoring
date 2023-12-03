# FastAPI Backend with Prometheus Monitoring on Kubernetes


## Overview

This project includes a backend application built using FastAPI, a modern, fast web framework for building APIs with Python. This project also incorporates Prometheus for monitoring various aspects of the Kubernetes cluster.

## Features

- **FastAPI Backend:** Utilizing the power of FastAPI, this project included a very basic python backend application.

- **Prometheus Monitoring:** Integrated Prometheus counter metrics for HTTP requests, allowing you to monitor the number of request received on application and create alerts accordingly.

- **Dockerized Application:** The project comes with a Dockerfile to containerize the FastAPI application, making it easy to deploy and scale on kubernetes cluster.

- **Kubernetes Deployment with Minikube:** Take advantage of Kubernetes orchestration for seamless deployment and management. The project includes configurations for deployment on Minikube, providing a local Kubernetes cluster for testing and development.





## Getting Started

Follow these steps to get started with the project:

1. **Clone the repository:** 
   - `git clone https://gitlab.com/portfolio7062046/python-backend-app-with-prometheus-monitoring.git`

2. [Install Docker](https://docs.docker.com/get-docker/) to containerize the application.

3. [Install Minikube](https://minikube.sigs.k8s.io/docs/start/) for local Kubernetes development.

4. **Run the Python App:**
   - Navigate to the project directory: `cd your-project-directory`
   - Install dependencies: `pip install -r requirements.txt`
   - Run the FastAPI application: `uvicorn main:app --reload`
   - Open [http://localhost:8000](http://localhost:8000) to view the homepage.
   - Open [http://localhost:metrics](http://localhost:metrics) to view the httprequestcount

5. **Build Docker Image:**
   - Build the Docker image: `docker build -t my-image .`

6. **Tag Docker Image:**
   - Tag the Docker image: `docker bdocker tag my-image username/repo-name:my-image`


7. **Push Docker Image to Repository:**
   - Log in to your Docker Hub account: `docker login`
   - Push the image to the repository: `docker push username/repo-name:my-image`

8. **Deploy the App on Minikube:**
   - Start Minikube: `minikube start --driver=docker`
   - Apply Kubernetes configurations: `kubectl apply -f k8s.yaml`

9. **Install Helm**
   - sudo apt-get install helm

10. **Install Prometheus Helm Chart**
   - helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
   - helm install monitoring prometheus-community/kube-prometheus-stack -n default

11. **PortForwarding for Prometheus, Grafana and AlertManager**
   - kubectl port-forward service/monitoring-kube-prometheus-prometheus 9090:9090 	
   - kubectl port-forward service/monitoring-grafana 8083:80 	
   - kubectl port-forward service/monitoring-kube-prometheus-alertmanager 9093:9093 	

12. **Adding ServiceMonitor resource to define the scraping configuration for your FastAPI application**
   - kubectl apply -f my-app-monitor.yaml 

13. **Creating Custom Alerts**
   - kubectl apply -f alert-rules.yaml 

14. **Adding Email Password as Secret**
   - kubectl apply -f email-secret.yaml

15. **Changing Alert Manager Configuration to Send Email Notification when Alerts are firing**
   - kubectl apply -f alert-mgr-config.yaml
     
16. **Sending Http Requests to app**
   - ./loadtest.sh

Although the above step is going to trigger all the custom alerts but if it doesnt triggers CPU Load Alert you can use following
   - kubectl run cpu-test --image=containerstack/cpustress -- --cpu 4  --timeout 200s --metrics-brief

