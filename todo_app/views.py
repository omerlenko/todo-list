from django.shortcuts import render
from django.views.generic import ListView

from todo_app.models import Task


class TaskListView(ListView):
    model = Task
    template_name = "todo_app/homepage.html"

