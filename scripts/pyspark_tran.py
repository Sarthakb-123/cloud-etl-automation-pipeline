from pyspark.sql import SparkSession
from pyspark.sql.functions import col


def spark_transform():

    spark = (
        SparkSession.builder
        .appName("CloudETL")
        .getOrCreate()
    )

    df = spark.read.csv(
        "data/europe_sales_records.csv",
        header=True,
        inferSchema=True
    )

    df = df.dropDuplicates()

    if (
        "Units Sold" in df.columns
        and "Unit Price" in df.columns
    ):

        df = df.withColumn(
            "Revenue",
            col("Units Sold")
            * col("Unit Price")
        )

    df.show(5)

    spark.stop()


if __name__ == "__main__":

    spark_transform()