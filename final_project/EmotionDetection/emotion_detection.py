import requests
import sys

sys.path.append("../final_project")
from Entity import SentimentResult


def emotion_detector(text_to_analyse):
    url = "https://api.uclassify.com/v1/uClassify/Sentiment/classify/"
    response = requests.get(
        url, params={"readKey": "QvjDTL27M5VL", "text": text_to_analyse}
    )

    formatted_response = response.json()
    Sentiment = SentimentResult.from_json(formatted_response)
    return (Sentiment.sentiment, Sentiment.confident)
