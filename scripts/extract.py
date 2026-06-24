import pandas as pd


def extract_data(
    file_path="data/europe_sales_records.csv"
):

    try:
        df = pd.read_csv(file_path)

        print(
            f"Successfully loaded {len(df)} records"
        )

        return df

    except Exception as e:

        print(
            f"Extraction failed: {e}"
        )

        return None