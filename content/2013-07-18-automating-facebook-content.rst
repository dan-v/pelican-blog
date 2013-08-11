Automated Facebook Voting
#########################################

:date: 2013-07-19 18:00
:tags: facebook,automation,script,python,javascript,bash
:category: Project
:author: Dan

There was recently a Facebook contest with users voting on pictures that people had submitted. The contest was hosted/provided by woobox.com. The contest rules stated you could vote once per day, so I was curious how this was being enforced. 

The first problem to workaround was a vote being tied to a logged in Facebook account, which meant a unique Facebook account would be needed for each vote. After not having any luck modifying the POST data on vote submission, I figured out that changing the browser user agent to an iPhone let me vote without being signed into facebook at all.

The next problem was that a unique IP address was required in order to submit a successful vote. I already had an OpenVPN provider, so I would just need to write some code to keep reconnecting and getting a new IP address. I also played around with TOR and learned that you can enable a control port and ask it to change your identity at will. Using both OpenVPN and TOR together would give me a larger number of IP addresses to work with.

The last piece to solve was the browser automation to submit the votes. My first search turned up PhantomJS_, a headless, scriptable browser with a JavaScript API.

.. _PhantomJS: http://phantomjs.org/

With these problems solved it was onto writing some scripts. It ended up being a mix of Bash, Python, and Javascript. You can find the code on Github_.

.. _Github: https://github.com/dan-v/automated-facebook-voting

The main bash script (start_automated_voting.sh_) does the following in an infinite loop.

- Connects to OpenVPN endpoint
- Runs PhantomJS automation
- Disconnects OpenVPN
- Changes TOR identity
- Runs PhantomJS automation again over TOR proxy

The browser automation with PhantomJS (phantomjs_vote.js_) does the following.

- Sets user agent to iPhone
- Opens woobox.com
- Takes a before screenshot
- Calls javascript function to vote
- Takes after screenshot
- Waits 10 seconds

The TOR identity changing script (change_tor_identity.py_) in Python does the following:

- Connects to TOR control port 9151 with password
- Sends 'SIGNAL NEWNYM' to force identity change

.. _start_automated_voting.sh: https://github.com/dan-v/automated-facebook-voting/blob/master/start_automated_voting.sh
.. _phantomjs_vote.js: https://github.com/dan-v/automated-facebook-voting/blob/master/phantomjs_vote.js
.. _change_tor_identity.py: https://github.com/dan-v/automated-facebook-voting/blob/master/change_tor_identity.py

That is all.
