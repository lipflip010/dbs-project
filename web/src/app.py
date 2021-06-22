from multiprocessing import Lock

from flask import Flask, Response, request, render_template
from matplotlib.figure import Figure

from database import CountryNotFoundException
from plots import PlotCreator

app = Flask(__name__)
mutex = Lock()
plot_creator = PlotCreator()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/population-total')
def population_total():
    country = request.args.get('country')

    try:
        figure: Figure = plot_creator.get_population_total_plot_for(country)
        return Response(plot_creator.create_svg(figure), mimetype="image/svg+xml")
    except CountryNotFoundException:
        return f"""Country '{country}' not found""", 404


@app.route('/co2_emission')
def co2_emission():
    country = request.args.get('country')

    try:
        figure: Figure = plot_creator.get_co2_emission_plot_for(country)
        return Response(plot_creator.create_svg(figure), mimetype="image/svg+xml")
    except CountryNotFoundException:
        return f"""Country '{country}' not found""", 404
