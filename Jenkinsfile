pipeline {
    agent any

    stages {
        stage('Set up env') {
            steps {
                script {
                    sh 'pip install -r requirement.txt'
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    sh 'pytest'
                }
            }
        }
    }
}
