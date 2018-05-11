from rest_framework import generics
from certification.models import Person
from certification.serializers import PersonSerializer


class PersonListOrCreate(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonDetailOperation(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
