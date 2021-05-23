-- Write your MySQL query statement below
select a.Name as Employee
FROM Employee AS a
inner join Employee AS b
WHERE a.ManagerId = b.Id AND a.Salary > b.Salary;
