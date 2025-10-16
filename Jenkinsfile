pipeline {
    agent any

    stages {
        stage('Preparar entorno') {
            steps {
                echo "Creando entorno virtual..."
                bat '"C:\Users\Shylocker\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.13\python.exe" -m venv venv'
                bat 'venv\\Scripts\\activate && pip install -r requirements.txt'
            }
        }

        stage('Ejecutar script') {
            steps {
                echo "Ejecutando script principal..."
                bat 'venv\\Scripts\\activate && python E:\HelloWorld.py'
            }
        }

        stage('Ejecutar tests') {
            steps {
                echo "Ejecutando pruebas..."
                bat 'venv\\Scripts\\activate && pytest tests\\ --maxfail=1 --disable-warnings -q'
            }
        }
    }

    post {
        success {
            echo "✅ Pipeline completado con éxito"
        }
        failure {
            echo "❌ Error en alguna etapa del pipeline"
        }
    }
}
