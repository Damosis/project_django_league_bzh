import datetime

from django.db import models
from django.utils import timezone

class Participant(models.Model):
    first_name = models.CharField(default='first name', max_length=30)
    last_name  = models.CharField(default='last name', max_length=30)
    age        = models.IntegerField(default=0)
    reg_date   = models.DateTimeField(default='1970-01-01 00:00:00')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class League(models.Model):
    league_name = models.CharField(default='default league name',max_length=30)

    def __str__(self):
        return self.league_name

# class Equipe:
#     ID: int #PK
#     nom: str
#     joueurs: Participant[]

class Match(models.Model):
    match_name  = models.CharField(default='match name',max_length=30)
    match_date  = models.DateTimeField(default='1970-01-01 00:00:00')
    local       = models.ForeignKey(Participant, on_delete=models.CASCADE, default=None, related_name="player1")
    visitor     = models.ForeignKey(Participant, on_delete=models.CASCADE, default=None, related_name="player2")
    league      = models.ForeignKey(League, on_delete=models.CASCADE, default=None, related_name="matchleague")
    score_local = models.IntegerField(default=0)
    score_visitor = models.IntegerField(default=0)

    def __str__(self):
        return self.match_name
    
