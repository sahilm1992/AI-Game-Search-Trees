import copy
debug = False
inf = float('infinity')
import multiprocessing as mp



def negamax(game,alpha,beta,output,movement):
    #print game
    if debug: print '   '*(10-depthLeft), game,
    # If at terminal state or depth limit, return utility value and move None
    if game.checkGameExists() :
        if debug: print 'terminal value',game.checkStatus()
        return game.checkStatus(), None
    if debug: print
    # Find best move and its value from current state
    bestValue = -inf
    bestMove = None
    movesList=game.getNextMoves()

    #print len(movesList)
    #input("hello")

    if len(movesList)==8:
	##print "hi"
	tmpMoves =[-1]*10
	tmpGrid=[-1]*10
	counter=0
	for mv in movesList:
		tmpMoves[counter]=mv
		game.changeGAMEBOARDbyMove(mv)
		tmpGrid[counter]=copy.deepcopy(game)
		game.unchangeGAMEBOARDbyMove(mv)
		counter+=1
	output = mp.Queue()
	processes = [mp.Process(target=negamax, args=(tmpGrid[i],-beta,-alpha,output,tmpMoves[i])) for i in range(0, len(movesList))]
	#for x in tmpGrid:
	#	print x	
	#print tmpGrid[0],"\n\n"
	#print len(movesList)
	for p in processes:
		p.start()
	
	for p in processes:
		p.join()
	#print "proc"
	#print output.get()
	bvF=-2
	bmF=-1
	results = [output.get() for p in processes]
	for bv,bm in results:
		if(bv>=bvF):
			bvF=bv
			bmF=bm
	
	#print results
	#print "ho"#,results
	return bvF,bmF

    elif len(movesList)<8:
	 #print "h"
	 for move in game.getNextMoves():
		# Apply a move to current state
		game.changeGAMEBOARDbyMove(move)
		value = - negamax(game,-beta,-alpha,None,None)[0]
		# Remove the move from current state, to prepare for trying a different move
		game.unchangeGAMEBOARDbyMove(move)
		#if debug: print '   '*(10-depthLeft), game, "move",move,"backed up value",value,
		if value > bestValue:
		#	Value for this move is better than moves tried so far from this state.
			bestValue = value
			bestMove = move
			if debug: print "new best"
		else:
			if debug: print
		if(bestValue>=beta):
			break
		alpha = max([alpha,bestValue])
    if(len(movesList)==7):
	if(output is not None):
		#print "********"
		#print 
		#print game,bestValue, movement
		#print "*********"
		output.put([-1*bestValue,movement])
    #print game,bestValue
    return bestValue, bestMove
