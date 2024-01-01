pipeline {
    agent any
    parameters {
        booleanParam(name: 'enableCron', defaultValue: false, description: 'Enable cron trigger')
        booleanParam(name: 'enableGitHubPush', defaultValue: true, description: 'Enable GitHub Push trigger')
    }

    triggers {
        cron(spec: 'H H * * *', disabled: !params.enableCron)
        githubPush(disabled: !params.enableGitHubPush)
    }

    environment {
        ENV = credentials('pipeline')
    }

    stages {
        stage('Set up env') {
            steps {
                sh 'python3 -m pip install --upgrade pip'
                sh 'pip3 install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'python3 -m pytest -s -v'
            }
        }
    }
}
