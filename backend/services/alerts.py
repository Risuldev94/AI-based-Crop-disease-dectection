# backend/alerts.py

def generate_alert(confidence):
    if confidence >= 90:
        return "HIGH ALERT – Immediate action required"
    elif confidence >= 70:
        return "MEDIUM ALERT – Monitor closely"
    else:
        return "LOW ALERT – Low risk"
