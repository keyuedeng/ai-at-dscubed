CREATE SCHEMA IF NOT EXISTS project_two;

CREATE TABLE IF NOT EXISTS project_two.employee (
    emp_id INT PRIMARY KEY, 
    name VARCHAR(255) NOT NULL,
    salary INT NOT NULL,
    department VARCHAR(255) NOT NULL,
    hire_date DATE NOT NULL
);

