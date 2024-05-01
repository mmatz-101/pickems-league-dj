from django.urls import path

from .views import HomePageView, AboutPageView, UserHomePage

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("<uuid:pk>/", UserHomePage.as_view(), name="user-homepage"),
]
