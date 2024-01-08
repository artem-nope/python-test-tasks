from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    # ref to manager
    data = Language.objects.all()
    context = {
        'object_list': data
    }
    return render(
        request,
        template_name="languages/index.html",
        context=context
    )


def language_detail(request, pk):
    language = Language.objects.get(id__exact=pk)
    context = {
        'object': language
    }
    return render(
        request,
        template_name="languages/language_detail.html",
        context=context
    )

