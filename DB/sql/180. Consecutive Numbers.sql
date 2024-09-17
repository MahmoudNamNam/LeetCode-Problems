SELECT DISTINCT num [ConsecutiveNums]
FROM (
    SELECT num,
           LAG(num) OVER (ORDER BY id) AS prev_num,
           LEAD(num) OVER (ORDER BY id) AS next_num
    FROM logs
) t
WHERE num = prev_num AND num = next_num;
