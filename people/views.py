from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from .models import Person, News, Departments
from .serializers import PersonSerializer, NewSerializer
from rest_framework.response import Response


def index(request):
    return render(request, 'people/oleg.html')

class PersonView(APIView):
    def get(self, request):
        p = Person.objects.all()
        return Response({'persons': PersonSerializer(p, many=True).data})

class NewsView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewSerializer
