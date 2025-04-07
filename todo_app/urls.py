from django.contrib import admin
from django.urls import path

from todo_app.views import TaskListView, TagListView, complete_task

urlpatterns = [
    path("", TaskListView.as_view(), name="home-page"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("<int:pk>/complete/", complete_task, name="task-complete"),
]

app_name = "todo_app"