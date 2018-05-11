from django.urls import path
from certification import controllers

urlpatterns = [
    path('companies', controllers.companies.CompanyListOrCreate.as_view()),
    path('companies/<int:pk>', controllers.companies.CompanyDetailOperation.as_view()),
    path('persons', controllers.persons.PersonListOrCreate.as_view()),
    path('persons/<int:pk>', controllers.persons.PersonDetailOperation.as_view()),
]