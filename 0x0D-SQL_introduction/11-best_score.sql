-- Script to list all records with a score >= 10
-- in the 'second_table' of database 'hbtn_0c_0' in MySQL server
-- Results display both the score and the name (in this order)
-- Records are ordered by score (top first).
-- Database name will be passed as an argument in the mysql command
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
