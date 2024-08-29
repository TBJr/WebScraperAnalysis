import matplotlib.pyplot as plt
import pandas as pd

def generate_visual_reports():
    df = pd.read_csv('../data/sentiment_data.csv')

    #Histogram of sentiment scores
    plt.figure(figsize=(10, 6))
    plt.hist(df['sentiment'], bins=20, color='blue', edgecolor='black')
    plt.title("Sentiment Analysis of Product Reviews")
    plt.xlabel("Sentiment Score")
    plt.ylabel("Number of Products")
    plt.show()

    # Price vs Sentiment scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['price'], df['sentiment'], color='green')
    plt.title("Price vs Sentiment Score")
    plt.xlabel("Price ($)")
    plt.ylabel("Sentiment Score")
    plt.show()

if __name__ == '__main__':
    generate_visual_reports()