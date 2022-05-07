from django.shortcuts import render
from.models import Question
# Create your views here.

def polls_list(request):
    poll = Question.objects.all()

    return render(request,
                  'my_polls/question.html',
                  {'poll': poll})