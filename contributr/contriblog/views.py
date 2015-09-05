from django.http import HttpResponse

def index(request):
    return HttpResponse("I am a blog.")
