from django.urls import path
from apiapp import views

urlpatterns = [
    path('',views.index),
    path('<int:id>/',views.index),
    path('savefile/',views.SAVEFILES)
]