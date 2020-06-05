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
        stage('Push Container Image') {
            steps {
                withCredentials([string(credentialsId: 'dockerpw', variable: 'DOCKERPW')]){
                    sh 'bash ./pushcontainer.sh $DOCKERPW'
                }
            }
        }
        stage('Deploy Containers to EKS') {
            steps {
                withAWS(credentials: '(udacityIaC) programmaticAccessAdmin', region: 'eu-central-1'){
                    sh 'bash ./deploycontainers.sh'
                 }
            }
        }
        // stage('Clean up local Container Image') {
        //     steps {
        //         sh 'bash ./cleanupdocker.sh'
        //     }
        //}
    }

}