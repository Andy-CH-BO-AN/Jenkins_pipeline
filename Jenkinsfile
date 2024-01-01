pipeline {
    agent any
    parameters {
        booleanParam(name: 'enableCron', defaultValue: false, description: 'Enable cron trigger')
        booleanParam(name: 'enableGitHubPush', defaultValue: true, description: 'Enable GitHub Push trigger')
    }

    triggers {
        script {
            def cronExpression = '0 5 * * 2,4'
            def timeZone = 'Asia/Taipei'

            if (params.enableCron) {
                cron(cronExpression, false, timeZone)
            }

            if (params.enableGitHubPush) {
                githubPush()
            }
        }
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

