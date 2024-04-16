SELECT (
    -- Select the second highest salary using a subquery
    SELECT DISTINCT Salary
      FROM Employee
     -- Order salaries in descending order
     ORDER BY Salary DESC
     -- Skip the first highest salary
     OFFSET 1
     -- Limit the result to just one row
     LIMIT 1
) AS SecondHighestSalary; 
