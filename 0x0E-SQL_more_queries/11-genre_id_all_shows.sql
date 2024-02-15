-- Script to list all shows in the database hbtn_0d_tvshows.
-- Each record displays: tv_shows.title - tv_show_genres.genre_id
-- Results sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- Display NULL if a show doesn’t have a genre.
-- One SELECT statement only.
-- Database name passed as an argument in the mysql command.


SELECT R.`title`, g.`genre_id`
FROM `tv_shows` AS R
LEFT JOIN `tv_show_genres` AS g
ON R.`id` = g.`show_id`
ORDER BY R.`title`, g.`genre_id`;
 
