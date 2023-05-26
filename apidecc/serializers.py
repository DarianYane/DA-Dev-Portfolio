from rest_framework import serializers
from .models import Job, Department, HiredEmployee

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('id', 'department')

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('id', 'job')

class HiredEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HiredEmployee
        fields = ('id', 'name', 'datetime', 'department_id', 'job_id')