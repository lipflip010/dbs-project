import time
import redis
import database
import io
import random
from flask import Flask, Response
from matplotlib.backends.backend_svg import FigureCanvasSVG
from matplotlib.figure import Figure

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)


@app.route('/population-total')
def population_total():
    query_result = database.execute_query(
        """SELECT year,count FROM population_total WHERE country_name='Germany' LIMIT 100""")
    year,count = zip(*query_result)
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)

    axis.plot(year,count)

    output = io.BytesIO()
    FigureCanvasSVG(fig).print_svg(output)
    return Response(output.getvalue(), mimetype="image/svg+xml")
    #return '{}'.format(query_result)


@app.route("/matplot-as-image")
def plot(num_x_points=50):
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    x_points = range(num_x_points)
    axis.plot(x_points, [random.randint(1, 30) for x in x_points])

    output = io.BytesIO()
    FigureCanvasSVG(fig).print_svg(output)
    return Response(output.getvalue(), mimetype="image/svg+xml")
