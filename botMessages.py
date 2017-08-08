import tweepy  # what in the sweet christmas causes this error
import random
import time
from keys import Keys

auth = tweepy.OAuthHandler(Keys.consumerKey, Keys.consumerKeySecret)
auth.set_access_token(Keys.accessToken, Keys.accessTokenSecret)

# Spinning Up

errorCount = 0  # number of errors
user = ""  # add DM recipient here
api = tweepy.API(auth)
print "Current user is: " + str(api.me().name)


# This gets the ID of a tweet
def getID(status):
    status = str(status)
    idList = status.split('id=')
    listOfMostlyTrash = idList[2].split(',')
    return listOfMostlyTrash[0]


# Retrieving most recent tweet to determine if action must be taken
def getMostRecent(api, operatedOn):
    mostRecent = api.user_timeline(operatedOn)
    entireTweet = str(mostRecent[0])  # this includes everything, not just text
    mostRecentID = getID(entireTweet)
    return mostRecentID


def sendNightlyDM(api, numberOfTweetsMade, errorCount, numberOfFollowers, lastFollowers):
    dmBody = file.open("dmBody.txt", 'r+')
    dmBody.write("Good evening sir, " + '\n')
    dmBody.write("Today I tweeted " + str(numberOfTweetsMade) + " times." + '\n')
    grossFollowChange = numberOfFollowers - lastFollowers
    if errorCount == 0:
        dmBody.write("I'm pleased to report I encountered zero errors.")
    else:
        dmBody.write("I encountered " + str(errorCount + " errors today.  Please see my log for more information." + '\n'))
    dmBody.write("I currently have " + str(numberOfFollowers) + "followers." )
    if numberOfFollowers > lastFollowers:
        dmBody.write("I'm pleased to report that I gained " + str(grossFollowChange) + " today+ + '\n")
    if numberOfFollowers < lastFollowers:
        dmBody.write("I lost " + str(abs(grossFollowChange)) + " followers today." + '\n')
    else:
        dmBody.write("I had no change in my follower count today." + '\n')
    dmBody.write("That is all for today, sir.  Please consult my log for more detail and have a good evening.")
    api.send_direct_message(user, dmBody.read())
    dmBody.close()


def sendErrorDM(api, errorMessage, errorCount):  # api is the api being used, and error message is the exception caught
    activationTime = time.time()
    if time.time() - activationTime > 86400:  # basically, if the time seperating the two is greater than 1 day
        errorCount = 0
    errorCount += 1
    greeting = "Hello, I've encountered an error."
    error = "The error is: " + str(errorMessage) + "."
    errorTime = "The error was encountered at " + str(time.strftime("%a %b %Y %I:%M:%S %p %z", time.localtime())) + "."
    dmBody = greeting + '\n' + error + '\n' + errorTime
    api.send_direct_message(user, dmBody)

