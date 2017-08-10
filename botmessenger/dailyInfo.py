# class for status information


class DailyInfo:
    def __init__(self, errorCount, tweetCount, dailyFlag, oldFollowers, newFollowers, user):
        self.errorCount = errorCount
        self.tweetCount = tweetCount
        self.dailyFlag = dailyFlag
        self.oldFollowers = oldFollowers
        self.newFollowers = newFollowers
        self.user = user
