import numpy

numTilings = 4
    
def tilecode(x,y,tileIndices):
    # write your tilecoder here (5 lines or so)
    for i in range(numTilings):
        xNew = x + (i*0.6/4)
        yNew = y + (i*0.6/4)
        xTile = numpy.ceil(xNew/0.6) - 1
        yTile = numpy.ceil(yNew/0.6) - 1
        tileIndices[i] = i*81 + yTile*9 + xTile
    
def printTileCoderIndices(x,y):
    tileIndices = [-1]*numTilings
    tilecode(x,y,tileIndices)
    print 'Tile indices for input (',x,',',y,') are:', tileIndices

#printTileCoderIndices(0.1,0.1)
#printTileCoderIndices(4.0,2.0)
#printTileCoderIndices(5.99,5.99)
#printTileCoderIndices(4.0,2.1)
    
