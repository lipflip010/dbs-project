import time
import redis
import database
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)


def get_hit_count(name: str):
    retries = 5
    while True:
        try:
            return cache.incr(name)
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


@app.route('/')
def hello():
    count = get_hit_count(hello.__name__)
    return 'Hello World from Docker! I have been seen {} times.\n'.format(count)


@app.route('/population-total')
def population_total():
    count = get_hit_count(population_total.__name__)
    query_result = database.execute_query("""SELECT * FROM population_total WHERE country_name='Germany' LIMIT 100""")
    return 'Hello World from population-total! I have been seen {} times.\n {}'.format(count, query_result)
