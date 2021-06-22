import io
from multiprocessing import Lock

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvasPNG
from matplotlib.backends.backend_svg import FigureCanvasSVG
from matplotlib.figure import Figure

import database


class PlotCreator:
    mutex = Lock()

    @staticmethod
    def get_population_total_plot_for(country: str) -> Figure:
        query = f"""SELECT year,count FROM population_total WHERE country_name='{country}' LIMIT 100"""
        query_result = database.execute_query(query)

        year, count = zip(*query_result)
        figure = Figure()

        axis = figure.add_subplot(1, 1, 1)
        axis.set_title(f"Population of {country}")
        axis.set_xlabel("Year")
        axis.set_ylabel("Population in millions")
        axis.ticklabel_format(style="sci", scilimits=(6, 6), axis='y')
        axis.plot(year, count)

        return figure

    @staticmethod
    def get_co2_emission_plot_for(country: str) -> Figure:
        query = f"""SELECT year,emission FROM co2_emission WHERE country_name='{country}' AND year>=1960 LIMIT 250"""
        query_result = database.execute_query(query)

        year, emission = zip(*query_result)
        figure = Figure()

        axis = figure.add_subplot(1, 1, 1)
        axis.set_title(f"Emission of {country}")
        axis.set_xlabel("Year")
        axis.set_ylabel("Emission in million tonnes")
        axis.ticklabel_format(style="sci", scilimits=(6, 6), axis='y')
        axis.plot(year, emission)

        return figure

    def create_png(self, figure: Figure) -> bytes:
        with self.mutex:
            output = io.BytesIO()
            FigureCanvasPNG(figure).print_png(output)
            return output.getvalue()

    def create_svg(self, figure: Figure) -> bytes:
        with self.mutex:
            output = io.BytesIO()
            FigureCanvasSVG(figure).print_svg(output)
            return output.getvalue()
