-- Script to list all genres in the database hbtn_0d_tvshows_rate by their rating sum.
-- Each record displays: tv_genres.name - rating sum
-- Results sorted in descending order by their rating.
-- One SELECT statement only.
-- Database name passed as an argument in the mysql command.


SELECT tv_genres.name, SUM(tv_show_ratings.rate) AS rating
FROM tv_genres AS g
INNER JOIN tv_show_genres AS s ON s.genre_id = g.id
INNER JOIN tv_show_ratings AS r ON r.show_id = s.show_id
GROUP BY tv_genres.name
ORDER BY rating DESC;
