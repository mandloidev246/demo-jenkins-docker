🚀 CI/CD Pipeline Automation using Jenkins & Docker!

This project implements a complete CI/CD pipeline using Jenkins, Docker, GitHub Webhooks, and AWS EC2.
Every code push to GitHub automatically triggers Jenkins to build, test, containerize, and deploy the application to an EC2 instance.

🎯 Features

✔ Fully automated CI/CD pipeline
✔ Jenkins pipeline using Jenkinsfile
✔ Docker-based containerized Flask app
✔ GitHub Webhooks → auto-trigger builds
✔ Live deployment on AWS EC2
✔ Zero manual steps — 100% automation
✔ Health checks + automated container reload

🛠 Tech Stack

Jenkins (running inside Docker)

Docker Engine

GitHub Webhooks

AWS EC2 (Ubuntu)

Python Flask

Linux Shell

📦 Architecture

GitHub → Webhook → Jenkins → Docker Build → Deploy to EC2 → Live Flask App

🧱 Pipeline Stages

1. Checkout Code

Jenkins pulls the latest code using SCM.

2. Build Docker Image

Builds a Docker image using:

Python 3.11-slim base

requirements.txt

your Flask app (app.py)

3. Deploy Container

Stops old container & runs the new one:

docker run -d -p 5000:5000 demo-jenkins-docker:<VERSION>

4. Health Check

Ensures deployment succeeded by curling the app on EC2.

📁 Project Structure
.
├── app.py
├── Dockerfile
├── Jenkinsfile
├── requirements.txt
└── README.md

🌍 Live Application

Your app runs at:

👉 http://13.126.221.169:5000

(Output: “Hello from Jenkins + Docker CI/CD + Webhook!!”)

📌 Impact

⏱ Deployment time reduced by 70%

🔁 No manual steps → true continuous deployment

⚙️ Reliable, consistent builds

☁️ Cloud-hosted CI/CD pipeline

🚀 Future Enhancements

Add Slack notifications

Push Docker images to Docker Hub

Add unit testing stage

Add Blue/Green or Canary deployment

Add Terraform for Infra-as-Code

📜 Author

Dev Mandloi
4th Year CSE | DevOps & Cloud Enthusiast
