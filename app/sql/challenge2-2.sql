--List of ids, name and number of employees hired of each department that hired more
--employees than the mean of employees hired in 2021 for all the departments, ordered
--by the number of employees hired (descending).
WITH department_hires AS (
    SELECT
        d.department_id,
        COUNT(e.employee_id) AS hired
    FROM departments d
    JOIN employees e ON d.department_id = e.department_id
    WHERE EXTRACT(YEAR FROM e.hire_date) = 2021
    GROUP BY d.department_id
),
average_hires AS (
    SELECT AVG(hired) AS avg_hired
    FROM department_hires
)
SELECT
    d.department_id,
    d.department_name,
    dh.hired
FROM departments d
JOIN department_hires dh ON d.department_id = dh.department_id
JOIN average_hires ah ON dh.hired > ah.avg_hired
ORDER BY dh.hired DESC;