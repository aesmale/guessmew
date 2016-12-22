from django.shortcuts import render
from random import randint
import random
from .models import Player, Cat, Board
import itertools
from django.contrib import messages



# Create your views here.
def newgame(request):
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
    request.session['questions'] = ["white", "black", "grey", "orange", "glasses", "scarf", "hat"]

    player_cats = Board.objects.filter(id  = request.session['player_board_id']),

    context = {
        'player' : this_player,
        'opponent' : this_opponent,
        'player_cats' : Cat.objects.filter(board__player  = this_player).values_list('id', flat = True),
        'opponent_cats' : Cat.objects.filter(board__player = this_opponent).values_list('id', flat = True),
        'all_cats' : Cat.objects.all()
    }
    print context['player_cats']
    print context['opponent_cats']
    return render(request, "mew/index.html", context)

def game(request):
#FETCHING RELATED PLAYER BOARDS AND PLAYER OBJECTS
    player_board = Board.objects.get(id = request.session['player_board_id'])
    opponent_board= Board.objects.get(id = request.session['opponent_board_id'])
    this_player = Player.objects.get(id = request.session['player_id'])
    this_opponent = Player.objects.get(id = request.session['opponent_id'])

#LOGIC FOR IF THE REQUEST IS A POST FROM FORM
    if request.method == "POST":
#DEPENDING ON THE POST, FILTER THE CATS BASED ON OPPONENTS CHOSENCAT
        if request.POST['option'] == "white":
            if this_opponent.chosencat.color == request.POST['option']:
                these_cats = Cat.objects.filter(color = "white")
            else:
                these_cats = Cat.objects.all().exclude(color = "white")
        elif request.POST['option'] == "black":
            if this_opponent.chosencat.color == request.POST['option']:
                these_cats = Cat.objects.filter(color = "black")
            else:
                these_cats = Cat.objects.all().exclude(color = "black")
        elif request.POST['option'] == "grey":
            if this_opponent.chosencat.color == request.POST['option']:
                these_cats = Cat.objects.filter(color = "grey")
            else:
                these_cats = Cat.objects.all().exclude(color = "grey")
        elif request.POST['option'] == "orange":
            if this_opponent.chosencat.color == request.POST['option']:
                these_cats = Cat.objects.filter(color = "orange")
            else:
                these_cats = Cat.objects.all().exclude(color = "orange")
        elif request.POST['option'] == "plain":
            if this_opponent.chosencat.fur == request.POST['option']:
                these_cats = Cat.objects.filter(fur = "plain")
            else:
                these_cats = Cat.objects.all().exclude(fur = "plain")
        elif request.POST['option'] == "striped":
            if this_opponent.chosencat.fur == request.POST['option']:
                these_cats = Cat.objects.filter(fur = "striped")
            else:
                these_cats = Cat.objects.all().exclude(fur = "striped")
        elif request.POST['option'] == "spotted":
            if this_opponent.chosencat.fur == request.POST['option']:
                these_cats = Cat.objects.filter(fur = "spotted")
            else:
                these_cats = Cat.objects.all().exclude(fur = "spotted")
        elif request.POST['option'] == "glasses":
            if this_opponent.chosencat.glasses == True:
                these_cats = Cat.objects.all().exclude(glasses = False)
            else:
                these_cats = Cat.objects.all().exclude(glasses = True)
        elif request.POST['option'] == "scarf":
            if this_opponent.chosencat.scarf == True:
                these_cats = Cat.objects.all().exclude(scarf = False)
            else:
                these_cats = Cat.objects.all().exclude(scarf = True)
        elif request.POST['option'] == "hat":
            if this_opponent.chosencat.hat == True:
                these_cats = Cat.objects.all().exclude(hat = False)
            else:
                these_cats = Cat.objects.all().exclude(hat = True)



#REMOVING THE FILTERED CATS FROM THE PLAYERS GAMEBOARD
        for cat in these_cats:
            cat.board.remove(player_board)


#CHOOSING A RANDOM Q ON BEHALF OF THE OPPONENT
        opponent_question = random.choice(request.session['questions'])
        print opponent_question
        for each in request.session['questions']:
            print each

#REMOVING REDUNDANT OPTIONS BASED ON ? PICKED
        if opponent_question == "white":
            request.session['questions'].remove('black')
            request.session['questions'].remove('grey')
            request.session['questions'].remove('orange')
        if opponent_question == "black":
            request.session['questions'].remove('white')
            request.session['questions'].remove('grey')
            request.session['questions'].remove('orange')
        if opponent_question == "grey":
            request.session['questions'].remove('white')
            request.session['questions'].remove('black')
            request.session['questions'].remove('orange')
        if opponent_question == "orange":
            request.session['questions'].remove('white')
            request.session['questions'].remove('black')
            request.session['questions'].remove('grey')
        if opponent_question == "spotted":
            request.session['questions'].remove('plain')
            request.session['questions'].remove('striped')
        if opponent_question == "plain":
            request.session['questions'].remove('spotted')
            request.session['questions'].remove('striped')
        if opponent_question == "striped":
            request.session['questions'].remove('spotted')
            request.session['questions'].remove('plain')

#REMOVING ? PICKED FROM LIST TO PREVENT REPEATS
        for question in request.session['questions']:
            if question == opponent_question:
                print question
                request.session['questions'].remove(question)
#DEPENDING ON THE ???, FILTER THE CATS BASED ON PLAYERS CHOSENCAT, SET MESSAGES FOR PLAYER
        if question == "white":
            messages.add_message(request, messages.INFO, 'Opponent asked if your kitty was white')
            if this_player.chosencat.color == question:
                these_cats = Cat.objects.filter(color = "white")
            else:
                these_cats = Cat.objects.all().exclude(color = "white")
        elif question == "black":
            messages.add_message(request, messages.INFO, 'Opponent asked if your kitty was black')
            if this_player.chosencat.color == question:
                these_cats = Cat.objects.filter(color = "black")
            else:
                these_cats = Cat.objects.all().exclude(color = "black")
        elif question == "grey":
            messages.add_message(request, messages.INFO, 'Opponent asked if your kitty was grey')
            if this_player.chosencat.color == question:
                these_cats = Cat.objects.filter(color = "grey")
            else:
                these_cats = Cat.objects.all().exclude(color = "grey")
        elif question == "orange":
            messages.add_message(request, messages.INFO, 'Opponent asked if your kitty was orange')
            if this_player.chosencat.color == question:
                these_cats = Cat.objects.filter(color = "orange")
            else:
                these_cats = Cat.objects.all().exclude(color = "orange")
        elif question == "plain":
            messages.add_message(request, messages.INFO, 'Opponent asked if your kitty has plain fur')
            if this_player.chosencat.fur == question:
                these_cats = Cat.objects.filter(fur = "plain")
            else:
                these_cats = Cat.objects.all().exclude(fur = "plain")
        elif question == "striped":
            messages.add_message(request, messages.INFO, 'Opponent asked if your kitty has striped fur')
            if this_player.chosencat.fur == question:
                these_cats = Cat.objects.filter(fur = "striped")
            else:
                these_cats = Cat.objects.all().exclude(fur = "striped")
        elif question == "spotted":
            messages.add_message(request, messages.INFO, 'Opponent asked if your kitty has spotted fur')
            if this_player.chosencat.fur == question:
                these_cats = Cat.objects.filter(fur = "spotted")
            else:
                these_cats = Cat.objects.all().exclude(fur = "spotted")
        elif question == "glasses":
            messages.add_message(request, messages.INFO, 'Opponent asked if your kitty is wearing glasses')
            if this_player.chosencat.glasses == True:
                these_cats = Cat.objects.all().exclude(glasses = False)
            else:
                these_cats = Cat.objects.all().exclude(glasses = True)
        elif question == "scarf":
            messages.add_message(request, messages.INFO, 'Opponent asked if your kitty is wearing a scarf')
            if this_player.chosencat.scarf == True:
                these_cats = Cat.objects.all().exclude(scarf = False)
            else:
                these_cats = Cat.objects.all().exclude(scarf = True)
        elif question == "hat":
            messages.add_message(request, messages.INFO, 'Opponent asked if your kitty is wearing a hat')
            if this_player.chosencat.hat == True:
                these_cats = Cat.objects.all().exclude(hat = False)
            else:
                these_cats = Cat.objects.all().exclude(hat = True)
        for cat in these_cats:
            cat.board.remove(opponent_board)
    context = {
        'player' : this_player,
        'opponent' : this_opponent,
        'player_cats' : Cat.objects.filter(board__player  = this_player).values_list('id', flat = True),
        'opponent_cats' : Cat.objects.filter(board__player = this_opponent).values_list('id', flat = True),
    }

    return render(request, "mew/index.html", context)
