pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/Grzywocz-W/python-calculator.git'
            }
        }
        stage('Install dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run tests') {
            steps {
                sh 'pytest --maxfail=1 --disable-warnings -v'
            }
        }
    }
}