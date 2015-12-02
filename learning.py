import mountaincar
from Tilecoder import numTilings, tilecode, numTiles
from Tilecoder import numTiles as n
from pylab import *  #includes numpy

numRuns = 50
numEpisodes = 200
alpha = 0.5/numTilings
gamma = 1
lmbda = 0.9
Epi = Emu = epsilon = 0
n = numTiles * 3
F = [-1]*numTilings
Fp = [-1]*numTilings
theta = -0.01*rand(n)
episodeReturn = 0*zeros(numEpisodes)
episodeSteps = 0*zeros(numEpisodes)

# computes state-action value where the state is in F and the action is a
def QValue(F,a,theta):
    value = 0
    for index in F:
        value = value + theta[index+(a*numTiles)]
    return value

def Qs(F,theta):
    return [QValue(F,0,theta),QValue(F,1,theta),QValue(F,2,theta)]

def learn():    
    runSum = 0.0
    for run in xrange(numRuns):
        theta = -0.01*rand(n)
        returnSum = 0.0
        for episodeNum in xrange(numEpisodes):
            step = 0
            G = 0        
            traces = zeros(n)
            S=mountaincar.init()
            # Until S is terminal:
            while S!=None:
                # Choose action
                tilecode(S,F)
                if rand() <= Emu:                 # randomly explore
                    a = randint(0, 2)
                else:                             # greedy action choice
                    a = argmax([QValue(F,0,theta),QValue(F,1,theta),QValue(F,2,theta)])
                # Replacing traces on indices where feature vector is 1
                for index in F:
                    traces[index+(a*numTiles)] = 1                     
                # Take action, observe r,Sp
                r,Sp=mountaincar.sample(S,a)
                G += r
                # If terminal action update theta and end episode
                if Sp == None:
                    delta = r - QValue(F,a,theta)
                    theta =  theta + alpha*delta*traces
                    break
                # Choose expected next action
                tilecode(Sp,Fp)
                ap = argmax([QValue(Fp,0,theta),QValue(Fp,1,theta),QValue(Fp,2,theta)])
                # Update theta
                randomAction = (Epi/3)*QValue(Fp,0,theta) + (Epi/3)*QValue(Fp,1,theta)+ (Epi/3)*QValue(Fp,2,theta)
                delta = r + randomAction + (1-Epi)*QValue(Fp,ap,theta) - QValue(F,a,theta)
                theta = theta + alpha*delta*traces
                # Decay every component
                traces = gamma*lmbda*traces
                S=Sp
                step += 1
            returnSum += G        
    
            print "Episode: ", episodeNum, "Steps:", step, "Return: ", G
            episodeReturn[episodeNum] += (G-episodeReturn[episodeNum])/(numRuns+1)
            episodeSteps[episodeNum] += (step-episodeSteps[episodeNum])/(numRuns+1)
            returnSum = returnSum + G
        print "Average return:", returnSum/numEpisodes
        runSum += returnSum
    print "Overall performance: Average sum of return per run:", runSum/numRuns
    writeAverages(episodeReturn,episodeSteps)

#Additional code here to write average performance data to files for plotting...
#You will first need to add an array in which to collect the data

def writeF():
    fout = open('value', 'w')
    F = [0]*numTilings
    steps = 50
    for i in range(steps):
        for j in range(steps):
            tilecode([-1.2+i*1.7/steps, -0.07+j*0.14/steps], F)
            height = -max(Qs(F,theta))
            fout.write(repr(height) + ' ')
        fout.write('\n')
    fout.close()
    
def writeAverages(episodeReturn,episodeSteps):
    fout = open('avgret.dat','w')
    for episode in range(0,numEpisodes):
        fout.write(str(episode)+'\t'+str(episodeReturn[episode])+'\t'+str(int(episodeSteps[episode])))  
        fout.write('\n')
    fout.close()

learn()