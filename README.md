# API Documentation

## Endpoints

### /train
- **Method**: POST
- **Description**: Démarre l'entraînement du modèle.

### /infer
- **Method**: POST
- **Description**: Effectue l'inférence sur de nouvelles données.
- **Parameters**: 
  - `data` (JSON): Les données sur lesquelles effectuer l'inférence.

### /report
- **Method**: GET
- **Description**: Génère des rapports de fréquentation.

### /upload
- **Method**: POST
- **Description**: Upload un fichier de données.
- **Parameters**: 
  - `file` (File): Le fichier à uploader.
