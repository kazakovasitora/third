from django.shortcuts import render

# Create your views here.

def html_template(request):
    return render(request, 'index.html')