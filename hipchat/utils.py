import ConfigParser
import os
import sys

from hipchat.constants import HIPCHAT_COLORS


DEFAULT_CONFIG_PATH = os.path.expanduser("~/.hipchat.cfg")

def config_exists(path=DEFAULT_CONFIG_PATH):
	return os.path.exists(path)

def ensure_config(path=DEFAULT_CONFIG_PATH):
	if not config_exists(path):
		config = setup_config(path)
		exitMessage = "Your config was saved to {cp}. You should add your HipChat rooms to it now."
		sys.exit(exitMessage.format(cp=DEFAULT_CONFIG_PATH))
	else:
		config = ConfigParser.ConfigParser()
		config.read(path)

	return config

def setup_config(path=DEFAULT_CONFIG_PATH):
	import getpass

	defaultRoomName = "room_alias"
	defaults = {
		"alias": getpass.getuser(),
		"color": "random",
		"room_name": defaultRoomName,
		"rooms": {
			defaultRoomName: "<room_id>"
		}
	}

	hipchatApiToken = raw_input("HipChat API Token: ")
	alias = raw_input("Alias ({default}): ".format(default=defaults["alias"]))
	print "Available Colors: {colors}".format(colors=" ".join(HIPCHAT_COLORS))
	color = raw_input("Color ({default}): ".format(default=defaults["color"]))

	config = ConfigParser.ConfigParser()

	config.add_section("rooms")
	config.set("rooms", defaults["room_name"], defaults["rooms"][defaultRoomName])

	config.add_section("message_sender")
	config.set("message_sender", "alias", alias or defaults["alias"])
	config.set("message_sender", "color",  color or defaults["color"])

	config.add_section("hipchat")
	config.set("hipchat", "api_token", hipchatApiToken)
	config.set("hipchat", "room_name", defaults["room_name"])

	with open(path, "wb") as f:
		config.write(f)

	return config
