from django.urls import path

from .views import HomePageView, AboutPageView, user_page

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("<uuid:pk>", user_page, name="user-page"),
]
