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
    endpoints = [
        {'name': 'co2-per-capita', 'title': 'CO2 emission per capita'},
        {'name': 'gdp-per-capita', 'title': 'GDP per capita'},
        {'name': 'renewable-energy', 'title': 'Renewable energy consumption'},
        {'name': 'gdp', 'title': 'Gross domestic price'},
        {'name': 'population-total', 'title': 'Total population'},
        {'name': 'co2-emission', 'title': 'Total co2 emission'}
    ]

    columns = [
        {'id': 'one', 'country': 'Albania'},
        {'id': 'two', 'country': 'United Kingdom'}
    ]
    return render_template('index.html', endpoints=endpoints, columns=columns)


@app.route('/population-total')
def population_total():
    country = request.args.get('country')

    try:
        figure: Figure = plot_creator.get_population_total_plot_for(country)
        return Response(plot_creator.create_svg(figure), mimetype="image/svg+xml")
    except CountryNotFoundException:
        return f"""Country '{country}' not found""", 404


@app.route('/co2-emission')
def co2_emission():
    country = request.args.get('country')

    try:
        figure: Figure = plot_creator.get_co2_emission_plot_for(country)
        return Response(plot_creator.create_svg(figure), mimetype="image/svg+xml")
    except CountryNotFoundException:
        return f"""Country '{country}' not found""", 404


@app.route('/renewable-energy')
def renewable_energy():
    country = request.args.get('country')

    try:
        figure: Figure = plot_creator.get_renewable_energy_plot_for(country)
        return Response(plot_creator.create_svg(figure), mimetype="image/svg+xml")
    except CountryNotFoundException:
        return f"""Country '{country}' not found""", 404


@app.route('/gdp')
def gdp():
    country = request.args.get('country')

    try:
        figure: Figure = plot_creator.get_gdp_plot_for(country)
        return Response(plot_creator.create_svg(figure), mimetype="image/svg+xml")
    except CountryNotFoundException:
        return f"""Country '{country}' not found""", 404


@app.route('/co2-per-capita')
def co2_per_capita():
    country = request.args.get('country')

    try:
        figure: Figure = plot_creator.get_co2_per_capita_plot_for(country)
        return Response(plot_creator.create_svg(figure), mimetype="image/svg+xml")
    except CountryNotFoundException:
        return f"""Country '{country}' not found""", 404


@app.route('/gdp-per-capita')
def gdp_per_capita():
    country = request.args.get('country')

    try:
        figure: Figure = plot_creator.get_gdp_per_capita_plot_for(country)
        return Response(plot_creator.create_svg(figure), mimetype="image/svg+xml")
    except CountryNotFoundException:
        return f"""Country '{country}' not found""", 404
