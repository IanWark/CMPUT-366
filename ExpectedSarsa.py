import blackjack
import numpy
import random

def policy(s):
    global Q
    if Q[s][0] < Q[s][1]:
        return 1
    else:
        return 0
    
# initialize
Q = 0.00001*numpy.random.randint(2,size=[181,2])
alpha = 0.001
Epi = 0.01
Emu = 0.05
numEpisodes = 1000000

returnSum = 0
for episodeNum in range(numEpisodes):
    # Every 100000 episodes print average return
    if episodeNum%100000 == 0 and episodeNum!=0:
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
        target = r + (1-(Epi/2))*Q[sp][ap] + (Epi/2)*Q[sp][1-ap]
        Q[s][a] = Q[s][a] + alpha*(target - Q[s][a])
        s=sp
    returnSum += G
    
print('Episode:',episodeNum,' Average Return =',float(returnSum)/float(episodeNum))
blackjack.printPolicy(policy)