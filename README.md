<!DOCTYPE html>

<h1>botMessenger</h1>

<h2>Introduction</h2>
<p>Bot Messenger is a project created by John Williams using the <a href = "http://www.tweepy.org/"> tweepy Python libary</a>.  This
    project is designed for people who have both a twitter bot and a "personal" twitter account.  Simply put, this allows
    your bot to direct message (DM) your personal account so that you can be alerted to things like changes in followers,
    errors and other actions without having to be constantly checking your bot.  It is in active development, so if you encounter
    any bugs, please let me know!</p>

<h2>Using botMessenger</h2>
<p>Bot Messenger is designed to work with your current twitter bot.  You'll need a bot already working to use it, using the
    tweepy library in Python.  So before you can use Bot Messenger, make sure you have the following:</p>
<ul>
    <li> A twitter bot, built in Python</li>
    <li>The keys for your twitter bot, both consumer and access (keep these secret!)</li>
    <li>Stoke!</li>
</ul>

<h2>Getting started</h2>
<p>Ready to use Bot Messenger?  Bot Messenger requires a little setup to work with your bot.  Follow these steps to get started.</p>
<ol type = 1>
    <li>Clone/download this repo from github</li>
    <li>Add it to your twitter bot</li>
    <li>Naviagte to the directory where you've add Bot Messenger to your project</li>
    <li>Create a new python file called <code>keys.py</code></li> (case matters, see below for a copyable template)
    <li>Add the import statement to your bot:
        <code>import botMessenger</code></li>
    <li></li>
</ol>

<h2><code>keys.py</code> template</h2>
<pre><code> class Keys: <br />
    consumerKey = "Your consumer key here" <br />
    consumerKeySecret = "Your secret consumer key here" <br />
    accessToken = "Your access token here" <br />
    accessTokenSecret = "Your secret access token here" <br />
</code></pre>
<p>If your using github or another VCS software, make sure you don't put these keys on your repo.  Keep them secret!</p>

Made with love in Venice, California