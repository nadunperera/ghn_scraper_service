import pandas as pd


def distinct():
    df = pd.read_csv('crawl_results.csv', usecols=['Product Name', 'Price']).drop_duplicates(keep='first').reset_index()
    file_name = "output.csv"
    df.to_csv(file_name, index=False)
