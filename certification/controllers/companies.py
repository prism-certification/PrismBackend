from rest_framework import generics
from certification.models import Company
from certification.serializers import CompanySerializer


class CompanyListOrCreate(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyDetailOperation(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
