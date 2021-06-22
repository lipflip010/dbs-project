import psycopg2


def execute_query(query: str):
    connection = psycopg2.connect(host="localhost", port=5432, database="dbs2021", user="postgres", password="postgres")

    cursor = connection.cursor()

    cursor.execute(query)
    query_result = cursor.fetchall()

    print(query_result)
    if not query_result:
        raise CountryNotFoundException("Country not found")

    cursor.close()
    connection.close()

    return query_result


class CountryNotFoundException(Exception):
    pass
