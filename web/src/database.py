import psycopg2


def execute_query(query: str):
    conn = psycopg2.connect(host="db", port=5432, database="dbs2021", user="postgres", password="postgres")

    cur = conn.cursor()

    cur.execute(query)
    query_results = cur.fetchall()

    cur.close()
    conn.close()

    return query_results
