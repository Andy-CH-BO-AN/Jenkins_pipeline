pipeline {
    agent any

    stages {
        stage('Set up env') {
            steps {
                script {
                    sh 'python3 -m pip install --upgrade pip'
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
