# Cloud Infrastructure Deployment for a Simple Web App

This project demonstrates a simple Flask web application integrated with PostgreSQL, deployed on AWS ECS using modern DevOps practices. It includes CI/CD with GitHub Actions, containerization with Docker, infrastructure-as-code with Terraform, and monitoring with healthchecks and CloudWatch.

Overview
The Flask app serves a simple page and a /health endpoint. The app is containerized, stored in AWS ECR, and deployed to ECS in the eu-north-1 region using Terraform. GitHub Actions automates the build and deployment pipeline, with monitoring via AWS CloudWatch.

## 📂 Structure

cloud-infra-demo/
├── app/
│ ├──templates/
│ |── index.html
│ ├── main.py
│ ├── requirements.txt
├── Dockerfile
├── .dockerignore
├── terraform/
│ ├── main.tf
│ ├── variables.tf
│ ├── outputs.tf
├── .github/
│ ├── workflows/
│ |── docker-deploy.yml
├── README.md

---

## 🧩 Technology

- Python 3.11
- Flask
  ✅ **Containerization:**
- Docker
  ✅ **Infrastructure as Code (IaC):**
- Terraform
  ✅ **CI/CD:**
- GitHub Actions
  ✅ **Моніторинг:**
- Healthcheck endpoint (`/health`)
- CloudWatch Logs

---

Setup and Deployment
Prerequisites:
Docker
AWS CLI
Terraform
GitHub account
AWS IAM permissions for ECS, ECR, and IAM

## ⚙️

Local Setup

1. Clone the repository:git clone https://github.com/Olena3K/cloud-infra-demo.git
   cd cloud-infra-demo
2. Install dependencies:
   pip install -r app/requirements.txt
3. Run the Flask app:
   python app/main.py
4. Access your localhost:80 and /health.

Docker Setup

1. Build the Docker image:
   docker build -t cloud-infra-demo .
2. Run the container:
   docker run -p 80:80 -d cloud-infra-demo
3. Verify healthcheck:
   docker ps

Cloud Deployment

1. Configure AWS CLI:
   aws configure
   (Set region to eu-north-1.)
2. Initialize Terraform:
   cd terraform
   terraform init
3. Deploy infrastructure:
   terraform apply
4. Access the app at the ECS service URL.
