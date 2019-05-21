from pandas import read_csv


def distinct(model_name, category_name):
    print("intiating distinct...")
    temp_dump_name = "temp_" + model_name + "_dump.csv"
    try:
        df = (
            read_csv(temp_dump_name, usecols=["product_name", "price"])
            .drop_duplicates(keep="first")
            .reset_index()
        )
        final_result = model_name + "-" + category_name + ".csv"
        df.to_csv(final_result, index=False)
        print("removed duplicates, created final csv file.")
    except FileNotFoundError:
        print(temp_dump_name + " must exsist to distinct results.")
