pipeline {
    agent any

    environment {
        REPORT_DIR = 'report'
    }

    stages {
        stage('Start Services') {
            steps {
                script {
                    sh 'docker-compose up -d'
                    timeout(time: 60, unit: 'SECONDS') {
                        waitUntil {
                            sh(script: "docker ps | grep 'healthy'", returnStatus: true) == 0
                        }
                    }
                }
            }
        }

        stage('Run Tests') {
            parallel {
                stage('Unit Tests') {
                    steps {
                        sh 'pytest -s -v tests/unit'
                    }
                }
                stage('Integration Tests') {
                    steps {
                        sh 'pytest -s -v tests/integration'
                    }
                }
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: "${REPORT_DIR}/**/*.xml", allowEmptyArchive: true
        }
        cleanup {
            sh 'docker-compose down'
        }
    }
}
