from django.contrib import admin
from django.urls import path

from todo_app.views import TaskListView

urlpatterns = [
    path("", TaskListView.as_view(), name="home-page"),
]

app_name = "todo_app"