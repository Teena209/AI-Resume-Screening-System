pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code from GitHub...'
                checkout scm
            }
        }
        stage('Install Dependencies') {
            steps {
                echo 'Installing Python dependencies...'
           bat '"C:\\Users\\teena\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pip install pandas numpy scikit-learn'
            }
        }
        stage('Run Resume Screening') {
            steps {
                echo 'Running AI Resume Screening System...'
                bat '"C:\\Users\\teena\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" resume_screening.py'
            }
        }
    }
}
