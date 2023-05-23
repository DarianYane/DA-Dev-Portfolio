# Human Resources API

This Human Resources API allows managing departments, job positions, and hired employees using Django REST Framework.

# Table of Contents
- [Setup](#setup)
- [Models](#models)
- [Endpoints](#endpoints)
  - [Importing data from CSV](#importing-data-from-csv)
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

- `/api/jobs/`: endpoint to manage job positions.
- `/api/departments/`: endpoint to manage departments.
- `/api/hired-employees/`: endpoint to manage hired employees.

### Importing data from CSV

For each model, an additional endpoint called `upload_data` is provided to import data from a CSV file.

- For job positions: `/api/jobs/upload_data/`
- For departments: `/api/departments/upload_data/`
- For hired employees: `/api/hired-employees/upload_data/`

It is expected to send a CSV file with the "file" field in the POST request to import the corresponding data.

## Serializers

The following serializers are defined to convert the models to JSON format:

- `JobSerializer`
- `DepartmentSerializer`
- `HiredEmployeeSerializer`

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
