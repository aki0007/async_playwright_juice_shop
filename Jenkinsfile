pipeline {
    agent any

    environment {
        BROWSER = 'chrome'
        DEVICES = 'Desktop Chrome'
        LOCAL = '0'
        ENVIRONMENT = 'development'
        GLOBAL_URL = 'https://juice-shop.herokuapp.com/#/'
        TESTING_URL = 'login'
        LOGIN_USERNAME = 'jaksa.milanovic007@gmail.com'
        LOGIN_PASSWORD = 'Test123*'
        SECURITY_ANSWER = 'aki'
    }

    stages {
        stage('Set up Docker') {
            steps {
                script {
                    // Ensure Docker is available, this should be automatically handled by Docker Plugin
                    docker.image('bkimminich/juice-shop').inside {
                        echo "Docker container is ready"
                    }
                }
            }
        }

        stage('Set up Python Environment') {
            steps {
                // Use ShiningPanda plugin to create and activate Python virtual environment
                sh 'pip install --upgrade pip'
                sh 'pip install -r requirements/common.txt'
            }
        }

        stage('Install Playwright') {
            steps {
                script {
                    // Use ShiningPanda plugin to run Playwright installation
                    sh 'pip install playwright'
                    sh 'playwright install'
                }
            }
        }

        stage('Run Tests with Docker') {
            steps {
                script {
                    // Run tests inside Docker container using pytest-lovely-docker
                    sh 'pytest -s -v --docker --alluredir=report/allure-results'
                }
            }
        }

        stage('Publish Allure Report') {
            steps {
                allure includeProperties: false, jdk: '', results: [[path: 'report/allure-results']]
            }
        }
    }

    post {
        always {
            cleanWs() // Clean workspace after execution
        }
    }
}
