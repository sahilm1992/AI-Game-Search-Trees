

import copy
import sys
sys.path.append('/home/sahil/Desktop/AI/project/distr/')
print sys.path
#debug = False

def negamax(game,alpha,beta,output,movement,depth):
    inf = float('infinity')
    import dispy
    import tictactoe

    if game.checkGameExists() :

        return game.checkStatus(), None	

    bestValue = -inf
    bestMove = None
    movesList=game.getNextMoves()


    if len(movesList)==depth and depth >4:

	tmpMoves =[-1]*10
	tmpGrid=[-1]*10
	counter=0
	for mv in movesList:
		tmpMoves[counter]=mv
		game.changeGAMEBOARDbyMove(mv)
		tmpGrid[counter]=copy.deepcopy(game)
		game.unchangeGAMEBOARDbyMove(mv)
		counter+=1



	cluster = dispy.JobCluster(negamax,depends=[])
	jobs = []
	for i in range(0,len(movesList)):

		print " submitting" , tmpGrid[i].GAMEBOARD, -beta, -alpha, tmpMoves[i], depth
		job = cluster.submit(tmpGrid[i],-beta,-alpha,None,tmpMoves[i],depth)
		job.id = i 
		jobs.append(job)

	results=[]
	for job in jobs:
		
		returnedbyProc =  job() 
		if(results is None):
			print job.exception
		else:
			print "STDOUT",job.stdout
		results.append(returnedbyProc)

	cluster.print_status()
	print " RESULTS ARE"
	print results
	for bv,bm in results:
		if(bv>bestValue):
			bestValue=bv
			bestMove=bm

	return [bestValue,bestMove]

	print "distr" 
	#print "ho"#,results
	#return bvF,bmF

    elif len(movesList)<8:
	 #print "h"
	 for move in game.getNextMoves():

		game.changeGAMEBOARDbyMove(move)
		value = - negamax(game,-beta,-alpha,None,None,depth)[0]

		game.unchangeGAMEBOARDbyMove(move)

		if value >= bestValue:
	
			bestValue = value
			bestMove = move

		else:
			None

		if(bestValue>=beta):

			break
		alpha = max([alpha,bestValue])
    if(len(movesList)==depth-1):
	
	print( game.GAMEBOARD,bestValue,movement)
	return -bestValue,movement

    return bestValue, bestMove
