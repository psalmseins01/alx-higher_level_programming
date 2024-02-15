-- Script to list all shows from hbtn_0d_tvshows_rate by their rating sum.
-- Each record displays: tv_shows.title - rating sum
-- Results sorted in descending order by the rating.
-- One SELECT statement only.
-- Database name passed as an argument in the mysql command

SELECT `title`, SUM(`rate`) AS `rating`
FROM `tv_shows` AS s
INNER JOIN `tv_show_ratings` AS t
ON s.`id` = t.`show_id`
GROUP BY `title`
ORDER BY `rating` DESC;
 
