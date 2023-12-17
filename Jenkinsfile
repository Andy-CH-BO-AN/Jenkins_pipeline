pipeline {
    agent any

    stages {
        stage('Set up env') {
            steps {
                python -m pip install --upgrade pip
                pip install -r requirement.txt
            }
        stage('test') {
            steps {
                pytest
            }
        }
    }
}