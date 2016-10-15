
import tictactoe
import gameSearch as gs
import sys
sys.path.append('/home/sahil/Desktop/AI/project/distr/')
print sys.path
inf = float('infinity')
debug = False

def playGameNegamax(game):
    depth=8
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

		value,move= gs.negamax(game,-inf,inf,None,None,depth)#=gs.pvSplit(game,-inf,inf) #
		depth-=2
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
		game.turnChange()

gameObj =tictactoe.tictactoe(debug)
print gameObj.player
#gameObj.turnChange()
#print gameObj.player
playGameNegamax(gameObj)
