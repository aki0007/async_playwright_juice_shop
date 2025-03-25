pipeline {
    agent any

    stages {
        stage('Setup Virtual Environment') {
            steps {
                sh 'python3 -m venv venv'  // Create virtual environment
                sh 'source venv/bin/activate'
            }
        }
        stage('Install Requirements') {
            steps {
                sh 'pip install -r requirements/common.txt'  // Use venv's pip
            }
        }

        stage('Install Playwright') {
            steps {
                sh 'playwright install'  // Use venv's playwright
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
