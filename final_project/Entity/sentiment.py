from dataclasses import dataclass

@dataclass
class SentimentResult:
    sentiment: str
    confident: float

    @classmethod
    def from_json(cls, json_data):
        # results = []
        max_confident = 0
        max_sentiment = ""
        for k, v in json_data.items():
            if v > max_confident:
                max_confident = v
                max_sentiment = k
            # results.append(cls(k, v))
        return cls(max_sentiment, max_confident)
        # return results
    
# if __name__ == "__main__":
#     test = {
#         "happy": 0.65,
#         "sad": 0.35
#     }
#     print(SentimentResult.from_json(test))