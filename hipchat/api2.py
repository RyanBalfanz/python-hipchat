#!/usr/bin/env/python3
import os

import requests


API_BASE_URL = "https://api.hipchat.com/v2"
AUTH_TOKEN = os.environ.get("HIPCHAT_API_TOKEN")


class HipChatClient(object):
	def __init__(self, api_token):
		super(HipChatClient, self).__init__()
		self.api_token = api_token
		
		session = requests.Session()
		session.headers.update({"Authorization": "Bearer " + self.api_token})
		self.session = session

	def get_resource(self, path):
		return API_BASE_URL + path

	def get(self, *args, **kwargs):
		return self.session.get(*args, **kwargs)

	def auth_test(self, *args, **kwargs):
		url = self.get_resource("/room")
		return self.get(url, params={"auth_test": True})

	def get_rooms(self):
		resource = self.get_resource("/room")
		return self.get(resource)


def main():
	if not AUTH_TOKEN:
		raise RuntimeError("HIPCHAT_API_TOKEN is not set")
	client = HipChatClient(AUTH_TOKEN)
	print(client.auth_test().text)

if __name__ == '__main__':
	main()
