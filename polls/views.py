from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Choice, Question
# Create your views here.


def index(request):
    #seleciona as 5 primeiras as questions ordenadas do menor pro maior a data de publicação
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #contexto a ser enviado para a view
    context = {
        'latest_question_list': latest_question_list,
    }
    #forma resumida de retornar a view
    return render(request, 'polls/index.html', context)
    # return HttpResponse(template.render(context, request))


def detail(request, question_id):
    #get uma questão especifica ou da erro 404
    #try:
    #    question = Question.objects.get(pk=question_id)
    #except Question.DoesNotExist:
    #    raise Http404("Question does not exist")
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
    #return HttpResponse("You're looking at question %s." % question_id)

#identação de string
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        #reverse aponta para o nome da url
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
        
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})