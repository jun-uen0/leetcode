SELECT subordinate.name AS "Employee"
FROM Employee subordinate
JOIN Employee manager
    ON subordinate.managerId = manager.id
WHERE subordinate.salary > manager.salary;