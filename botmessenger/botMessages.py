import tweepy  # what in the sweet christmas causes this error
from keys import Keys
from botFunctions import *
import dailyInfo

auth = tweepy.OAuthHandler(Keys.consumerKey, Keys.consumerKeySecret)
auth.set_access_token(Keys.accessToken, Keys.accessTokenSecret)

# Spinning Up

api = tweepy.API(auth)
print "Current user is: " + str(api.me().name)


# first time setup, to be called outside of a "forever" loop
def initialSetup(api, user):
    info = dailyInfo.DailyInfo()
    info.dailyFlag = time.time()
    info.errorCount, info.tweetCount = 0, 0
    info.oldFollowers = api.followers(api.me().name)
    info.newFollowers = 0
    info.user = user
    return info


# set needed variables for running
def dailySetup(activationTime, oldFollowerCount):
    currentTime = hourGetter()
    info = dailyInfo.DailyInfo()
    if (time.time() - info.dailyFlag > 86400) and (currentTime + 1 == activationTime) or (currentTime - 1 == activationTime):
        info.errorCount = 0
        info.tweetCount = 0
        info.dailyFlag = time.time()
        info.oldFollowers = oldFollowerCount
        info.newFollowers = api.followers(api.me().name)
    return info


# Send nightly DM to bot manager specified by user parameter
def sendNightlyDM(api, info, user):
    dmBody = file.open("dmBody.txt", 'r+')
    dmBody.write("Hello, " + '\n')
    dmBody.write("Today I tweeted " + str(info.tweetCount) + " times." + '\n')
    grossFollowChange = info.newFollowers - info.oldFollowers
    if info.errorCount == 0:
        dmBody.write("I'm pleased to report I encountered zero errors.")
    else:
        dmBody.write("I encountered " + str(info.errorCount + " errors today.  Please see my log for more information." + '\n'))
    dmBody.write("I currently have " + str(info.newFollowers) + "followers.")
    if info.newFollowers > info.oldFollowers:
        dmBody.write("I'm pleased to report that I gained " + str(abs(grossFollowChange)) + " today+ + '\n")
    if info.newFollowers < info.oldFollowers:
        dmBody.write("I lost " + str(abs(grossFollowChange)) + " followers today." + '\n')
    else:
        dmBody.write("I had no change in my follower count today." + '\n')
    dmBody.write("That is all for today, sir.  Please consult my log for more detail and have a good evening.")
    api.send_direct_message(user, dmBody.read())
    dmBody.close()


def sendErrorDM(api, info, user, errorMessage):  # api is the api being used, and error message is the exception caught
    activationTime = time.time()
    if time.time() - activationTime > 86400:  # basically, if the time seperating the two is greater than 1 day
        info.errorCount = 0
    info.errorCount += 1
    greeting = "Hello, I've encountered an error."
    error = "The error is: " + str(errorMessage) + "."
    errorTime = "The error was encountered at " + str(time.strftime("%a %b %Y %I:%M:%S %p %z", time.localtime())) + "."
    dmBody = greeting + '\n' + error + '\n' + errorTime
    api.send_direct_message(user, dmBody)

