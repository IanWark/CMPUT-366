
numTilings = 4
numTiles = 9 * 9 * numTilings
    
def tilecode(x,y,tileIndices):
    x += 1.2 
    y += 0.07

    for i in range (0, numTilings):
        xNew = i * (0.2125) / numTilings
	yNew = i * (0.0175 ) / numTilings 
        xTile = int( (8 * (x + xNew)/1.7))
        yTile = int( (8 * (y + yNew)/0.14))
        tileIndices[i] = int((81 * i) + (9 * yTile) + xTile)
    
    
def printTileCoderIndices(x,y):
    tileIndices = [-1]*numTilings
    tilecode(x,y,tileIndices)
    print 'Tile indices for input (',x,',',y,') are : ', tileIndices

printTileCoderIndices(-1.2,-0.07)
printTileCoderIndices(0.5,0.07)
printTileCoderIndices(5.99,5.99)
printTileCoderIndices(4.0,2.1)