from django import forms
from .models import Participant, Match

class ParticipantForm(forms.ModelForm):
  class Meta:
    model = Participant
    fields = ["first_name", "last_name", "age", "reg_date",]
    labels = {'first_name': "firstname", "last_name": "lastname", "age": "age", "reg_date": "registration date",}

class MatchForm(forms.ModelForm):
  class Meta:
    model = Match
    fields = ["match_name", "match_date", "local", "visitor", "league", "score_local", "score_visitor",]
    labels = {"match_name": "match name", "match_date": "match date", "local": "local player", "visitor": "visitor player", "league": "Player's league", "score_local": "score local", "score_visitor": "score visitor",}
