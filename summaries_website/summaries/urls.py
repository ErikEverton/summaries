from django.urls import path
from summaries import views 

app_name = "summaries"
urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("create-subject/", views.CreateSubject.as_view(), name="create-subject"),
    path("update-subject/<int:id>/", views.UpdateSubject.as_view(), name="update-subject"),
    path("create-summarie/", views.CreateSummarie.as_view(), name="create-summarie")
]

