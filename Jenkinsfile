pipeline {
    agent any
    triggers {
        githubPush()
        cron('0 5 * * 2,4', false, 'Asia/Taipei')
    }

    environment {
        ENV = credentials('pipeline')
    }

    stages {
        stage('設定環境') {
            steps {
                sh 'python3 -m pip install --upgrade pip'
                sh 'pip3 install -r requirements.txt'
            }
        }
        stage('測試') {
            steps {
                sh 'python3 -m pytest -s -v'
            }
        }
    }
}
