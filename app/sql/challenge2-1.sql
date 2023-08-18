-- Number of employees hired for each job and department in 2021 divided by quarter and ordered alphabetically by department and job.
SELECT
    d.department_name,
    j.job_title,
    SUM(CASE WHEN EXTRACT(QUARTER FROM e.hire_date) = 1 THEN 1 ELSE 0 END) AS Q1,
    SUM(CASE WHEN EXTRACT(QUARTER FROM e.hire_date) = 2 THEN 1 ELSE 0 END) AS Q2,
    SUM(CASE WHEN EXTRACT(QUARTER FROM e.hire_date) = 3 THEN 1 ELSE 0 END) AS Q3,
    SUM(CASE WHEN EXTRACT(QUARTER FROM e.hire_date) = 4 THEN 1 ELSE 0 END) AS Q4
FROM
    departments d
JOIN
    employees e ON d.department_id = e.department_id
JOIN
    jobs j ON e.job_id = j.job_id
WHERE
    EXTRACT(YEAR FROM e.hire_date) = 2021
GROUP BY
    d.department_name,
    j.job_title
ORDER BY
    d.department_name,
    j.job_title;
