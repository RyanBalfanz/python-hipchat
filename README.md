python-hipchat
==============

Command Line Tool for HipChat

Installation
------------

	pip install python-hipchat && hc

Configuration
-------------

If your configuration file is not found by the `hc` command, it will guide you though creating one. The default configuration is in ``~/.hipchat.cfg``.

The configuration file is of the form:

	[hipchat]
	api_token = abc123
	room_name = cool_room ; This is the default room alias, one of the room aliases listed below.
	
	[rooms]
	cool_room = 123
	
	[message_sender]
	alias = ryan
	color = random ; gray, green, purple, red, yellow, random

Usage
-----

Simple message sending:

	hc "Hi, from Python-HipChat"

Altering the sender's name and specifying the room alias:

	hc --user "Dr. Nick" --room cool_room "Hi, everybody!"