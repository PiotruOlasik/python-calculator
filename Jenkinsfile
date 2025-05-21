pipeline {
    agent {
        docker {
            image 'python:3.10'
        }
    }
    stages {
        stage('Checkout') {
            steps {
                echo 'Pliki są już dostępne lokalnie.'
            }
        }

        stage('Install dependencies') {
            steps {
                sh 'pip install -r /home/project/requirements.txt'
            }
        }

        stage('Run tests') {
            steps {
                sh 'pytest /home/project/test_main.py'
            }
        }
    }
}
