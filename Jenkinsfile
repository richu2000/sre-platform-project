pipeline{
  agents any
  stages{
     stage('Checkout'){
       steps{
         scheckout scm
       }
     } 
     stage('Install dependancies'){
       steps{
         sh 'pip3 install -r app/requirements.txt'
       }
     }
     stage('Test'){
       steps{
         steps{
           sh 'pytest'
         }
       }
     }
  }
}
