from django.http import HttpResponse


def index(request):
    return HttpResponse("Prism certification service welcome page")
