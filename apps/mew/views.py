from django.shortcuts import render
from random import randint
from .models import Player, Cat, Board
import itertools


# Create your views here.
def newgame(request):
    if "player_id" in request.session:
        request.session.flush()
    Player.objects.all().delete()
    Board.objects.all().delete()
    if not Cat.objects.filter(name = "Kyle").exists():
        Cat.objects.create(name = "Shadow", color = "black", fur = "plain")
        Cat.objects.create(name = "Griffey", color = "black", fur ="plain", hat = True)
        Cat.objects.create(name = "Louise", color = "black", fur ="striped", glasses = True)
        Cat.objects.create(name = "Charles", color = "black", fur ="spotted")
        Cat.objects.create(name = "Junior", color = "black", fur ="striped", scarf = True)
        Cat.objects.create(name = "Muffin", color = "black", fur ="spotted", scarf = True)
        Cat.objects.create(name = "Ashley", color = "grey", fur ="plain", glasses = True )
        Cat.objects.create(name = "Jamie", color = "grey", fur ="striped", scarf = True)
        Cat.objects.create(name = "Diana", color = "grey", fur ="spotted", hat = True)
        Cat.objects.create(name = "Robel", color = "grey", fur ="plain", scarf = True, hat = True)
        Cat.objects.create(name = "Jamal", color = "grey", fur ="spotted")
        Cat.objects.create(name = "Nicu", color = "grey", fur ="striped", scarf = True, glasses = True)
        Cat.objects.create(name = "John", color = "orange", fur ="plain", glasses = True)
        Cat.objects.create(name = "Helen", color = "orange", fur ="spotted", hat = True)
        Cat.objects.create(name = "Sahar", color = "orange", fur ="plain")
        Cat.objects.create(name = "Pumpkin Spice", color = "orange", fur ="striped")
        Cat.objects.create(name = "Chelsea", color = "orange", fur ="plain", scarf = True)
        Cat.objects.create(name = "Pretzel", color = "orange", fur ="striped", glasses = True)
        Cat.objects.create(name = "Rascal", color = "white", fur ="plain", scarf = True, glasses = True)
        Cat.objects.create(name = "Macaron", color = "white", fur ="spotted", glasses = True)
        Cat.objects.create(name = "Arjun", color = "white", fur ="plain")
        Cat.objects.create(name = "Ember", color = "white", fur ="spotted", scarf = True, hat = True)
        Cat.objects.create(name = "Kyle", color = "white", fur ="striped", hat = True)
        Cat.objects.create(name = "Ellie", color = "white", fur ="striped", scarf = True)
    #RANDOMLY ASSIGN PLAYER AND OPPONENT CHOICES
    player_choice = Cat.objects.get(id = randint(1,24))
    opponent_choice = Cat.objects.get(id = randint(1,24))

    #CREATING PLAYER AND OPPONENT
    this_player = Player.objects.create(chosencat = player_choice)
    this_opponent = Player.objects.create(chosencat = opponent_choice)


    #CREATING GAMEBOARD FOR PLAYER AND OPPONENT
    player_board = Board.objects.create(player = this_player)
    opponent_board = Board.objects.create(player = this_opponent)

    #ADDING ALL CATS TO EACH GAME BOARD
    all_cats = Cat.objects.all()
    for cat in all_cats:
        cat.board.add(player_board)
    for cat in all_cats:
        cat.board.add(opponent_board)

    #SETTING SESSION VARIABLES FOR PLAYER, OPPONENT, AND RESPECTIVE GAMEBOARDS
    request.session['player_id'] = this_player.id
    request.session['opponent_id'] = this_opponent.id
    request.session['player_board_id'] = player_board.id
    request.session['opponent_board_id'] = opponent_board.id
    player_cats = Board.objects.filter(id  = request.session['player_board_id']),

    context = {
        'player_cats' : Cat.objects.filter(board__player  = this_player).values_list('id', flat = True),
        'opponent_cats' : Cat.objects.filter(board__player = this_opponent).values_list('id', flat = True),
        'all_cats' : Cat.objects.all()
    }
    print context['player_cats']
    print context['opponent_cats']
    return render(request, "mew/index.html", context)

def game(request):
    #submit logic is fur orange
    if request.method == POST:
        if request.POST['name'] == "white":
            these_cats = Cat.objects.filter(color = "white")
        elif request.POST['name'] == "black":
            these_cats = Cat.objects.filter(color = "black")
        elif request.POST['name'] == "grey":
            these_cats = Cat.objects.filter(color = "grey")
        elif request.POST['name'] == "orange":
            these_cats = Cat.objects.filter(color = "orange")
        elif request.POST['name'] == "plain":
            these_cats = Cat.objects.filter(fur = "plain")
        elif request.POST['name'] == "striped":
            these_cats = Cat.objects.filter(fur = "striped")
        elif request.POST['name'] == "spotted":
            these_cats = Cat.objects.filter(fur = "spotted")
        elif request.POST['name'] == "glasses":
            these_cats = Cat.objects.filter(glasses = True)
        elif request.POST['name'] == "scarf":
            these_cats = Cat.objects.filter(scarf = True)
        elif request.POST['name'] == "hat":
            these_cats = Cat.objects.filter(hat = True)
        if request.POST['name'] == "white" or request.POST['name'] == "grey" or request.POST['name'] == "black" or request.POST['name'] == "orange":
            print "something"

    player_board_id = request.session['player_board_id']
    opponent_board_id = request.session['opponent_board_id']
    this_player = Player.objects.get(id = request.session['player_id'])
    this_opponent = Player.objects.get(id = request.session['opponent_id'])
    context = {
        'player_cats' : Cat.objects.filter(board__player  = this_player),
        'opponent_cats' : Cat.objects.filter(board__player = this_opponent)
    }

    return render(request, "mew/index.html", context)
