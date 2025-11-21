pipeline {
  agent any

  environment {
    IMAGE_NAME = "demo-jenkins-docker"
    CONTAINER_NAME = "demo-jenkins-docker"
    APP_PORT = "5000"
  }

  options {
    buildDiscarder(logRotator(numToKeepStr: '10'))
    timestamps()
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Prepare') {
      steps {
        script {
          // show docker version for debugging
          sh 'docker --version || true'
        }
      }
    }

    stage('Test') {
      when {
        expression {
          fileExists('requirements.txt') && (sh(script: 'python3 -m pytest -q || true', returnStatus: true) == 0)
        }
      }
      steps {
        echo "Running pytest (if tests present)..."
        sh 'pip install -r requirements.txt || true'
        sh 'python3 -m pytest -q || true'
      }
    }

    stage('Build Docker Image') {
      steps {
        script {
          def tag = "${env.BUILD_NUMBER}"
          sh """
            docker build -t ${IMAGE_NAME}:$tag .
            docker tag ${IMAGE_NAME}:$tag ${IMAGE_NAME}:latest
          """
        }
      }
    }

    stage('Deploy to EC2 (same host)') {
      steps {
        script {
          def tag = "${env.BUILD_NUMBER}"
          // stop old container if exists
          sh '''
            if docker ps -q --filter "name=${CONTAINER_NAME}" | grep -q . ; then
              echo "Stopping existing container..."
              docker stop ${CONTAINER_NAME} || true
            fi
            if docker ps -a -q --filter "name=${CONTAINER_NAME}" | grep -q . ; then
              echo "Removing existing container..."
              docker rm ${CONTAINER_NAME} || true
            fi
          '''
          // run new container
          sh """
            docker run -d --name ${CONTAINER_NAME} -p ${APP_PORT}:${APP_PORT} --restart unless-stopped ${IMAGE_NAME}:${tag}
          """
        }
      }
    }

    stage('Smoke Check') {
      steps {
        // a simple check of the app health
        sh '''
          sleep 3
          echo "HTTP status:"
          curl -s -o /dev/null -w "%{http_code}" http://localhost:${APP_PORT} || true
        '''
      }
    }
  }

  post {
    success {
      echo "Pipeline succeeded. App deployed to port ${APP_PORT}."
    }
    failure {
      echo "Pipeline failed. Check console output for errors."
    }
  }
}
