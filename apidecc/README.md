# Human Resources API

This Human Resources API allows managing departments, job positions, and hired employees using Django REST Framework.

# Table of Contents
- [Setup](#setup)
- [Models](#models)
- [Endpoints](#endpoints)
  - [Importing data from CSV](#importing-data-from-csv)
  - [SQL Queries](#sql-queries)
- [Serializers](#serializers)
- [License](#license)

## Setup

1. Install Django REST Framework: `pip install djangorestframework`
2. Create the "apidecc" application: `python manage.py startapp apidecc`
3. Add "apidecc" and "rest_framework" to INSTALLED_APPS in your project's settings.py file.
4. Create migrations and apply them to the database: `python manage.py makemigrations` and `python manage.py migrate`.

## Models

The API has the following models:

- `Department`: represents a department in the company.
- `Job`: represents a job position in the company.
- `HiredEmployee`: represents a hired employee with their name, date and time of hiring, and associated department and job position.

## Endpoints

The API provides the following endpoints:

- `/apidecc/api/jobs/`: endpoint to manage job positions.
- `/apidecc/api/departments/`: endpoint to manage departments.
- `/apidecc/api/hired-employees/`: endpoint to manage hired employees.

### Importing data from CSV

For each model, an additional endpoint called `upload_data` is provided to import data from a CSV file.

- For job positions: `/apidecc/api/jobs/upload_data/`
- For departments: `/apidecc/api/departments/upload_data/`
- For hired employees: `/apidecc/api/hired-employees/upload_data/`

It is expected to send a CSV file named "file" in the POST request to import the corresponding data.

### SQL Queries

1) Number of employees hired for each job and department divided by quarter. The table must be ordered alphabetically by department and job.

Solution:

SELECT<br>
    apidecc_hiredemployee.department,<br>
    apidecc_hiredemployee.job,<br>
    EXTRACT(QUARTER FROM apidecc_hiredemployee.datetime) AS quarter,<br>
    COUNT(apidecc_hiredemployee.id) AS count<br>
FROM<br>
    apidecc_hiredemployee<br>
GROUP BY<br>
    apidecc_hiredemployee.department,<br>
    apidecc_hiredemployee.job,<br>
    quarter<br>
ORDER BY<br>
    apidecc_hiredemployee.department,<br>
    apidecc_hiredemployee.job;<br>

- in table format: `/apidecc/api/hired-employees/employees_by_job_department_quarter_on_table/`
- in API format:`/apidecc/api/hired-employees/employees_by_job_department_quarter_json/?format=api`
- in JSON format:`/apidecc/api/hired-employees/employees_by_job_department_quarter_json/?format=json`

2) List of ids, name and number of employees hired of each department that hired more employees than the mean of employees hired for all the departments, ordered by the number of employees hired (descending).

Solution:

SELECT <br>
    d.id, <br>
    d.department, <br>
    COUNT(he.id) as num_hires<br>
FROM <br>
    apidecc_department d<br>
INNER JOIN <br>
    apidecc_hiredemployee he ON d.id = he.department_id<br>
WHERE <br>
    he.datetime >= '2021-01-01' AND he.datetime < '2022-01-01'<br>
GROUP BY <br>
    d.id, d.department<br>
HAVING COUNT(he.id) > (<br>
    SELECT AVG(num_hires) as mean_hires<br>
    FROM (<br>
        SELECT COUNT(id) as num_hires<br>
        FROM apidecc_hiredemployee<br>
        WHERE datetime >= '2021-01-01' AND datetime < '2022-01-01'<br>
        GROUP BY department_id<br>
    ) as subquery<br>
)<br>
ORDER BY num_hires DESC<br>

- in table format: `/apidecc/api/departments/departments_hiring_above_mean_on_table/?format=api`
- in API format:`/apidecc/api/departments/departments_hiring_above_mean_json/?format=api`
- in JSON format:`/apidecc/api/departments/departments_hiring_above_mean_json/?format=json`

## Serializers

The following serializers are defined to convert the models to JSON format:

- `JobSerializer`
- `DepartmentSerializer`
- `HiredEmployeeSerializer`

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
