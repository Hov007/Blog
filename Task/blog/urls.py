from django.urls import path

from . import views
# We are creating separate urls.py to give routs to our particular app
urlpatterns = [
    path("", views.index, name="index"),
    path("newyear/", views.newyear, name="newyear"),
    path("add/", views.add, name="add"),
    path('<str:name>/', views.greet, name="greet")
]