
SELECT P.project_id, ROUND(AVG(CAST(E.experience_years AS FLOAT)), 2) AS average_years
FROM Employee E
INNER JOIN Project P ON P.employee_id = E.employee_id
GROUP BY P.project_id;
