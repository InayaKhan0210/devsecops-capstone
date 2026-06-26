pipeline {
    agent any

    stages {
        stage('Project Info') {
            steps {
                sh 'pwd'
                sh 'ls -la'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t devsecops-notes-app .'
            }
        }
    }
}