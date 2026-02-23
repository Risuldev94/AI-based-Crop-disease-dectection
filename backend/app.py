import os
from flask import Flask, request, jsonify
from backend.services.detector import detect_disease
from backend.services.recommender import recommend_treatment
from backend.services.alerts import generate_alert
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "backend/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "CropGuard AI backend is running",
        "usage": "Open frontend/index.html in browser"
    })


@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        if "image" not in request.files:
            return jsonify({"error": "No image uploaded"}), 400

        image = request.files["image"]
        crop = request.form.get("crop", "Unknown")

        if image.filename == "":
            return jsonify({"error": "Empty filename"}), 400

        image_path = os.path.join(UPLOAD_FOLDER, image.filename)
        image.save(image_path)

        ai_result = detect_disease(image_path)
        treatment = recommend_treatment(ai_result["disease"])
        alert = generate_alert(ai_result["confidence"])

        return jsonify({
            "AI_Analysis": ai_result,
            "Crop": crop,
            "Treatment_Recommendation": treatment,
            "Alert_Level": alert
        })

    except Exception as e:
        print("BACKEND ERROR:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
