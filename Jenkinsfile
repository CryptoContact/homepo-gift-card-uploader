pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
        stage('deploy') {
            steps {
                sh 'docker-compose up --build -d'
            }
        }
    }
}
