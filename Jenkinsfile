pipeline {
    agent any
    parameters {
        booleanParam(name: 'enableCron', defaultValue: false, description: '啟用定時觸發器')
        booleanParam(name: 'enableGitHubPush', defaultValue: true, description: '啟用 GitHub 推送觸發器')
    }

    triggers {
        cron(spec: 'H H * * *', enabled: params.enableCron) // 使用 enabled 取代 disabled
        githubPush(branches: [[enabled: params.enableGitHubPush]]) // 使用 branches 設定 enabled
    }

    environment {
        ENV = credentials('pipeline')
    }

    stages {
        stage('設定環境') {
            steps {
                script {
                    sh 'python3 -m pip install --upgrade pip'
                    sh 'pip3 install -r requirements.txt'
                }
            }
        }
        stage('測試') {
            steps {
                script {
                    sh 'python3 -m pytest -s -v'
                }
            }
        }
    }
}
