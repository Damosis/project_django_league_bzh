Modèle de données très simple:

Participant:
	-first_name 
	-last_name
	-age
	-reg_date

League:
	-league_name

Match:
	-match_name
    	-match_date
    	-local
    	-visitor
    	-league
    	-score_local
    	-score_visitor

N.B1: Je n’ai pas ajouté de ligue pour les participants, c’est un choix initial afin de simplifier les choses. J'ai voulu aller vite à cause de mon problème de PC.

N.B2: Il n’y a pas d’équipe par simplification également.

N.B3: Je n’ai pas pris le temps de rendre le projet “joli”
 

Algo classement:

3 points par victoires
1 points par match nul

tri par:
-points
-points marqué
-date d’enregistrement



http://localhost:8000/admin/
panneau admin

http://localhost:8000/league_bzh/
liste des participants

http://localhost:8000/league_bzh/participant/1/
detail joueur 1

http://localhost:8000/league_bzh/register/
Ajouter un joueur

http://localhost:8000/league_bzh/add-match/
Ajouter un match

http://localhost:8000/league_bzh/rank/2/
Classement ligue 2

http://localhost:8000/league_bzh/matches/
liste des matchs joués
