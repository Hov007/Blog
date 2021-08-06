from django.urls import path

from . import views

# We are creating separate urls.py to give routs to our particular app
urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.register, name="register"),
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("home", views.home, name="home"),
    path("home/<int:post_id>/", views.viewPost, name="view"),
    path("add/", views.addPost, name="add"),
    path("myposts/", views.myPost, name="myposts"),
    path("myposts/<int:post_id>/", views.edit, name="edit"),

]