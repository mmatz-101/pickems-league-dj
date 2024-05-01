from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from pytz import timezone
import requests
import datetime

from .forms import DataRetrieverForm
from .models import Game


class DataHome(TemplateView):
    template_name = "data_retriever/home.html"


@require_POST
def data_request(request):
    form = DataRetrieverForm(request.POST)
    if form.is_valid():
        form_data = form.cleaned_data
        data = get_data(
            form_data.get("league"),
            form_data.get("year"),
            form_data.get("week_query"),
            form_data.get("week"),
        )
        if data == {}:
            return HttpResponse("error")
        save_game_data(data)
        return HttpResponse("Success")

    return HttpResponse("Unable to parse form data.")


def get_data(league, year, week_query, week) -> list[Game]:
    if league == "ncaa":
        url = f"https://www.oddsshark.com/api/scores/football/ncaaf/{year}/{week_query}?_format=json"
    else:
        url = f"https://www.oddsshark.com/api/scores/football/{league.lower()}/{year}/{week_query}?_format=json"
    response = requests.get(url)

    if response.status_code != 200:
        return {}

    data = clean_json_data(response.json()["scores"], week, league)
    return data


def clean_json_data(data: dict, week, league) -> list[Game]:
    """
    Parse the raw json data from the betting website. Returning a list of Game models.
    """
    game_list = []
    for game_id_str in data:
        game_id = data[game_id_str]["id"]
        schedule_date = data[game_id_str]["date"]
        status = data[game_id_str]["status"]
        tv_station = data[game_id_str]["tvStation"]
        home_team_name = data[game_id_str]["teams"]["home"]["names"]["name"]
        home_team_spread = data[game_id_str]["teams"]["home"]["spread"]
        home_team_score = data[game_id_str]["teams"]["home"]["score"]
        home_team_record = data[game_id_str]["teams"]["home"]["record"]
        away_team_name = data[game_id_str]["teams"]["away"]["names"]["name"]
        away_team_spread = data[game_id_str]["teams"]["away"]["spread"]
        away_team_score = data[game_id_str]["teams"]["away"]["score"]
        away_team_record = data[game_id_str]["teams"]["away"]["record"]

        # TODO: fix timezone
        # convert schedule_date
        schedule_date = datetime.datetime.fromtimestamp(schedule_date)
        eastern_datetime = timezone("US/Eastern").localize(schedule_date)

        game = Game(
            game_id=game_id,
            schedule_date=eastern_datetime,
            status=status,
            tv_station=tv_station,
            week=week,
            league=league,
            home_team_name=home_team_name,
            home_team_spread=home_team_spread,
            home_team_score=home_team_score,
            home_team_record=home_team_record,
            away_team_name=away_team_name,
            away_team_spread=away_team_spread,
            away_team_score=away_team_score,
            away_team_record=away_team_record,
        )

        game_list.append(game)

    return game_list


def save_game_data(data: list[Game]) -> None:
    for game in data:
        game.save()
