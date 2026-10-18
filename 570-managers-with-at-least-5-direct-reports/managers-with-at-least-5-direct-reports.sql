# Write your MySQL query statement below
WITH ManagerCount AS(
    SELECT managerId, 
    COUNT(id) AS report_count
    FROM Employee
    WHERE managerId IS NOT NULL
    GROUP BY managerId
    HAVING count(id) >= 5

)
SELECT 
e.name
FROM Employee e
INNER JOIN ManagerCount m
ON e.id = m.managerId