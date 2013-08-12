Keep Mint.com In Sync With Value Of Bitcoins
############################################

:date: 2013-03-05 17:00
:tags: bitcoin,script,python
:category: Project
:author: Dan

Mint.com does not have support for tracking the value of Bitcoins. There is an open request_ to support this, but there has been no progress that I can see. 

I decided to take things into my own hands and create a script that would:

.. _request: https://satisfaction.mint.com/mint/topics/tracking_of_bitcoin_addresses

- Grab the bitcoin current market price in USD
- Find the current balance of bitcoin addresses
- Total this value up and post it to Mint.com

Script can be found on Github_.

.. _Github: https://github.com/dan-v/mint-bitcoin-sync

Usage: python mint_bitcoin_sync.py "<mint-login>" "<mint-password>" "<comma-separated-bitcoin-addresses>". Here is example output.

.. code-block:: text

	dan@ubuntu:~$ python mint_bitcoin_sync.py 

	Bitcoin addresses: 16ga2uqnF1NqpAuQeeg7sTCAdtDUwDyJav
	Mint email: myemail@gmail.com
	Password: 
	Bitcoin address '16ga2uqnF1NqpAuQeeg7sTCAdtDUwDyJav' has 11.05011651 BTC

	Total bitcoins for all addresses: 11.05011651 BTC
	Using 24 hour price: 104.02854 USD
	Current combined balance for all addresses: $1,149.53

	Press any key to update Mint with these details

	Updated Bitcoin account on mint with current balance: $1,149.53

