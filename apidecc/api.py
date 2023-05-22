from apidecc.models import Job, Department, HiredEmployee
from rest_framework import viewsets, permissions
from .serializers import JobSerializer, DepartmentSerializer, HiredEmployeeSerializer

#for CSV import
import csv
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from rest_framework.decorators import action
from rest_framework.response import Response

fs = FileSystemStorage(location='tmp/')

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = DepartmentSerializer
    
    @action(detail=False, methods=['POST'])
    def upload_data(self, request):
        # The file is first stored and then read to populate the data.
        file = request.FILES["file"]
        content = file.read()
        # Create a ContentFile object with the file contents
        file_content = ContentFile(content)
        file_name = fs.save("tmp.csv", file_content)
        # Gets the path to the temporary file
        tmp_file = fs.path(file_name)
        # Open the CSV file
        csv_file = open(tmp_file, errors="ignore")
        reader = csv.reader(csv_file)
        next(reader) #Skip the first row (header)
        
        department_list = []
        for id_, row in enumerate(reader):
            # Read data from each row of the CSV file
            (department) = row
            department_list.append(Department(department=department[0]))
        # Creates Department objects in the database using bulk_create
        Department.objects.bulk_create(department_list)

        return Response("Successfully upload the data")

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = JobSerializer
    
    @action(detail=False, methods=['POST'])
    def upload_data(self, request):
        # The file is first stored and then read to populate the data.
        file = request.FILES["file"]
        content = file.read()
        # Create a ContentFile object with the file contents
        file_content = ContentFile(content)
        file_name = fs.save("tmp.csv", file_content)
        # Gets the path to the temporary file
        tmp_file = fs.path(file_name)
        # Open the CSV file
        csv_file = open(tmp_file, errors="ignore")
        reader = csv.reader(csv_file)
        next(reader) #Skip the first row (header)
        
        job_list = []
        for id_, row in enumerate(reader):
            # Read data from each row of the CSV file
            (job) = row
            job_list.append(Job(job=job[0]))
        # Creates Job objects in the database using bulk_create
        Job.objects.bulk_create(job_list)

        return Response("Successfully upload the data")

class HiredEmployeeViewSet(viewsets.ModelViewSet):
    queryset = HiredEmployee.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = HiredEmployeeSerializer
    
    @action(detail=False, methods=['POST'])
    def upload_data(self, request):
        # The file is first stored and then read to populate the data.
        file = request.FILES["file"]
        content = file.read()
        # Create a ContentFile object with the file contents
        file_content = ContentFile(content)
        file_name = fs.save("tmp.csv", file_content)
        # Gets the path to the temporary file
        tmp_file = fs.path(file_name)
        # Open the CSV file
        csv_file = open(tmp_file, errors="ignore")
        reader = csv.reader(csv_file)
        next(reader) #Skip the first row (header)
        
        hired_employee_list = []
        for id_, row in enumerate(reader):
            # Read data from each row of the CSV file
            (name, datetime, department, job) = row
            hired_employee_list.append(HiredEmployee(name=name, datetime=datetime, department_id=department, job_id=job))
        # Creates Job objects in the database using bulk_create
        HiredEmployee.objects.bulk_create(hired_employee_list)

        return Response("Successfully upload the data")