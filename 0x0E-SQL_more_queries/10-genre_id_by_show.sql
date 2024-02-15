/*
  - Import the database dump from hbtn_0d_tvshows to your MySQL server: download
  - Script to list all shows in hbtn_0d_tvshows with at least one linked genre.
  - Each record displays: tv_shows.title - tv_show_genres.genre_id
  - Results sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
  - One SELECT statement only.
  - Database name passed as an argument in the mysql command.
*/

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
