# backend/recommender.py

def recommend_treatment(disease):
    recommendations = {
        "Healthy": "No treatment required. Continue regular monitoring.",
        "Bacterial Spot": "Apply copper-based fungicide and avoid overhead watering.",
        "Early Blight": "Use appropriate fungicide and remove infected leaves.",
        "Late Blight": "Immediate fungicide treatment required. Improve drainage.",
        "Leaf Mold": "Ensure proper air circulation and apply fungicide.",
        "Rust": "Apply sulfur fungicide and maintain plant spacing.",
        "Mosaic Virus": "Remove infected plants and control pests."
    }

    return recommendations.get(
        disease,
        "Consult an agricultural expert for further analysis."
    )
