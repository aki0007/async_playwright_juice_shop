pipeline {
    agent none
    stages {
        stage('Checkout') {
            agent {
                docker {
                    image 'my-juice-shop-image'
                }
            }
            steps {
                git 'https://github.com/your-repo.git'
            }
        }
        stage('Build') {
            agent {
                docker {
                    image 'my-juice-shop-image'
                }
            }
            steps {
                sh 'docker-compose up -d'
            }
        }
        stage('Test') {
            agent {
                docker {
                    image 'my-juice-shop-image'
                }
            }
            steps {
                sh 'pytest tests/ --alluredir=report/allure-results/'
            }
        }
        stage('Generate Allure Report') {
            agent {
                docker {
                    image 'my-juice-shop-image'
                }
            }
            steps {
                sh 'allure generate report/allure-results/ -o report/allure-report/'
            }
        }
        stage('Deploy') {
            agent {
                docker {
                    image 'my-juice-shop-image'
                }
            }
            steps {
                // Deploy logic here
            }
        }
        stage('Cleanup') {
            agent {
                docker {
                    image 'my-juice-shop-image'
                }
            }
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
