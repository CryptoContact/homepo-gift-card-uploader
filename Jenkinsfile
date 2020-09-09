pipeline {
    agent any

    options {
        buildDiscarder logRotator(daysToKeepStr: '1', numToKeepStr: '1')
    }

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
