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
                sh 'pytest tests/'
            }
        }
        stage('Deploy') {
            steps {
                // Deploy logic here
            }
        }
        stage('Cleanup') {
            steps {
                sh 'docker-compose down'
            }
        }
    }
}
