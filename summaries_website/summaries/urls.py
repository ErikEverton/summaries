from django.urls import path
from summaries import views 

app_name = "summaries"
urlpatterns = [
    path("home/", views.HomeView.as_view(), name="home"),
    path("create-subject/", views.CreateSubject.as_view(), name="create-subject"),
]

