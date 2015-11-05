import blackjack
import numpy
import random
import ExpectedSarsa

alpha = 0.001
Epi = 0.01
Emu = 0.01
numEpisodes = 1000000

maxQ = []
maxReturn = -1
maxEpi=0
maxEmu=0
maxAlpha=0

for alpha in [0.001]:
    for Epi in [0.02,0.01]:
        for Emu in [0.01]:
            print('alpha:',alpha,'Epi:',Epi,'Emu',Emu)
            Q,averageReturn = ExpectedSarsa.ExpectedSarsa(alpha,Epi,Emu,numEpisodes)
            print(averageReturn)
            Q,averageReturn = ExpectedSarsa.ExpectedSarsa(0,0,0,numEpisodes,Q) 
            print(averageReturn)
            if averageReturn > maxReturn:
                maxAlpha = alpha
                maxEpi = Epi
                maxEmu = Emu
                maxQ = Q
                maxReturn = averageReturn
                
                
print(maxAlpha,maxEpi,maxEmu,maxReturn)
f = open('optimization1.txt','w')
f.write('maxAlpha: '+str(maxAlpha)+' maxEpi: '+str(maxEpi)+' maxEmu: '+str(maxEmu)+' maxReturn: '+str(maxReturn))
f.close()