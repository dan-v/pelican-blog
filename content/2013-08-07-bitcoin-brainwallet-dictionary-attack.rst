Dictionary Attack on Bitcoin Brainwallets
#########################################

:date: 2013-08-08 21:00
:tags: bitcoin,bruteforce,script,python
:category: Project
:author: Dan

I wanted to create a simple program that would take a dictionary word, convert it into a bitcoin address, and then check to see if any bitcoin transactions had ever taken place with this address. I was curious to see how many insecure brainwallets existed.

I was able to borrow the bitcoin address generation code_ and had initially planned to point it at blockexplorer.com_ but then realized that this would probably end up flooding the site with traffic. It also appeared to be possible to get address information from a local bitcoin server (using JSON-RPC), but it was fairly slow. I then moved on to setting up a blockexplorer of my own called Abe_. After getting it up and running, it took over a week to insert all transactions into the database from the blockchain.

It was then just a matter of finding a simple dictionary_ file and writing a script to:

- Convert a word into public/private bitcoin addresses
- Check with local Abe server using HTTP request to see if any bitcoins had ever been received to this public address. 
- Print output and save to file any addresses that had transactions take place.

You can find the script on Github_.

.. _blockexplorer.com: http://blockexplorer.com/
.. _code: https://github.com/weex/addrgen/blob/master/addrgen.py
.. _Abe: https://github.com/jtobey/bitcoin-abe 
.. _Github: https://github.com/dan-v/bruteforce-bitcoin-brainwallet
.. _dictionary: http://downloads.skullsecurity.org/passwords/english.txt.bz2

Here are the addresses I found with this particular dictionary. Apparently this dictionary has duplicate words, so a little cleanup was required.

.. code-block:: text

	Word         Received Bitcoins  Public Address                     
	a            0.01               1HUBHMij46Hae75JPdWjeZ5Q7KaL7EFRSD 
	cat          0.15               162TRPRZvdgLVNksMoMyGJsYBfYtB4Q8tM 
	chicken      0.001              15Z16yvxv3oH6FBd83qkgo8AmzYcaSy2vX 
	destruction  0.09               11p4664ndnKmiPBL6naW9nF9z91skDdkf  
	dog          0.01               19MxhZPumMt9ntfszzCTPmWNQeh6j6QqP2 
	hangzhou     0.2                1EaUxkWMQ1kGPh3gWLev3Uzb2MUEmP59ws 
	love         0.012              1Mm6ouhpHqbtahCRNYfTo7Art1fbmk7PcR 
	password     0.06108            16ga2uqnF1NqpAuQeeg7sTCAdtDUwDyJav 
	poop         0.001              1LVL6qEhMQTbNtSBDfBkmzo5ZS1PwaKZWs 
	root         0.001              148qEts4TkouGRwvUMRFM8dB9MjxM6iCuN 
	sausage      0.01               1TnnhMEgic5g4ttrCQyDopwqTs4hheuNZ  
	supper       0.002              16rAKW1gUqtQL8PaaYM2Drkitm686kgdEC 
	swordfish    0.00144271         1PG9p4dG3vhZ8gx19aVdu5ZfECw9Q7N3B6 
	test         0.0511876          1HKqKTMpBTZZ8H5zcqYEWYBaaWELrDEXeE 
	very         0.0075             16NpdGeEeEebivqHGSXeDCjozr9yKHeZPD 
	wang         0.0001             1AjzxqeicCxMYDSAW5xqk1is3KX8eipD82 
	you          0.01               1NGj2UvhbC79ZXFBPBaXSmf7vwRy7cXK5R 

