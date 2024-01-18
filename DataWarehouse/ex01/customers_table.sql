-- Create a table called customers that contains all the data from the tables data_2022_oct, data_2022_nov, data_2022_dec, data_2023_jan, data_2023_feb.
CREATE TABLE IF NOT EXISTS customers AS (
    SELECT * FROM data_2022_oct
    UNION ALL
    SELECT * FROM data_2022_nov
    UNION ALL
    SELECT * FROM data_2022_dec
    UNION ALL
    SELECT * FROM data_2023_jan
    UNION ALL
    SELECT * FROM data_2023_feb
);