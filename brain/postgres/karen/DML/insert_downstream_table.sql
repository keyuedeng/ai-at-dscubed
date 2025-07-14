INSERT INTO project_two.department_salary (department, total_salary)
SELECT department, SUM(salary) AS total_salary
FROM project_two.employee
GROUP BY department;