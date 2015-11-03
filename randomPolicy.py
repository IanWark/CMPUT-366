import blackjack
import numpy
import random

#from scipy import *
numEpisodes = 2000


def showOneGame():
    s=blackjack.init()

    # this is a defined set of moves, we need to make (equiprobably)
    # randomly choose a move.
    turn=0
    total_return = 0
    while s!=-1: #-1 is terminal
        a = numpy.random.randint(0, 2)
        r,sp=blackjack.sample(s,a)
        total_return += r
        s=sp
        turn+=1
    return total_return

returnSum = 0.0
for episodeNum in range(numEpisodes):
    G = 0
    G = showOneGame();
    print("Episode: ", episodeNum, "Return: ", G)
    returnSum = returnSum + G
print("Average return: ", returnSum/numEpisodes)
