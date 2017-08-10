<!DOCTYPE html>

<h1>botMessenger</h1>

<h2>Introduction</h2>
<p>Bot Messenger is a project created by John Williams using the <a href = "http://www.tweepy.org/"> tweepy Python libary</a>.  This
    project is designed for people who have both a twitter bot and a "personal" twitter account.  Simply put, this allows
    your bot to direct message (DM) your personal account so that you can be alerted to things like changes in followers,
    errors and other actions without having to be constantly checking your bot.  It is meant for bot that are "forever on"
    typically using a type of loop that keeps the bot in a perpetual state of being on.  It is in active development, so 
    if you encounter any bugs, please let me know!</p>

<h2>Using botMessenger</h2>
<p>Bot Messenger is designed to work with your current twitter bot.  You'll need a bot already working to use it, using the
    tweepy library in Python.  So before you can use Bot Messenger, make sure you have the following:</p>
<ul>
    <li> A twitter bot, built in Python with the Tweepy Library</li>
    <li>The keys for your twitter bot, both consumer and access (keep these secret!)</li>
    <li>Stoke!</li>
</ul>

<h2>Getting started</h2>
<p>Ready to use Bot Messenger?  Bot Messenger requires a little setup to work with your bot.  Follow these steps to get started.</p>
<ol type = 1>
    <li><code>pip install botmessenger</code> to get the package</li>
    <li>Add the import statement to your bot:
        <code>import botMessenger</code></li>
    <li>Add in the functions wherever you see fit!  (with a few exceptions)</li>
</ol>

<h2>Using the setup functions</h2>
<p>Included in the API are two functions called <code>initialSetup</code> and <code>dailySetup</code>.  These two
functions set up many of the variables needed to run the other functions, and as such must be called in specific places
in the overall code of your twitter bot.  This is detailed in the section "Code Template" below.  Just remember, if you
want to use the other fucntions, you must use the setup functions first!</p>

<h2>Code Template</h2>
<pre><code>
auth = tweepy.OAuthHandler("Your keys here")
auth.set_access_token("Your tokens here")
api = tweepy.API(auth)
...Whatever code you want...
errorCount, tweetCount, dailyFlag, followers = initialSetup(api)
while True:  # this is the "forever" loop<br />
    errorCount, tweetCount, dailyFlag = dailySetup(activationTime, dailyFlag, errorCount, tweetCount)
    ...Your code here...</code></pre>
<p>If your using github or another VCS software, make sure you don't put these keys on your repo.  Keep them secret!
The <code>initialSetup</code> function gets the time the program is started (for timekeeping purposes), and declares
and initializes several other variables to zero for use.   The <code>dailySetup</code> function updates these values
everyday, at the hour specified by the variable <code>activationTime</code> (24 hour clock, within a +/- one hour range).</p>

<h2>A warning</h2>
<p>Please don't use this code in any malicous ways, such as to DM spam users.  Dont't send the DMs to anyone who hasn't
expressly consented to recieve them.  Doing so is a violation of Twitter's rules, and could result in punishment.  Curious
if you're breaking the rules?  Check out<a href = "https://support.twitter.com/articles/76915">Twitter's rules</a>on the
subject.  Basically, be nice and respectful.</p>

<h6>Made with love in Venice, California❤</h6>