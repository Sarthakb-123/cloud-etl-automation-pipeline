import psycopg2


def connect_redshift():

    conn = psycopg2.connect(
        host="redshift.amazonaws.com",
        port="5439",
        database="dev",
        user="awsuser",
        password="password"
    )

    print(
        "Connected to Redshift"
    )

    conn.close()


if __name__ == "__main__":

    connect_redshift()