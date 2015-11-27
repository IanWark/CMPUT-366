import mountaincar
from Tilecoder import numTilings, tilecode, numTiles
from Tilecoder import numTiles as n
from pylab import *  #includes numpy

numRuns = 1
numEpisodes = 200
alpha = 0.5/numTilings
gamma = 1
lmbda = 0.9
Epi = Emu = epsilon = 0
n = numTiles * 3
F = [-1]*numTilings

runSum = 0.0
for run in xrange(numRuns):
    theta = -0.01*rand(n)
    returnSum = 0.0
    for episodeNum in xrange(numEpisodes):
        G = 0
        
        S=mountaincar.init()
        F = Tilecoder.tilecode(S,F)
        # Until s is terminal:
        while s!=-1:
            # Choose action    
            if numpy.random.rand() <= Emu:    # randomly explore
                a = random.randint(0, 2)
            else:                               # greedy action choice
                a = numpy.argmax(actionValue(F,0,theta),actionValue(F,1,theta),actionValue(F,2,theta))
   
            # Take action, observe r,sp
            r,Sp=mountaincar.sample(s,a)
            G += r
            # Choose next action
            Fp = Tilecoder.tilecode(Sp,F)
            ap = numpy.argmax(actionValue(Fp,0,theta),actionValue(Fp,1,theta),actionValue(Fp,2,theta))    
            # Update Q
            if sp == -1:
                target = r
                Q[s][a] = Q[s][a] + alpha*(target - Q[s][a])                
            else:
                target = r + (1-(Epi/2))*Q[sp][ap] + (Epi/2)*Q[sp][1-ap]
                Q[s][a] = Q[s][a] + alpha*(target - Q[s][a])
            s=sp
        returnSum += G        
    
        print "Episode: ", episodeNum, "Steps:", step, "Return: ", G
        returnSum = returnSum + G
    print "Average return:", returnSum/numEpisodes
    runSum += returnSum
print "Overall performance: Average sum of return per run:", runSum/numRuns

#Additional code here to write average performance data to files for plotting...
#You will first need to add an array in which to collect the data

def writeF():
    fout = open('value', 'w')
    F = [0]*numTilings
    steps = 50
    for i in range(steps):
        for j in range(steps):
            tilecode(-1.2+i*1.7/steps, -0.07+j*0.14/steps, F)
            height = -max(Qs(F))
            fout.write(repr(height) + ' ')
        fout.write('\n')
    fout.close()

# sums theta values for the indices at a certain action
def actionValue(F,a,theta):
    value = 0
    for index in F:
        value = value + theta[index+(a*numTiles*81)]
    return value