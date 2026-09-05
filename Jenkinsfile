pipeline{
  agent any
  stages{
     stage('Checkout'){
       steps{
         checkout scm
       }
     } 
     stage('Install dependancies'){
       steps{
         sh '.venv/bin/python -m pip install -r requirements.txt'
       }
     }
     stage('Test'){
       steps{
         steps{
           sh '.venv/bin/python -m pytest'
         }
       }
     }
  }
}
