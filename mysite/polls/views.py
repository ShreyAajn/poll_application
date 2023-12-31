from typing import Any
from django.db import models
from django.utils import timezone
from django.http import *
from django.shortcuts import redirect, render
from django.views import generic
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .forms import UserCreationForm
from .models import Question, Choice, user_info


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))


# class IndexView(generic.ListView):
#     template_name = "polls/index.html"
#     context_object_name = "latest_question_list"

#     def get_queryset(self):
#         """Return the last five published questions."""
#         return Question.objects.order_by("-pub_date")[:5]


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_user_info_list"

    def get_queryset(self):
        return user_info.objects.all()


class UserInformationView(generic.DetailView):
    model = user_info
    template_name = "polls/user_information.html"


def create_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the user data to the database
            return redirect(
                "polls:index"
            )  # Redirect to the index page after user creation
    else:
        form = UserCreationForm()

    return render(request, "polls/create_user.html", {"form": form})
