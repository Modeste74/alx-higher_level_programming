-- imports database dump to mysql server
-- list all shows in the database
-- displays 2 fields
-- uses SELECT once

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id =tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
