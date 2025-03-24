pipeline {
    agent any

    stages {
        stage('Install Requirements') {
            steps {
                sh 'AAAA'
                sh 'python --version'
                sh 'pip install -r requirements/common.txt'
            }
        }
        stage('Install Playwright') {
            steps {
                sh 'playwright install'
            }
        }
        stage('Run Pytest') {
            steps {
                sh 'pytest -s -v --alluredir=report/allure-results'
            }
        }
    }
    post {
        always {
            allure([
                includeProperties: false,
                jdk: '',
                results: [[path: 'report/allure-results']]
            ])
        }
    }
}
