import time
import redis
import database
import io
import random
from flask import Flask, Response, request
from matplotlib.backends.backend_svg import FigureCanvasSVG
from matplotlib.figure import Figure

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)


@app.route('/population-total')
def population_total():
    country = request.args.get('country')
    query = f"""SELECT year,count FROM population_total WHERE country_name='{country}' LIMIT 100"""
    query_result = database.execute_query(query)
    year, count = zip(*query_result)
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)

    axis.plot(year, count)

    output = io.BytesIO()
    FigureCanvasSVG(fig).print_svg(output)
    return Response(output.getvalue(), mimetype="image/svg+xml")
