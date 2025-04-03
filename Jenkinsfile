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

    parameters {
        choice(
            name: 'TEST_SUITE',
            choices: ['level_1', 'level_2'],
            description: 'Select test suite level'
        )
        string(
            name: 'THREADS',
            defaultValue: '1',
            description: 'Number of parallel threads to use'
        )
    }

    options {
        timestamps() // Add timestamps to the console output
    }

    triggers {
        githubPush() // Trigger builds based on GitHub hooks
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'master',
                    url: 'https://github.com/aki0007/async_playwright_juice_shop'
            }
        }

        stage('Setup Environment') {
            steps {
                sh '''
                    # Delete workspace before build starts
                    rm -rf *
                    # Ensure Python virtual environment exists
                    python3 -m venv venv
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    source venv/bin/activate
                    pytest -s -v \
                        --alluredir=report/allure-results \
                        -m ${TEST_SUITE} \
                        -n ${THREADS}
                '''
            }
        }
    }

    post {
        success {
            echo "Build succeeded. Generating Allure report..."
            allure([
                results: [[path: 'report/allure-results']]
            ])
        }

        failure {
            echo "Build failed. Check logs for details."
        }

        always {
            echo "Pipeline completed."
        }
    }
}
