from django.urls import path
from .views import DataHome, data_request

urlpatterns = [
    path("", DataHome.as_view(), name="data-homepage"),
    path("gather-data/", data_request, name="gather-data")
]

