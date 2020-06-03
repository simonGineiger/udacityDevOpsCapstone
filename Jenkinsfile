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
                sh 'bash docker build --tag=XCLapi .'
            }
        }
        stage('Push Container') {
            steps {
                echo 'Testing..'
                // withCredentials([usernameColonPassword(credentialsId: 'mylogin', variable: 'USERPASS')])
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying..'
            }
        }
    }

}