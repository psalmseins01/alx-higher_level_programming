-- Retrieves all cities located in California from the 'hbtn_0d_usa' database.
-- Orders the results by the 'id' column of the 'cities' table in ascending order

SELECT `id`, `name`
FROM `cities` WHERE `state_id` IN (
	SELECT `id`
	FROM `states`
	WHERE `name` = "California")
 ORDER BY `id`;
 
