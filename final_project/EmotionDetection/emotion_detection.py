import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://api.uclassify.com/v1/uClassify/Sentiment/classify/'
    response = requests.get(url, params={
        'readKey' : 'QvjDTL27M5VL',
        'text' : text_to_analyse
    })

    formatted_response = response.json()
    positive = formatted_response['positive']
    negative = formatted_response['negative']
    if positive >= negative:
        return ("Happy", positive)
    else:
        return ("Sadness", negative)
    
