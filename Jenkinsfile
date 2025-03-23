pipeline {
    agent any
    stages {
        stage('Before Checkout') {
           steps {
               sh 'docker images -f reference="my-juice-shop-image"'
            }
         }

        stage('Checkout') {
            agent {
                docker {
                    image 'my-juice-shop-image'
                    args '--privileged -v /var/run/docker.sock:/var/run/docker.sock'
                }
            }
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
                sh 'pytest -s -v --alluredir=report/allure-results/'
            }
        }
        stage('Generate Allure Report') {
            steps {
                sh 'allure generate report/allure-results/ -o report/allure-report/'
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
