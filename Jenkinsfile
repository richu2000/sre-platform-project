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
     stage('Security') {
      steps {
         echo 'Security scan will be added here'
      }
     }  
     stage('Get git sha'){
       steps {
         script{
           env.GIT_SHA = sh(
              script: 'git rev-parse --short HEAD',
              returnStdout: true
           ).trim()
           echo "Building commit:${env.GIT_SHA}"
         }
       }
     }
     stage('Docker Build') {
       steps {
          sh 'docker build -t myrepo:${GIT_SHA} .'
       }
     }
     stage('Docker Push') {
      steps {
         withCredentials([
             usernamePassword(
                 credentialsId: 'dockerhub-creds',
                 usernameVariable: 'DOCKER_USER',
                 passwordVariable: 'DOCKER_PASSWORD'
             )
         ]) {
             sh '''
                 echo "$DOCKER_PASSWORD" | docker login \
                     -u "$DOCKER_USER" \
                     --password-stdin

                 docker push \
                     "$DOCKER_USER/myrepo:$GIT_SHA"
             '''
         } 
      }
     }
  }
}
