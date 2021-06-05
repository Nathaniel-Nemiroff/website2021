from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import Question

def index(request):
    return render(request,'polls/index.html')   

def example(request, question_id):
    #template = loader.get_template('polls/example.html')
    qu = Question.objects.get(id=question_id)
    context = {'qu' : qu}
    #return HttpResponse(template.render(context, request))
    return render(request, 'polls/example.html', context)
