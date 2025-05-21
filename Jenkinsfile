pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/PiotruOlasik/python-calculator.git'
            }
        }

        stage('Install dependencies') {
            steps {
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install -r requirements.txt'
            }
        }

        stage('Run tests') {
            steps {
                sh './venv/bin/pytest'
            }
        }
    }
}
