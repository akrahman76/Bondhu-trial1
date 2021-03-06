from django.urls import path
from . import views

urlpatterns = [
    path("", views.home,name="home"),
    path("prediction/", views.prediction,name="home"),
    path("addprofile/", views.addProfile,name="addProfile"),
    path("addprofile/success", views.home,name="home"),
    # path("allprofiles/", views.allprofiles,name="allprofiles"),
    path("history/<str:pk>", views.history,name="history"),
    path("home/", views.home,name="home"),
]