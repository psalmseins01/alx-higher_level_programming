-- Lists records of 'second_table' in 'hbtn_0c_0' with names
-- Displays score and name. Ordered by score
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
