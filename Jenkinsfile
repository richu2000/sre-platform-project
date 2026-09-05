pipeline{
  agent any
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
  }
}
