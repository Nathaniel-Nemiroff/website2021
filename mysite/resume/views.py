from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

#from .models import Question

def index(request):
    print('\n\n\n\n\n\n\n\nDEBUG: INSIDE resume.views\n\n\n\n\n\n\n\n')
    context = {}
    return render(request,'resume/index.html', context)
