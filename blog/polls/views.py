from django.shortcuts import render
from django.http import HttpResponse

from .models import Question

def index(request):
    lastest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'lastest_question_list': lastest_question_list,
    }
    return render(request, 'polls/index.html', context)

    return HttpResponse("Hello")

def detail(request, question_id):
    return HttpResponse(f"Question {question_id}")

def results(request, question_id):
    response = "You are looking at results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting on question %s" % question_id)