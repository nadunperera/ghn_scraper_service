from pandas import read_csv


def distinct(file_name):
    print("intiating distinct...")
    try:
        df = (
            read_csv("temp_dump.csv", usecols=["product_name", "price"])
            .drop_duplicates(keep="first")
            .reset_index()
        )
        final_result = file_name
        df.to_csv(final_result, index=False)
        print("removed duplicates, created final csv file.")
    except FileNotFoundError:
        print("temp_dump.csv must exsist to distinct results.")
