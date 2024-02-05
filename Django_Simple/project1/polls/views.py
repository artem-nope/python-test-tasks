from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Count, Sum
from . import models


# Create your views here.
def index(request):
    context = {
        'latest_question_list': models.Question.objects.order_by('-created')[:5],
        'most_viewed_question_list': models.Question.objects.order_by('-views')[:5],
        'most_answered_question_list': models.Question.objects.annotate(number_of_answers=Count('answers'))
                                       .order_by('-number_of_answers')[:5],
        'most_voted_question_list': models.Question.objects.annotate(sum_of_votes=Sum('answers__votes'))
                                       .order_by('-sum_of_votes')[:5],
    }
    return render(
        request,
        template_name='polls/index.html',
        context=context
    )


def question_detail(request, pk):
    question = models.Question.objects.get(id__exact=pk)
    question.views += 1
    question.save()
    context = {
        'object': question,
    }
    return render(
        request,
        template_name='polls/question_detail.html',
        context=context
    )


def question_vote(request, pk):
    if request.method == 'POST':
        answer_id = request.POST.get('answer-id')
        print(answer_id)
        if answer_id:
            answer = models.Answer.objects.get(id__exact=answer_id)
            print(answer)
            answer.votes += 1
            answer.save()
            return HttpResponseRedirect(
                reverse('polls:question-results', args=[pk])
            )
        else:
            context = {
                'object': models.Question.objects.get(id__exact=pk),
                'message': 'You must select one answer!'
            }
            return render(
                request,
                template_name='polls/question_detail.html',
                context=context
            )


def question_results(request, pk):
    question = models.Question.objects.get(id__exact=pk)
    context = {
        'object': question,
    }
    return render(
        request,
        template_name='polls/question_results.html',
        context=context
    )


def add_question_answer(request, pk):
    # INSERT
    # INTO
    # polls_answer(text, votes, question_id)
    # VALUES("Some text", 0, 1)
    if request.method == 'POST':
        question = models.Question.objects.get(id__exact=pk)
        new_answer_text = request.POST.get('new-answer')
        if new_answer_text:
            # 1
            # new_answer = models.Answer.objects.create(text=new_answer_text, question=question)
            # 2
            new_answer = models.Answer(text=new_answer_text, question=question)
            new_answer.save()
        return HttpResponseRedirect(
            reverse('polls:question-results', kwargs={
                'pk': pk
            })
        )


def new_answer(request, pk):
    question = models.Question.objects.get(id__exact=pk)
    context = {
        'object': question
    }
    return render(
        request,
        template_name='polls/add_questions_answer.html',
        context=context
    )