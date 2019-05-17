from pandas import read_csv


def distinct():
    print("intiating distinct...")
    try:
        df = (
            read_csv("crawl_results.csv", usecols=["Product Name", "Price"])
            .drop_duplicates(keep="first")
            .reset_index()
        )
        final_result = "final_result.csv"
        df.to_csv(final_result, index=False)
    except FileNotFoundError:
        print("crawl_results.csv must exsist to distinct results.")
