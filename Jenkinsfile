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
            choices: ['none', 'level_1', 'level_2'],
            description: 'Select test suite level (leave as "none" to run all tests)'
        )
        string(
            name: 'THREADS',
            defaultValue: '1',
            description: 'Number of parallel threads to use (default is 1)'
        )
    }


    options {
        timestamps() // Add timestamps to the console output
    }

    triggers {
        githubPush() // Trigger builds based on GitHub hooks
    }

    stages {
        stage('Setup Environment') {
            steps {
                sh '''
                    # Delete workspace before build starts
                    # Ensure Python virtual environment exists
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements/common.in
                    playwright install
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
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
