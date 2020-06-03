pipeline {
    agent any
    stages {        
        stage('Lint Dockerfile') {
            steps {
                sh 'hadolint Dockerfile'
            }
        }
        stage('Lint Python') {
            steps {
                sh 'bash ./lintpython.sh'
            }
        }
        stage('Build Container') {
            steps {
                echo 'Building..'
            }
        }
        stage('Push Container') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying..'
            }
        }
    }

}