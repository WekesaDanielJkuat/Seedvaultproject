from django.shortcuts import render

# Create your views here.
#creating a simple API endpoint
# api/views.py

from django.http import JsonResponse

def hello(request):
    return JsonResponse({'message': 'Hello from Django API!'})
