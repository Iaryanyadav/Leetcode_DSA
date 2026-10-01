WITH total AS (
    SELECT 
        user_id,
        COUNT(movie_id) AS movie_count
    FROM MovieRating
    GROUP BY user_id
),
ttl AS (
    SELECT 
        movie_id,
        AVG(rating) AS average_rating
    FROM MovieRating
    WHERE created_at >= '2020-02-01'
      AND created_at < '2020-03-01'
    GROUP BY movie_id
)

(
    SELECT u.name AS results
    FROM total t
    JOIN Users u
        ON t.user_id = u.user_id
    ORDER BY t.movie_count DESC, u.name ASC
    LIMIT 1
)

UNION all

(
    SELECT m.title AS results
    FROM ttl t
    JOIN Movies m
        ON t.movie_id = m.movie_id
    ORDER BY t.average_rating DESC, m.title ASC
    LIMIT 1
);