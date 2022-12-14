from django.contrib import admin

from .models import Participant, League, Match

admin.site.register(Participant)
admin.site.register(League)
admin.site.register(Match)
