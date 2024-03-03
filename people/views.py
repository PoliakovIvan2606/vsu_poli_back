from django.shortcuts import render
from rest_framework.views import APIView
from .models import Person
from .serializers import PersonSerializer
from rest_framework.response import Response


def index(request):
    return render(request, 'people/oleg.html')

class PersonView(APIView):
    def get(self, request):
        p = Person.objects.all()
        return Response({'persons': PersonSerializer(p, many=True).data})