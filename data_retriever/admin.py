from django.contrib import admin
from .models import Game


class GameAdmin(admin.ModelAdmin):
    list_display = [
        "home_team_name",
        "away_team_name",
        "schedule_date",
        "league",
        "week",
    ]
    search_fields = [
        "home_team_name",
        "away_team_name",
        "schedule_date",
        "league",
        "week",
    ]
    list_filter = [
        "schedule_date",
        "league",
        "week",
    ]


admin.site.register(Game, GameAdmin)
