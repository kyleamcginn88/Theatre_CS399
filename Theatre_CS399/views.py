from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {})
	
def store(request):
    return render(request, 'store.html', {})
	
def performances(request):
	list_performances = [('1/15/15', 'Fish Pump', 'Techno' ),
	('2/25/15', '7pac' ,'Hip-Hop'),
	('3/1/15', 'J-ci and Jolow','R&B' ),
	('4/18/15', 'King of Lions', 'Alternative Rock'),
	('5/5/15', 'Dr Jays', 'Rap' ),
	('6/7/15', 'Nerdvana' , 'Grunge'),
	('7/11/15', 'My Chemical Love' , 'Punk'),
	('8/21/15', 'T.I. Guy' , 'Hip-Hop'),
	('9/13/15', 'RUN D & C' ,'Hip-Hop'),
	('10/16/15', 'Food Thrower', 'Alternative Rock' ),
	('11/23/15', 'Dark Keys' ,'Alternative Rock'),
	('12/11/15', 'IceBox','Rap' ),
	('12/31/15', 'boyz II Gentlemen', 'R&B' )]
	return render(request, 'performances.html', {'list_performances': list_performances})
	
def location(request):
    return render(request, 'location.html', {})
	
	
# Random movie generator: http://phrasegenerator.com/actionmovies
def movies(request):
    list_movies = [('Predict' , 'Only one can Predict the future, are you ready?') ,
	('Galactica Reborn' , 'Galactica is back!') ,
	('Destructio' , 'Destruction is the answer.') ,
	('Quadruple Overkill' , 'Real-life counter-strike.') ,
	('Infinite Blood' , 'In an infinite world, there is infinite blood.') ,
	('War for Surrender' , 'Sometimes its best to just surrender.') ,
	('Duke of Retreat' , 'Sometimes its better to be the retreating rich person.') ,
	('Maximum Revenge' , 'When only some revenge isnt enough.') ,
	('Reflex Payback' , 'The automated killer is the key to survival.') ,
	('Fist of Vengence' , 'A fighting movie about fists!') ,
	('Triple Honor' , 'Triple kills, triple honor') ,
	('Sudden Execution' , 'Fun with turrets.') ,
	('Vendetta of Jeopardy' , 'A spin off from V for vendetta.') ,
	('Inferno of Action' , 'Fiery flaming spiral of death.') ,
	('Soldier of Justice' , 'Judge Dredd is back!') ]
    return render(request, 'movies.html', {'list_movies': list_movies})
    