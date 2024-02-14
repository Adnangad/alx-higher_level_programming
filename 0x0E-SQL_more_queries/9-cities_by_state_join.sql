-- uses join to combine 2 rows of a table
SELECT cities.id, cities.name FROM cities LEFT JOIN states ON states.id = cities.state_id ORDER BY cities.id ASC;
