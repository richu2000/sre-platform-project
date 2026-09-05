pipeline{
  agent any
  environment {
        PATH = "/Users/richaparikh/.docker/bin:/opt/homebrew/bin:${env.PATH}"
  }
  stages{
     stage('Create virtual environment') {
            steps {
                sh 'python3 -m venv .venv'
            }
     }
     stage('Install dependancies'){
       steps{
         sh '.venv/bin/python -m pip install -r requirements.txt'
       }
     }
     stage('Test'){
       steps{
           sh '.venv/bin/python -m pytest'
       }
     }
    stage('Docker Build') {
      steps {
         sh 'docker build -t sre-demo:v1 .'
      }
    }
  }
}
