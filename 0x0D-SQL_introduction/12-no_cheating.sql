 -- Script to update Bob's score to 10 in 'second_table'.
 -- Only Bob's name field will be used; his id value cannot be utilized.
 -- Database name will be provided as an argument in the mysql command
UPDATE second_table SET score = 10 WHERE name = 'Bob';
