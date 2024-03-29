from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Participant, Match, League
from .forms import ParticipantForm, MatchForm

def index(request):
    participant_list = Participant.objects.order_by('-reg_date')
    context = {'participant_list': participant_list}
    return render(request, 'league_bzh/index.html', context)

def detail(request, participant_id):
    try:
        participant = Participant.objects.get(pk=participant_id)
    except Participant.DoesNotExist:
        raise Http404("participant does not exist")
    return render(request, 'league_bzh/detail.html', {'participant': participant})

def register(request):
  if request.method == "POST":
    form = ParticipantForm(request.POST)
    if form.is_valid():
      form.save()
  else:
      form = ParticipantForm()
  return render(request, 'league_bzh/participant-form.html', {'form': form})

def add_match(request):
  if request.method == "POST":
    form = MatchForm(request.POST)
    if form.is_valid():
      form.save()
  else:
      form = MatchForm()
  return render(request, 'league_bzh/match-form.html', {'form': form})

def matches(request):
    matches_list = Match.objects.order_by('-match_date')
    context = {'matches_list': matches_list}
    return render(request, 'league_bzh/matches.html', context)

def rank(request, league_id):
    try:
        #matchs = Match.objects.all()
        matchs = Match.objects.filter(league=league_id)
        participants = Participant.objects.all()
        participants_dict_matches = {}#participant:[n_win,n_lose,n_draw,n_points,firstname,lastname,total_points,reg_date]

        for p in participants:
            participants_dict_matches.update({p.id: [0,0,0,0,p.first_name,p.last_name,0,p.reg_date]})

        for m in matchs:
            #if m.league.id != league_id: continue
            lst_local   = participants_dict_matches.get(m.local.id)
            lst_visitor = participants_dict_matches.get(m.visitor.id)
            if m.score_local > m.score_visitor:
                participants_dict_matches.update({m.local.id:   [ lst_local[0]+1, lst_local[1],   lst_local[2],                 lst_local[3]+3,
                                                                  lst_local[4],   lst_local[5],   lst_local[6] + m.score_local, lst_local[7] ] })
                participants_dict_matches.update({m.visitor.id: [ lst_visitor[0], lst_visitor[1]+1, lst_visitor[2],                 lst_visitor[3],
                                                                  lst_visitor[4], lst_visitor[5], lst_visitor[6] + m.score_visitor, lst_visitor[7] ] })
            if m.score_local < m.score_visitor:
                participants_dict_matches.update({m.local.id:   [ lst_local[0], lst_local[1]+1,   lst_local[2],                 lst_local[3],
                                                                  lst_local[4],   lst_local[5],   lst_local[6] + m.score_local, lst_local[7] ] })
                participants_dict_matches.update({m.visitor.id: [ lst_visitor[0]+1, lst_visitor[1], lst_visitor[2],                 lst_visitor[3]+3,
                                                                  lst_visitor[4], lst_visitor[5], lst_visitor[6] + m.score_visitor, lst_visitor[7] ] })
            else:
                participants_dict_matches.update({m.local.id:   [ lst_local[0], lst_local[1], lst_local[2]+1,               lst_local[3]+1,
                                                                  lst_local[4], lst_local[5],   lst_local[6] + m.score_local, lst_local[7] ] })
                participants_dict_matches.update({m.visitor.id: [ lst_visitor[0], lst_visitor[1] , lst_visitor[2]+1,                 lst_visitor[3]+1,
                                                                  lst_visitor[4],   lst_visitor[5],  lst_visitor[6] + m.score_visitor, lst_visitor[7] ] })

        participants_dict_matches = dict(sorted(participants_dict_matches.items(),reverse=True, key=lambda item: (item[1][3], item[1][6], item[1][7] ) ))# sort by point, total_points, reg_date
        
        '''for key, value in participants_dict_matches.items():
            p = participants.get(id=key)
            p_first = p.first_name
            p_last = p.last_name
            p_win = value[0]
            p_lose = value[1]
            p_draw = value[2]
            p_points = value[3]
            print(p_first,p_last, 'win:',p_win,'lose:',p_lose,'draw:',p_draw,'points:',p_points)
            if p_points != p_win*3 + p_draw: print('p_points not OK\n')'''
        
    except Match.DoesNotExist:
        raise Http404("participants_dict_matches does not exist")
    return render(request, 'league_bzh/rank.html', {'participants_dict_matches': participants_dict_matches})
