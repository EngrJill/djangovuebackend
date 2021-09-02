from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view #Handles @api_view([HTTP REQUEST])
from rest_framework.response import Response
from .serializers import SubjectsSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import SearchFilter

from .models import Subjs

# Create your views here.

@api_view(['GET'])
def subjectDetail(request, id):
    tasks = Subjs.objects.get(id=id)
    serializer = SubjectsSerializer(tasks, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def subjectCreate(request):
    serializer = SubjectsSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def subjectUpdate(request, id):
    task = Subjs.objects.get(id=id)
    serializer = SubjectsSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def subjectDelete(request, id):
    task = Subjs.objects.get(id=id)
    task.delete()

    return Response("Item Successfully Deleted")

class subjectList(generics.ListAPIView):
    queryset = Subjs.objects.all()
    serializer_class = SubjectsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['course', 'year']