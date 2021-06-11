import io

import redis
from flask import Flask, Response, request
from matplotlib.backends.backend_svg import FigureCanvasSVG
from matplotlib.figure import Figure

import database

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)


@app.route('/population-total')
def population_total():
    country = request.args.get('country')
    query = f"""SELECT year,count FROM population_total WHERE country_name='{country}' LIMIT 100"""
    query_result = database.execute_query(query)
    print(query_result)
    if not query_result:
        return "Null"

    year, count = zip(*query_result)
    fig = Figure()

    axis = fig.add_subplot(1, 1, 1)
    axis.set_title(f"Population of {country}")
    axis.set_xlabel("Year")
    axis.set_ylabel("Population")
    axis.ticklabel_format(useOffset=False, style='plain')
    axis.plot(year, count)

    output = io.BytesIO()
    FigureCanvasSVG(fig).print_svg(output)
    return Response(output.getvalue(), mimetype="image/svg+xml")
