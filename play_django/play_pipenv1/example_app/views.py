from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from django.template import loader

from .models import Question, Choice

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join(q.question_text for q in latest_question_list)
    template = loader.get_template('example/index.html')  # changed
    context = {
        'latest_question_list': latest_question_list
    }
    return render(request, 'example/index.html', context)

def detail(request, question_id):
    # response = f"You're looking at question {question_id}."
    # return HttpResponse(response)
    # question = Question.objects.get(pk=question_id)
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'example/detail.html', {'question': question})
    # pk stands for primary key, important

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'example/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        # request.POST is the name of Django's parsed dictionary/etc.
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'example/detail.html', {
            'question': question,
            'error_message': 'no choice entered!! doof!',
        })

    selected_choice.votes += 1
    selected_choice.save()
    return HttpResponseRedirect(reverse('example:results', args=[question.id]))