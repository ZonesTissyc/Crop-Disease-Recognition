from recognition import *
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    filename = "temp.jpg"
    file.save(filename)
    # 推理
    output = return_diagnosis_dic(filename)
    return jsonify({
        "prediction": output
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)