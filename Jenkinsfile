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
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Run tests') {
            steps {
                dir('python-calculator') {
                    sh 'pytest'
                }
            }
        }
    }
}