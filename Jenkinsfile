pipeline {
  agent any

  environment {
    IMAGE_NAME = "demo-jenkins-docker"
    CONTAINER_NAME = "demo-jenkins-docker"
    APP_PORT = "5000"
  }

  stages {

    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Build Docker Image') {
      steps {
        script {
          def tag = "${env.BUILD_NUMBER}"
          sh """
            docker build -t ${IMAGE_NAME}:${tag} .
            docker tag ${IMAGE_NAME}:${tag} ${IMAGE_NAME}:latest
          """
        }
      }
    }

    stage('Deploy to EC2') {
      steps {
        script {
          def tag = "${env.BUILD_NUMBER}"

          sh '''
            if docker ps -q --filter "name=demo-jenkins-docker" | grep -q . ; then
              docker stop demo-jenkins-docker || true
            fi

            if docker ps -a -q --filter "name=demo-jenkins-docker" | grep -q . ; then
              docker rm demo-jenkins-docker || true
            fi
          '''

          sh """
            docker run -d --name demo-jenkins-docker -p 5000:5000 --restart unless-stopped ${IMAGE_NAME}:${tag}
          """
        }
      }
    }

    stage('Health Check') {
      steps {
        sh '''
          sleep 3
          curl -s -o /dev/null -w "%{http_code}" http://localhost:5000 || true
        '''
      }
    }
  }

  post {
    success {
      echo "Deployment successful!"
    }
    failure {
      echo "Deployment failed. Check logs!"
    }
  }
}
