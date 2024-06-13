from flask import Flask, request, jsonify, render_template
import os
from training import train_model
from inference import load_model, infer
from annotation import annotate_faces
from database import create_database, insert_attendance_record, generate_report

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    file.save(os.path.join('uploads', file.filename))
    return jsonify({"message": "Fichier uploadé avec succès"}), 200

@app.route('/train', methods=['POST'])
def train_model_endpoint():
    data_path = 'data_path/djek3.jpg'
    model = train_model(data_path)
    return jsonify({"message": "Entraînement terminé"}), 200

@app.route('/infer', methods=['POST'])
def infer_endpoint():
    model = load_model()
    data = request.json
    results = infer(model, data)
    return jsonify({"results": results}), 200

@app.route('/report', methods=['GET'])
def generate_report_endpoint():
    report = generate_report()
    return jsonify({"report": report}), 200

if __name__ == '__main__':
    create_database()
    app.run(debug=True)
