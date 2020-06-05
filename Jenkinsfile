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
                withCredentials([string(credentialsId: 'dockerpw', variable: 'DOCKERPW')]){
                    sh 'bash ./pushcontainer.sh $DOCKERPW'
                }
            }
        }
        stage('Deploy') {
            steps {
                withAWS(credentials: '(udacityIaC) programmaticAccessAdmin', region: 'eu-central-1'){
                    sh 'bash ./testawscreds.sh'
                 }
            }
        }
    }

}