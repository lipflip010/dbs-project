import io

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvasPNG
from matplotlib.backends.backend_svg import FigureCanvasSVG
from matplotlib.figure import Figure

import database
from database import CountryNotFoundException


def get_population_total_plot_for(country: str) -> Figure:
    query = f"""SELECT year,count FROM population_total WHERE country_name='{country}' LIMIT 100"""
    query_result = database.execute_query(query)
    print(query_result)
    if not query_result:
        raise CountryNotFoundException("Country not found")

    year, count = zip(*query_result)
    figure = Figure()

    axis = figure.add_subplot(1, 1, 1)
    axis.set_title(f"Population of {country}")
    axis.set_xlabel("Year")
    axis.set_ylabel("Population in Millions")
    axis.ticklabel_format(style="sci", scilimits=(6, 6), axis='y')
    axis.plot(year, count)

    return figure


def get_co2_emission_plot_for(country: str) -> Figure:
    query = f"""SELECT year,emission FROM co2_emission WHERE country_name='{country}' LIMIT 250"""
    query_result = database.execute_query(query)
    print(query_result)
    if not query_result:
        raise CountryNotFoundException("Country not found")

    year, emission = zip(*query_result)
    figure = Figure()

    axis = figure.add_subplot(1, 1, 1)
    axis.set_title(f"Emission of {country}")
    axis.set_xlabel("Year")
    axis.set_ylabel("Emission in tonnes")
    axis.ticklabel_format(style="sci", scilimits=(6, 6), axis='y')
    axis.plot(year, emission)

    return figure

    pass



def create_png(figure: Figure) -> bytes:
    output = io.BytesIO()
    FigureCanvasPNG(figure).print_png(output)
    return output.getvalue()


def create_svg(figure: Figure) -> bytes:
    output = io.BytesIO()
    FigureCanvasSVG(figure).print_svg(output)
    return output.getvalue()
