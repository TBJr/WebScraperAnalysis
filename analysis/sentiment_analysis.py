import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer

def perform_sentiment_analysis():
    sia = SentimentIntensityAnalyzer()
    df = pd.read_csv('../data/cleaned_data.csv')
    df['sentiment'] = df['reviews'].apply(lambda x: sia.polarity_scores(str(x))['compound'])
    df.to_csv('../data/sentiment_data.csv', index=False)

if __name__ == '__main__':
    perform_sentiment_analysis()