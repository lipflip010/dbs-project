COPY population_total FROM '/data/population_total.csv' DELIMITER ',' CSV HEADER;
COPY co2_emission FROM '/data/co2_emission.csv' DELIMITER ',' CSV HEADER;
COPY gdp FROM '/data/gdp_formatiert.csv' DELIMITER ',' CSV HEADER;
COPY population_growth FROM '/data/population_growth_formatiert.csv' DELIMITER ',' CSV HEADER;
COPY renewable_energy_consumption FROM '/data/renewable_energy_consumption.csv' DELIMITER ',' CSV HEADER;