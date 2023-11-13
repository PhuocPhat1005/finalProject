from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector


app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze:
        return jsonify({"error": "Please provide text to analyze."}), 400

    try:
        response = emotion_detector(text_to_analyze)
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": f"Error during emotion detection: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(host = 'localhost', port = 5000)
