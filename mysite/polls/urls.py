from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("polls/<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path("polls/<int:pk>/", views.detail, name="details"),
    path("in/<int:pk>/", views.UserInformationView.as_view(), name="user_info"),
    path("create_user/", views.create_user, name="create_user"),
]
