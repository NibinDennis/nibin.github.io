from django.shortcuts import render
from apiapp.models import Flights
from apiapp.serializers import FlightSerialigers
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage

# Create your views here.
@csrf_exempt
def index(request,id=0):
    if request.method == 'GET':
        flights = Flights.objects.all()
        new_data = FlightSerialigers(flights,many=True)
        return JsonResponse(new_data.data,safe=False)
    elif request.method == 'POST':
        flights = JSONParser().parse(request)
        flight_serializer = FlightSerialigers(data=flights)
        if flight_serializer.is_valid():
            flight_serializer.save()
            return JsonResponse("data added succefully",safe=False)
        return JsonResponse("data not added",safe=False)
    elif request.method == 'PUT':
        flights = JSONParser().parse(request)
        flight_data = Flights.objects.get(id=flights['id'])
        flight_serializer = FlightSerialigers(flight_data,data=flights)
        if flight_serializer.is_valid():
            flight_serializer.save()
            return JsonResponse("data updated succesfully",safe=False)
        return JsonResponse("data not updated",safe=False)
    elif request.method == 'DELETE':
        flight_data = Flights.objects.get(id=id)
        flight_data.delete()
        return JsonResponse("data is deleted",safe=False)
    
@csrf_exempt
def SAVEFILES(request):
    files = request.FILES['files']
    file_name = default_storage.save(files.name,files)
    return JsonResponse(file_name,safe=False)

             
         
       
   
    
