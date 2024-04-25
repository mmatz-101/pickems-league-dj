from django.views.generic import TemplateView
from django.http import HttpResponse


class HomePageView(TemplateView):
    template_name = "pages/home.html"


class AboutPageView(TemplateView):
    template_name = "pages/about.html"


def user_page(request):
    return HttpResponse(f"{request.user} Landing Page")
