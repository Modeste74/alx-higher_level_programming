-- lists all genre by ratings

--SELECT tv_genres.name, SUM(tv_show_ratings.rate) AS rating
--FROM tv_genres
--JOIN tv_show_genres ON tv_genres.id = tv_show_genres.show_id
--JOIN tv_show_ratings ON tv_show_genres.show_id = tv_show_ratings.show_id
--GROUP BY tv_genres.id
SELECT tv_genres.name, rating_sum
FROM tv_genres
LEFT JOIN (
	SELECT show_id, SUM(rate) AS rating_sum
	FROM tv_show_ratings
	GROUP BY show_id
) AS subquery
ON tv_genres.id = subquery.show_id
ORDER BY rating DESC;
