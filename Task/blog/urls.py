from django.urls import path

from . import views
# We are creating separate urls.py to give routs to our particular app
urlpatterns = [
    path("", views.index, name="index"),
    path("hov/", views.hov, name="hov"),
    path('<str:name>/', views.greet, name="greet")
]