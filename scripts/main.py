from extract import extract_data
from transform import transform_data
from load import load_data


def run_pipeline():

    df = extract_data()

    if df is not None:

        transformed_df = (
            transform_data(df)
        )

        load_data(
            transformed_df
        )


if __name__ == "__main__":

    run_pipeline()