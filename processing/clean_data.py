import pandas as pd


def clean_data():
    df = pd.read_csv('../data/raw/train.csv')
    df['price'] = df['price'].str.replace('$', '').astype(float)
    df['reviews'] = df['reviews'].str.replace(' out of 5 stars', '').astype(float)

    df.dropna(inplace=True)
    df.to_csv('../data/cleaned_data.csv', index=False)

if __name__ == '__main__':
    clean_data()