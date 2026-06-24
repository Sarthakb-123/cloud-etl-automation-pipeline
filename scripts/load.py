from sqlalchemy import create_engine
from config import DATABASE_URL


def load_data(df):

    try:

        engine = create_engine(
            DATABASE_URL
        )

        df.to_sql(
            "sales_data",
            engine,
            if_exists="replace",
            index=False
        )

        print(
            "Data successfully loaded"
        )

    except Exception as e:

        print(
            f"Load failed: {e}"
        )