from django.db import models
from .constants import LEAGUE_CHOICES


class Game(models.Model):
    """
    Game is each individual game created
    """

    game_id = models.IntegerField(primary_key=True, null=False)
    schedule_date = models.DateTimeField(null=False)
    status = models.CharField(max_length=200)
    tv_station = models.CharField(max_length=200)
    week = models.IntegerField()
    league = models.CharField(choices=LEAGUE_CHOICES)
    home_team_name = models.CharField(max_length=200)
    home_team_spread = models.FloatField()
    home_team_score = models.IntegerField()
    home_team_record = models.CharField(max_length=200)
    away_team_name = models.CharField(max_length=200)
    away_team_spread = models.FloatField()
    away_team_score = models.IntegerField()
    away_team_record = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f"{self.home_team_name} v. {self.away_team_name}"
