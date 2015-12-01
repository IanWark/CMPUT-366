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
Fp = [-1]*numTilings

# sums theta values for the indices at a certain action
def actionValue(F,a,theta):
    value = 0
    for index in F:
        value = value + theta[index+(a*numTiles)] # num tiles is 324 (9*9*4)
    return value

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
                # first equation from mountain-car.pdf 
                tilecode(S,F)
                if rand() <= Emu:                 # randomly explore
                    a = randint(0, 2)
                    traces = zeros(n)
                else:                             # greedy action choice
                    a = argmax([actionValue(F,0,theta),actionValue(F,1,theta),actionValue(F,2,theta)])
       
                # Take action, observe r,Sp
                r,Sp=mountaincar.sample(S,a)
                G += r
                # fourth equation from mountain-car.pdf
                for index in F:
                    traces[index+(a*numTiles)] = 1          # replacing traces on indices where feature vector is 1                
                if Sp == None:
                    delta = r - actionValue(F,a,theta)
                    theta =  theta + alpha*delta*traces
                    break
                # Choose next action
                tilecode(Sp,Fp)
                ap = argmax([actionValue(Fp,0,theta),actionValue(Fp,1,theta),actionValue(Fp,2,theta)]) 
                # third equation from mountain-car.pdf
                delta = r + actionValue(Fp,ap,theta) - actionValue(F,a,theta)
                
                # second equation from mountain-car.pdf
                theta = theta + alpha*delta*traces
                
                traces = gamma*lmbda*traces    # decay every component of traces
                S=Sp
                step += 1
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



learn()