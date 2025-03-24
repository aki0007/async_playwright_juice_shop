pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/aki0007/async_playwright_juice_shop'
            }
        }
        stage('Setup Virtual Environment') {
            steps {
                sh 'python3 -m venv venv'  // Create virtual environment
            }
        }
        stage('Install Requirements') {
            steps {
                sh 'venv/bin/pip install -r requirements/common.txt'  // Use venv's pip
            }
        }
        stage('Install Playwright') {
            steps {
                sh 'venv/bin/playwright install'  // Use venv's playwright
            }
        }
        stage('Run Pytest') {
            steps {
                sh 'venv/bin/pytest -s -v --alluredir=report/allure-results'
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
