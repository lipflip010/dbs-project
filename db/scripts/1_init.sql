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