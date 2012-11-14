import logging
import os
import urllib
import urllib2

from hipchat.constants import HIPCHAT_ROOM_MESSAGE_URL, HIPCHAT_SENDER_MAX_LENGTH
from hipchat.utils import ensure_config


HIPCHAT_API_TOKEN = os.getenv("HIPCHAT_API_TOKEN", None)

if not HIPCHAT_API_TOKEN:
	CONFIG = ensure_config()
	HIPCHAT_API_TOKEN = CONFIG.get("hipchat", "api_token")

logger = logging.getLogger(__name__)

def send_message_to_room(message, room_id, api_token=HIPCHAT_API_TOKEN, sender="Python-HipChat", color="random"):
	"""
	Sends a message to a HipChat room.
	"""
	if not room_id:
		raise ValueError("Cannot send HipChat message to room {r}".format(r=room_id))

	truncateSender = False
	if len(sender) > HIPCHAT_SENDER_MAX_LENGTH:
		logMessage = "Sender {sender} cannot be greater than {n} characters"
		logMessage = errorMessage.format(sender=sender, n=HIPCHAT_SENDER_MAX_LENGTH)
		logger.info(logMessage)
		if truncateSender:
			logMessage = "Truncating {sender} to {numChars} characters"
			logger.info(logMessage.format(sender=sender), numChars=HIPCHAT_SENDER_MAX_LENGTH)
			sender = sender[:HIPCHAT_SENDER_MAX_LENGTH]
		else:
			raise ValueError(logMessage)

	postData = {
		"auth_token": api_token,
		"room_id": room_id,
		"from": sender,
		"message": message,
		"notify": 1,
		"color": color,
	}

	response = None
	data = urllib.urlencode(postData)
	try:
		request = urllib2.Request(HIPCHAT_ROOM_MESSAGE_URL, data)
	except urllib2.URLError, e:
		errorMessage = "Caught an URLError while posting to HipChat room {room}: {error}"
		logger.error(errorMessage.format(room=room_id), error=e)
		raise
	else:
		try:
			response = urllib2.urlopen(request)
		except Exception, e:
			errorMessage = "Caught an Exception while posting to HipChat room {room}: {error}"
			logger.exception(errorMessage.format(room=room_id, error=e))
			raise
		else:
			logMessage = "Response from HipChat: {resp}"
			logger.debug(logMessage.format(resp=response.read()))

	return response.read()
