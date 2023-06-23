class Candy:
    def __init__( self, name, isChocolate, sugarPercentile, winPct ):
        self.name = name
        
        if isChocolate == "0":
            self.isChocolate = False
        else:
            self.isChocolate = True
            
        self.sugarPercentile = float( sugarPercentile )
        self.winPct = float( winPct )
        
    def getName( self ):
        return self.name
    
    def getIsChocolate( self ):
        return self.isChocolate
    
    def getSugarPercentile( self ):
        return self.sugarPercentile
    
    def getWinPct( self ):
        return self.winPct


def parseCandyDataFromLine( line ):
    name, isChocolate, sugarPercentile, winPct = line.split('\t')
    return Candy( name, isChocolate, sugarPercentile, winPct )

def main():
    candyDataFile = open("candy-data.txt", "r")
    
    noChocCandyWithMaxWinPct = None
    
    for line in candyDataFile:
        line = line.strip()
        
        candyData = parseCandyDataFromLine( line )
        
        if not candyData.getIsChocolate():
            if noChocCandyWithMaxWinPct == None or candyData.getWinPct() > noChocCandyWithMaxWinPct.getWinPct():
               noChocCandyWithMaxWinPct = candyData
            
    print( noChocCandyWithMaxWinPct.getName() )
    print( noChocCandyWithMaxWinPct.getWinPct() )
    candyDataFile.close()

main()