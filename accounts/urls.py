from django.urls import path

from .views import redirect_login



urlpatterns = [
    path("redirect-login/", redirect_login, name="redirect-login"),
]

