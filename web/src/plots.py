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
        query = f"""SELECT year,count FROM population_total WHERE country_name='{country}'"""
        query_result = database.execute_query(query)

        year, count = zip(*query_result)
        figure = Figure()

        axis = figure.add_subplot(1, 1, 1)
        axis.set_title(f"Population of {country}")
        axis.set_xlabel("Year")
        axis.set_ylabel("Population in millions")
        axis.ticklabel_format(style="sci", scilimits=(6, 6), axis='y')
        axis.yaxis.get_offset_text().set_visible(False)
        axis.plot(year, count)

        return figure

    @staticmethod
    def get_co2_emission_plot_for(country: str) -> Figure:
        query = f"""SELECT year,emission FROM co2_emission WHERE country_name='{country}'"""
        query_result = database.execute_query(query)

        year, emission = zip(*query_result)
        figure = Figure()

        axis = figure.add_subplot(1, 1, 1)
        axis.set_title(f"Emission of {country}")
        axis.set_xlabel("Year")
        axis.set_ylabel("Emission in million tonnes")
        axis.ticklabel_format(style="sci", scilimits=(6, 6), axis='y')
        axis.yaxis.get_offset_text().set_visible(False)
        axis.plot(year, emission)

        return figure

    @staticmethod
    def get_renewable_energy_plot_for(country: str) -> Figure:
        query = f"""SELECT year,percentage_of_total FROM renewable_energy_consumption WHERE country_name='{country}'"""
        query_result = database.execute_query(query)

        year, percentage_of_total = zip(*query_result)
        figure = Figure()

        axis = figure.add_subplot(1, 1, 1)
        axis.set_title(f"Renewable energy consumption of {country}")
        axis.set_xlabel("Year")
        axis.set_ylabel("% of total consumption")
        axis.ticklabel_format(style='plain', axis='y')
        axis.plot(year, percentage_of_total)

        return figure

    @staticmethod
    def get_gdp_plot_for(country: str) -> Figure:
        query = f"""SELECT year,usd FROM gdp WHERE country_name='{country}'"""
        query_result = database.execute_query(query)

        year, usd = zip(*query_result)
        figure = Figure()

        axis = figure.add_subplot(1, 1, 1)
        axis.set_title(f"GDP of {country}")
        axis.set_xlabel("Year")
        axis.set_ylabel("GDP in billion USD")
        axis.ticklabel_format(style="sci", scilimits=(9, 9), axis='y')
        axis.yaxis.get_offset_text().set_visible(False)
        axis.plot(year, usd)

        return figure

    @staticmethod
    def get_gdp_per_capita_plot_for(country: str) -> Figure:
        query = f"""SELECT year, usd_per_capita FROM gdp_per_capita WHERE country_name='{country}'"""
        query_result = database.execute_query(query)

        year, usd_per_capita = zip(*query_result)
        figure = Figure()

        axis = figure.add_subplot(1, 1, 1)
        axis.set_title(f"GDP per capita of {country}")
        axis.set_xlabel("Year")
        axis.set_ylabel("GDP per capita in US$")
        axis.ticklabel_format(style='plain', axis='y')
        axis.plot(year, usd_per_capita)

        return figure

    @staticmethod
    def get_co2_per_capita_plot_for(country: str) -> Figure:
        query = f"""SELECT year, emission_per_capita FROM co2_per_capita WHERE country_name='{country}'"""
        query_result = database.execute_query(query)

        year, emission_per_capita = zip(*query_result)
        figure = Figure()

        axis = figure.add_subplot(1, 1, 1)
        axis.set_title(f"Emission per capita of {country}")
        axis.set_xlabel("Year")
        axis.set_ylabel("Emission per capita in tonnes")
        axis.ticklabel_format(style='plain', axis='y')
        axis.plot(year, emission_per_capita)

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
