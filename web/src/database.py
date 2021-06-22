import psycopg2


def execute_query(query: str):
    connection = psycopg2.connect(host="localhost", port=5432, database="dbs2021", user="postgres", password="postgres")

    cursor = connection.cursor()

    cursor.execute(query)
    query_results = cursor.fetchall()

    cursor.close()
    connection.close()

    return query_results


class CountryNotFoundException(Exception):
    pass
