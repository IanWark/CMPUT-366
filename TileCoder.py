numTilings = 4
numTiles = 81


def tilecode(p,v,tileIndices):
	# write your tilecoder here (5 lines or so)
	for i in range(numTilings):
		pindex = int(((p+1.2)+i*0.2125/numTilings)*8/1.7)
		vindex = int(((v+0.07)+i*0.0175/numTilings)*8/0.14)
		tileIndices[i] = i*numTiles+pindex+9*vindex

def printTileCoderIndices(x,y):
	tileIndices = [-1]*numTilings
	tilecode(x,y,tileIndices)
	print 'Tile indices for input (',x,',',y,') are : ', tileIndices
printTileCoderIndices(-1.2,-0.07)
printTileCoderIndices(0.5,0.07)
printTileCoderIndices(5.99,5.99)
printTileCoderIndices(4.0,2.1)
