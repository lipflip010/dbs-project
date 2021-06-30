CREATE TABLE population_total (
  country_name varchar(40),
  year int,
  count int,
   PRIMARY KEY(country_Name, year)
);

CREATE TABLE population_growth (
  country_name varchar(80),
  country_code varchar(10),
  year int,
  growth_percentage float,
   PRIMARY KEY(country_Name, year)
);

CREATE TABLE co2_emission (
  country_name varchar(80),
  code varchar(10),
  year int,
  emission float,
   PRIMARY KEY(country_Name, year)
);

CREATE TABLE gdp (
  country_name varchar(80),
  country_code varchar(10),
  year int,
  usd float,
   PRIMARY KEY(country_name, year)
);

CREATE TABLE renewable_energy_consumption (
  country_name varchar(80),
  country_code varchar(10),
  year int,
  percentage_of_total float,
   PRIMARY KEY(country_name, year)
);

CREATE VIEW co2_per_capita AS
SELECT pt.country_name  AS country_name,
       pt.year          AS year,
       emission / count AS emission_per_capita
FROM co2_emission co2
         INNER JOIN population_total pt
                    ON co2.country_name = pt.country_name
                        AND co2.year = pt.year;



CREATE VIEW gdp_per_capita AS
SELECT pt.country_name  AS country_name,
       pt.year          AS year,
       usd / count AS usd_per_capita
FROM gdp
INNER JOIN population_total pt
ON gdp.country_name = pt.country_name
AND gdp.year = pt.year