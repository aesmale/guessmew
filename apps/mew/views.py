from django.shortcuts import render
from .models import Cat, Player, Board
from random import randint

# Create your views here.
def index(request):
    context = {
        'all_cats': Cat.objects.all(),
    }
    print context
    return render(request, "mew/index.html", context)

def newgame(request):
    player_choice = Cat.objects.get(id = request.POST['cat'])
    opponent_choice = Cat.objects.get(id = randint(1,25))


    #CREATING PLAYER AND OPPONENT
    this_player = Player.objects.create(chosencat = player_choice)
    this_opponent = Player.objects.create(chosencat = opponent_choice)


    #CREATING GAMEBOARD FOR PLAYER AND OPPONENT
    player_board = Board.objects.create(player = request.session['player'])
    opponent_board = Board.objects.create(player = request.session['opponent'])


    #ADDING ALL CATS TO EACH GAME BOARD
    all_cats = Cats.objects.all()
    player_board.cats.add(all_cats)
    opponent_board.cats.add(all_cats)

    #SETTING SESSION VARIABLES FOR PLAYER, OPPONENT, AND RESPECTIVE GAMEBOARDS
    request.session['player_id'] = this_player.id
    request.session['opponent_id'] = this_opponent.id
    request.session['player_board_id'] = player_board.id
    request.session['opponent_board_id'] = opponent_board.id
