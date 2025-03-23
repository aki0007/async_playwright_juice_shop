pipeline {
    agent {
        docker {
            image 'python:3.9-slim'
        }
    }
    stages {
        stage('Install Requirements') {
            steps {
                sh 'pip install -r requirements/common.txt'
            }
        }
        stage('Install Playwright') {
            steps {
                sh 'playwright install'
            }
        }
        stage('Run Juice Shop') {
            steps {
                sh 'docker-compose up -d'
            }
        }
        stage('Run Pytest') {
            steps {
                sh 'pytest -s -v --alluredir=report/allure-results'
            }
        }
        stage('Stop Juice Shop') {
            steps {
                sh 'docker-compose stop'
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
