pipeline {
    agent {
        docker {
            image 'my-juice-shop-image'
        }
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/your-repo.git'
            }
        }
        stage('Build') {
            steps {
                sh 'docker-compose up -d'
            }
        }
        stage('Test') {
            steps {
                sh 'pytest tests/ --alluredir=report/allure-results/'
            }
        }
        stage('Generate Allure Report') {
            steps {
                sh 'allure generate report/allure-results/ -o report/allure-report/'
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

    post {
        always {
            allure([
                includeProperties: false,
                jdk: '',
                results: [[path: 'report/allure-results/']]
            ])
        }
    }
}
