from django.http import HttpResponse

def index(request):
    return HttpResponse("This is first view")

# Create your views here.
