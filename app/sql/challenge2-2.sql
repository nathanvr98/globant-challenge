--List of ids, name and number of employees hired of each department that hired more
--employees than the mean of employees hired in 2021 for all the departments, ordered
--by the number of employees hired (descending).
SELECT
  d.department_id AS id,
  d.department_name AS department,
  COUNT(e.employee_id) AS hired
FROM
  departments d
JOIN
  employees e ON d.department_id = e.department_id
WHERE
  EXTRACT(YEAR FROM e.hire_date) = 2021
GROUP BY
  d.department_id, d.department_name
HAVING
  COUNT(e.employee_id) > (
    SELECT AVG(COUNT(e.employee_id))
    FROM departments d
    JOIN employees e ON d.department_id = e.department_id
    WHERE EXTRACT(YEAR FROM e.hire_date) = 2021
  )
ORDER BY
  hired DESC;