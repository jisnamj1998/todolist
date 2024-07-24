"""
URL configuration for ToDoList project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("todolist/create/",views.TodoListCreateView.as_view(),name="todolist-create"),
    path("todolist/<int:pk>/update/",views.TodoListUpdateView.as_view(),name="todolist-update"),
    path("todolist/<int:pk>/",views.TodoListDetailView.as_view(),name="todolist-detail"),
    path("todolist/<int:pk>/delete/",views.TodoListDeleteView.as_view(),name="todolist-delete"),
    path("register/",views.SignUpView.as_view(),name="register"),
    path("",views.SignInView.as_view(),name="signin"),
    path("logout/",views.SignOutView.as_view(),name="signout"),
]
