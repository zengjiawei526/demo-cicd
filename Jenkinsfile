pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo '拉取代码...'
                // Jenkins 的 Git 插件会自动 checkout，这里只是占位
            }
        }

        stage('Setup') {
            steps {
                sh 'python3 -m venv .venv'
                sh '. .venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh '. .venv/bin/activate && pytest tests/ --html=report.html --self-contained-html'
            }
        }
    }

    post {
        always {
            // 把测试报告发布到 Jenkins 界面
            publishHTML(target: [
                reportDir: '.',
                reportFiles: 'report.html',
                reportName: 'Pytest Report'
            ])
        }
    }
}