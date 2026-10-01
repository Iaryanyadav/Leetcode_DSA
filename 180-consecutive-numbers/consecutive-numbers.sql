WITH total AS (
    SELECT 
        id,
        num,
        LEAD(num) OVER (ORDER BY id) AS next_num,
        LEAD(num, 2) OVER (ORDER BY id) AS next_num2
    FROM Logs
)
SELECT DISTINCT num AS ConsecutiveNums
FROM total
WHERE num = next_num
  AND num = next_num2;