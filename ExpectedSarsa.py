import blackjack
import numpy
import random

def policy(s):
    global Q
    if Q[s][0] < Q[s][1]:
        return 1
    else:
        return 0

def ExpectedSarsa(alpha,Epi,Emu,numEpisodes,Q=[]):    
    # initialize
    if Q == []:
        Q = 0.00001*numpy.random.randint(2,size=[181,2])
    
    returnSum = 0
    for episodeNum in range(numEpisodes):
        # Every 1000000 episodes print average return
        if episodeNum%1000000 == 0 and episodeNum!=0:
            print('Episode:',episodeNum,' Average Return =',float(returnSum)/float(episodeNum))
        G = 0
        s=blackjack.init()
        # Until s is terminal:
        while s!=-1:
            # Choose action
            if s == 0:
                a = 1       
            elif numpy.random.rand() <= Emu:    # randomly explore
                a = random.randint(0, 1)
            else:                               # greedy action choice
                if Q[s][0] < Q[s][1]:
                    a = 1
                else:
                    a = 0     
            # Take action, observe r,sp
            r,sp=blackjack.sample(s,a)
            G += r
            # Choose next action
            if Q[sp][0] < Q[sp][1]:
                ap = 1
            else:
                ap = 0      
            # Update Q
            if sp == -1:
                target = r + (1-(Epi/2))*0 + (Epi/2)*0
                Q[s][a] = Q[s][a] + alpha*(target - Q[s][a])                
            else:
                target = r + (1-(Epi/2))*Q[sp][ap] + (Epi/2)*Q[sp][1-ap]
                Q[s][a] = Q[s][a] + alpha*(target - Q[s][a])
            s=sp
        returnSum += G
        
    averageReturn = float(returnSum)/float(episodeNum)
    return Q,averageReturn
