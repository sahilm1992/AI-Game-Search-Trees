import gameSearch as gs
import tictactoe
inf = float('infinity')
from time 	import time
debug = False

def playGameNegamax(game):
    print game
    while not game.checkGameExists():
	if(game.player=='X'):
		userInput = input("Enter move: ")
		userMove = int(userInput)
		if(userMove <0 or userMove > 8 or not (game.GAMEBOARD[userMove] ==' ')):
			continue
		game.changeGAMEBOARDbyMove(userMove)
		game.turnChange()
	else:
		start = time()
		value,move= gs.negamax(game,-inf,inf,None,None)#=gs.pvSplit(game,-inf,inf) #
		#print "grid sent, score ",value
		#print game
		#print "move ",move
		if move == None :
		    print "move is None. Stopping"
		    break
		game.changeGAMEBOARDbyMove(move)
		print "Player",game.player,"to",move,"for value",value,
		if not debug: print
		print game
		finish = time()
		print "Time ", finish-start
		game.turnChange()

gameObj =tictactoe.tictactoe(debug)
print gameObj.player
#gameObj.turnChange()
#print gameObj.player
playGameNegamax(gameObj)
