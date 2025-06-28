pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                sh 'rm -rf python-calculator'
                sh 'git clone https://github.com/Grzywocz-W/python-calculator.git'
            }
        }

        stage('Install dependencies') {
            steps {
                dir('python-calculator') {
                    sh '''
                        python3 -m venv venv
                        . venv/bin/activate
                        pip install --upgrade pip
                        pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Run tests') {
            steps {
                dir('python-calculator') {
                    sh '''
                        . venv/bin/activate
                        pytest test_main.py --maxfail=1 --disable-warnings --exitfirst
                    '''
                }
            }
        }
    }

    post {
        failure {
            echo 'Build failed. Check test output and fix.'
        }
        success {
            echo 'All tests passed. Great job!'
        }
    }
}

