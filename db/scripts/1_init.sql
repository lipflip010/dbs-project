CREATE TABLE population_total (
  Country_Name varchar(40),
  Year int,
  Count int,
   PRIMARY KEY(Country_Name, Year)
);

CREATE TABLE co2_emission (
  Country_Name varchar(80),
  Code varchar(10),
  Year int,
  Emission float,
   PRIMARY KEY(Country_Name, Year)
);

CREATE TABLE gdp (
  Country_Name varchar(80),
  Code varchar(10),
  Year int,
  Value float,
   PRIMARY KEY(Country_Name, Year)
);

CREATE VIEW co2_per_capita AS
SELECT pt.country_name  AS country_name,
       pt.year          AS year,
       emission / count AS emission_per_capita
FROM co2_emission co2
         INNER JOIN population_total pt
                    ON co2.country_name = pt.country_name
                        AND co2.year = pt.year
WHERE co2.year >= 1960
