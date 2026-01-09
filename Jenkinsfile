pipeline {
    agent any

    environment {
        AWS_ACCOUNT_ID = '478468080341'  // <--- REPLACE THIS
        AWS_REGION = 'us-east-1'                // <--- CHANGE IF YOUR REGION IS DIFFERENT
        ECR_REPO_NAME = 'ofekpenso'
        registryCredential = 'aws-credentials'
    }

    stages {
        stage('Checkout') {
            steps {
                // Get code from the GitHub repo
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    echo "Building Docker image..."
                    // Create the full ECR address
                    dockerImage = docker.build("${ECR_REPO_NAME}:${BUILD_NUMBER}")
                }
            }
        }

        stage('Push to ECR') {
            steps {
                script {
                    // Log in to ECR using the credentials ID we created in Jenkins
                    docker.withRegistry("https://${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com", registryCredential) {
                        // Push the image
                        dockerImage.push("${BUILD_NUMBER}")
                        dockerImage.push("latest")
                    }
                }
            }
        }
    }
    
    post {
        always {
            // Clean up to save space
            sh "docker rmi ${ECR_REPO_NAME}:${BUILD_NUMBER} || true"
            sh "docker rmi ${ECR_REPO_NAME}:latest || true"
        }
    }
}
