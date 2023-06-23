import graphics as g

movieRatingsFile = None
while True:
    movieRatingsFileName = input("Enter the name of the ratings file: ")
    try:
        movieRatingsFile = open( movieRatingsFileName, "r" )
        break
    except FileNotFoundError:
        print("{0} was not found".format ( movieRatingsFileName ))
        

firstLine = movieRatingsFile.readline()
firstLineTokens = firstLine.split(",")
movieTitle = firstLineTokens[1]

totalRatings = 0
totalRatingsAboveCool = 0

for line in movieRatingsFile:
    ratings = line.split(",")
    for rating in ratings:
        numericRating = int( rating )
        totalRatings += 1
        if numericRating >= 6:
            totalRatingsAboveCool += 1

coolPct = totalRatingsAboveCool / totalRatings

print('Movie Title: {}'.format( movieTitle ))
print('Total Number of Ratings: {}'.format( totalRatings ) )
print('Cool Percentage: {}'.format( coolPct ))

ratingImageFileName = ''
rating = ''
if totalRatings < 10:
    rating = "Too soon to rule"
    ratingImageFileName = 'tooSoonToRule.gif'
elif coolPct >= .6:
    rating = "COOL"
    ratingImageFileName = 'cool.gif'
else:
    rating = "DROOL"
    ratingImageFileName = 'drool.gif'
print( rating )
    
    

win = g.GraphWin('COOL or DROOL rater', 400, 400)

titleText = g.Text( g.Point( 200, 50 ), movieTitle )
titleText.draw( win )

ratingImage = g.Image( g.Point( 200, 200), ratingImageFileName )
ratingImage.draw( win )

coolPctText = g.Text( g.Point( 200, 350) , "{0:0.0f}% {1}".format( coolPct * 100, rating ))
coolPctText.draw( win )

