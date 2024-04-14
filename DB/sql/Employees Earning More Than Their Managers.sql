SELECT E.name AS Employee
FROM Employee AS MGR, Employee AS E
WHERE MGR.id = E.managerId AND E.salary > MGR.salary
