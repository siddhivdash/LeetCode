# Write your MySQL query statement below
WITH Boarding AS(
    SELECT
        person_name,
        SUM(weight) OVER(ORDER BY turn ASC) AS runningweight
    FROM Queue
)
SELECT
    person_name
FROM Boarding
WHERE runningweight <= 1000
ORDER BY runningweight DESC
LIMIT 1