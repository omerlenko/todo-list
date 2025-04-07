from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

from todo_app.models import Task, Tag


class TaskListView(ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "todo_app/homepage.html"


class TagListView(ListView):
    model = Tag
    context_object_name = "tags"
    template_name = "todo_app/tag_list.html"

def complete_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    if task.is_completed:
        task.is_completed = False
    else:
        task.is_completed = True
    task.save()

    return redirect("todo_app:home-page")




