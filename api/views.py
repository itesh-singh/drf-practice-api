from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.
def studentsView(request):
    students = [
        {
            'id': 1,
            'name': 'John Doe',
            'age': 20,
            'grade': 'A'
        }
    ]
    return JsonResponse(students, safe=False)