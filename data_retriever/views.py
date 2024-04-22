from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.decorators.http import require_POST
import requests
from .forms import DataRetrieverForm


class DataHome(TemplateView):
    template_name = "data_retriever/home.html"


@require_POST
def data_request(request):
    form = DataRetrieverForm(request.POST)
    if form.is_valid():
        form_data = form.cleaned_data
        json_data = get_json_data(form_data.get("league"), form_data.get("year"), form_data.get("week"))
        print("great thank you")
        return request
    
    print("uh oh")
    return request


def get_json_data(league, year, week):
    url = f"https://www.oddsshark.com/api/scores/football/{league.lower()}/{year}/s?_format=json"
    response = requests.get(url)

    if response.status_code != 200:
        return {}
    
    data = clean_json_data(response.json()["scores"])
    return 

def clean_json_data(data: dict):
    for game_id_str in data:
        game_id = data[game_id]["id"]
        schedule_date = data[game_id]["date"]
        status = data[game_id]["status"]
        home_team_abr = data[game_id]["teams"]["home"]["names"]["name"]
        home_team_spread = data[game_id]["teams"]["home"]["names"]["spread"]
        home_team_score = data[game_id]["teams"]["home"]["names"]["score"]
        home_team_record = data[game_id]["teams"]["home"]["names"]["record"]