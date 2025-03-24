pipeline {
    agent any

    stages {
            stage('Checkout') {
            steps {
                git 'https://github.com/aki0007/async_playwright_juice_shop' // Simplest form if no authentication is needed
                // OR:  For authenticated access:
                //git credentialsId: 'your-git-credentials-id', url: 'https://github.com/aki0007/async_playwright_juice_shop'
            }
        }
        stage('Install Requirements') {
            steps {
                sh 'echo "Building..."'
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
