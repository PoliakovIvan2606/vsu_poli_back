from rest_framework.views import APIView
from .models import Person
from .serializers import PersonSerializer
from rest_framework.response import Response

class PersonView(APIView):
    def get(self, request):
        p = Person.objects.all()
        return Response({'persons': PersonSerializer(p, many=True).data})