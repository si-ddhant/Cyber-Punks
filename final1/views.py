from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Table
from django.db.models import Count, Avg, Sum
from .serializers import TableSerializer
from rest_framework import viewsets
from django.http import HttpResponse


class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer


class RecordCountView(APIView):
    def get(self, request):
        # Calculate the total number of records
        count = Table.objects.count()
        return HttpResponse({'count': count})


class MeanSalaryView(APIView):
    def get(self, request):
        # Calculate the mean salary (You may need to adjust this based on your data structure)
        # mean_salary = Table.objects.aggregate(
        #     avg_salary=Avg('PREVAILING_WAGE'))['avg_salary']
        # return JsonResponse({'mean_salary': mean_salary})
        return HttpResponse(0)


class MedianSalaryView(APIView):
    def get(self, request):
        # Calculate the median salary (You may need to write custom SQL query for this)
        # Example: You can use `Table.objects.raw()` to execute a custom SQL query
        # and calculate the median
        median_salary = 0  # Replace with your custom logic
        
        return HttpResponse(0)
