from django.shortcuts import render

# Create your views here.

def index(request):
    #just returns a request object to template
    return render(request, 'job/index.html')
