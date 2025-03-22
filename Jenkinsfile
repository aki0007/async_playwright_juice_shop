pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/aki0007/async_playwright_juice_shop'
            }
        }
        stage('Build') {
            steps {
                sh 'docker-compose up -d'
            }
        }
        stage('Test') {
            steps {
                script {
                    sh 'pytest tests/'
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    // Deploy logic here
                }
            }
        }
        stage('Cleanup') {
            steps {
                sh 'docker-compose down'
            }
        }
    }
}
