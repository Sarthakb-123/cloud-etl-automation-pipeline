def transform_data(df):

    df = df.drop_duplicates()

    df.columns = [
        col.strip().replace(" ", "_")
        for col in df.columns
    ]

    df.fillna(0, inplace=True)

    if (
        "Units_Sold" in df.columns
        and "Unit_Price" in df.columns
    ):

        df["Revenue"] = (
            df["Units_Sold"]
            * df["Unit_Price"]
        )

    print(
        "Data transformation completed"
    )

    return df