import io

from flask import Flask, Response, request, render_template
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.backends.backend_svg import FigureCanvasSVG
from matplotlib.figure import Figure

import database

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


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
    axis.set_ylabel("Population in Millions")
    axis.ticklabel_format(style="sci", scilimits=(6, 6), axis='y')
    axis.plot(year, count)

    return Response(create_svg(fig), mimetype="image/svg+xml")


def create_png(figure: Figure) -> bytes:
    output = io.BytesIO()
    FigureCanvas(figure).print_png(output)
    print(type(output.getvalue()))
    return output.getvalue()


def create_svg(figure: Figure) -> bytes:
    output = io.BytesIO()
    FigureCanvasSVG(figure).print_svg(output)
    print(type(output.getvalue()))
    return output.getvalue()
