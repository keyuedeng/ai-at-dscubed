INSERT INTO project_two.employee (emp_id, name, salary, department, hire_date) VALUES
(1, 'John Doe', 50000, 'IT', '2021-01-01'),
(2, 'Jane Smith', 60000, 'HR', '2021-02-01'),
(3, 'Jim Beam', 70000, 'Sales', '2021-03-01'),
(4, 'Jill Johnson', 80000, 'Marketing', '2021-04-01'),
(5, 'Jack Daniels', 90000, 'Finance', '2021-05-01')
ON CONFLICT (emp_id) DO NOTHING;