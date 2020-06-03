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
                sh 'bash ./buildcontainer.sh'
            }
        }
        stage('Push Container') {
            steps {
                echo 'Testing..'
                // withCredentials([dockerpw(credentialsId: 'dockerpw', variable: 'DOCKERPW')])
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying..'
            }
        }
    }

}