from django.shortcuts import render, HttpResponse

# Create your views here.
def homepage(request):
    return render(request, 'store/index.html')