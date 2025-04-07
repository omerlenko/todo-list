from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from todo_app.models import Task, Tag


class TaskListView(ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "todo_app/homepage.html"

    def get_queryset(self):
        tasks = Task.objects.all().order_by("is_completed", "-datetime")
        return tasks


class TaskCreateView(CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo_app:home-page")


class TaskUpdateView(UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo_app:home-page")


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy("todo_app:home-page")


class TagListView(ListView):
    model = Tag
    context_object_name = "tags"
    template_name = "todo_app/tag_list.html"


class TagCreateView(CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_app:tag-list")


class TagUpdateView(UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_app:tag-list")


class TagDeleteView(DeleteView):
    model = Tag
    success_url = reverse_lazy("todo_app:tag-list")


def complete_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    if task.is_completed:
        task.is_completed = False
    else:
        task.is_completed = True
    task.save()

    return redirect("todo_app:home-page")
