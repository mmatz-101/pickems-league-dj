from django.views.generic import TemplateView
from django.shortcuts import redirect


class HomePageView(TemplateView):
    template_name = "pages/home.html"


class AboutPageView(TemplateView):
    template_name = "pages/about.html"


class UserHomePage(TemplateView):
    template_name = "pages/user.html"
