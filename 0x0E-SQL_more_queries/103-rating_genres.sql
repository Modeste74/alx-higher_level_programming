-- lists all genre by ratings

SELECT tv_genres.name, rating_sum
FROM tv_genres
LEFT JOIN (
	SELECT show_id, SUM(rate) AS rating_sum
	FROM tv_show_ratings
	GROUP BY show_id
) AS subquery
ON tv_genres.id = subquery.show_id
ORDER BY rating DESC;
