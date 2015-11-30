
numTilings = 4
numTiles = 9 * 9 * numTilings
    
def tilecode(S,tileIndices):
    position,velocity = S
    position += 1.2 
    velocity += 0.07

    for i in range (0, numTilings):
        positionNew = i * (0.2125) / numTilings
	velocityNew = i * (0.0175 ) / numTilings 
        positionTile = int( (8 * (position + positionNew)/1.7))
        velocityTile = int( (8 * (velocity + velocityNew)/0.14))
        tileIndices[i] = int((81 * i) + (9 * velocityTile) + positionTile)
    
    
def printTileCoderIndices(S):
    tileIndices = [-1]*numTilings
    tilecode(S,tileIndices)
    print 'Tile indices for input (',position,',',velocity,') are : ', tileIndices

printTileCoderIndices(-1.2,-0.07)
printTileCoderIndices(0.5,0.07)
printTileCoderIndices(5.99,5.99)
printTileCoderIndices(4.0,2.1)