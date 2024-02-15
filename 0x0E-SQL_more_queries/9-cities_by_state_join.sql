-- Retrieves all cities from the 'hbtn_0d_usa' database
-- Sorts the records by the 'id' column of the 'cities' table in ascending order

SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states ON cities.state_id = states.id
ORDER BY cities.id; 
