-- lists all records of a table
SELECT score, name FROM second_table WHERE name IS NOT NULL OR name != '' ORDER BY score DESC;
