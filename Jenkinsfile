pipeline {
    agent any

    environment {
        VENV_PATH = "${WORKSPACE}/venv"
    }

    stages {
        stage('Setup Virtual Environment') {
            steps {
                sh """
                    python3 -m venv ${VENV_PATH}
                    . ${VENV_PATH}/bin/activate
                    pip install --upgrade pip
                """
            }
        }
        stage('Install Requirements') {
            steps {
                sh """
                    . ${VENV_PATH}/bin/activate
                    pip install -r requirements/common.txt
                """
            }
        }
        stage('Install Playwright') {
            steps {
                sh """
                    . ${VENV_PATH}/bin/activate
                    playwright install
                """
            }
        }
        stage('Run Pytest') {
            steps {
                sh """
                    . ${VENV_PATH}/bin/activate
                    pytest -s -v --alluredir=report/allure-results
                """
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
