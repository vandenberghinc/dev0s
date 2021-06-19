
# imports.
from dev0s.classes.defaults.files import Date
from dev0s.classes.response import response as _response_
import json, requests

# the telgram object.
class Telegram(object):
	def __init__(self,
		# your telegram bot token.
		token=None,
	):

		# check params.
		response = _response_.parameters.check({
			"token:str":token,
		})
		if not response.success: response.crash()

		# attributes.
		self.token = token

	# read telegram messages.
	def read(self, 
		# optionally specify a chat id (str).
		chat_id=None,
	):

		# request.
		response = self.__request__(f"https://api.telegram.org/bot{self.token}/getUpdates")
		#response = self.__request__(f"https://api.telegram.org/bot{self.token}/getMessages")
		if not response.success: return response
		response = response["response"]

		# read all messages.
		messages = {}
		for response_data in response['result']:

			# parse.
			from_ = response_data["message"]["from"]
			chat = response_data["message"]["chat"]
			date = Date().from_seconds(response_data["message"]["date"])
			message = response_data["message"]["text"]

			# append.
			try: messages[chat['id']]
			except KeyError: messages[chat['id']] = {}
			messages[chat['id']][str(date)] = {
				"message":message,
				"date":str(date),
				"from":from_,
				"chat":chat,
			}
		
		# handler.
		if chat_id == None:
			return _response_.success("Successfully retrieved the messages.", {
				"messages":messages,
			})
		else:
			try:
				messages = messages[chat_id]
			except KeyError:
				messages = {}
			return _response_.success(f"Successfully retrieved the messages from chat {chat_id}.", {
				"messages":messages,
			})

		#

	# send a telegram message.
	def send(self, 
		# the message to send (str).
		message=None, 
		# the chat id where the message will be sent to.
		chat_id=None,
		# the message title.
		title=None,
	):

		# check params.
		response = _response_.parameters.check({
			"message:str":message,
			"chat_id:str":chat_id,
		})
		if not response.success: return response

		# clean msg.
		message = message.replace('[', '(').replace(']', ')')

		# make request.
		if title not in [None, False, "", "null", "NaN"]:
			message = f"*{title}*\n" + message
		response = self.__request__(f"https://api.telegram.org/bot{self.token}/sendMessage?chat_id={chat_id}&parse_mode=Markdown&text={message}")
		if not response.success: return response

		# handler.
		return _response_.success(f"Successfull send the message to {chat_id}.")

		#

	# make an request.
	def __request__(self, url: str, serialize=True):
		# make request.
		response = requests.get(url)

		# check status code.
		if response.status_code != 200:
			return _response_.error(f"Invalid request ({url}) [{response.status_code}]: {response.text}.")

		# serialize.
		if serialize:
			try: response = response.json()
			except: 
				return _response_.error(f"Failed to serialize response: {response.text}.")

		# handler.
		return _response_.success("Successfull request", {
			"response":response,
		})

		#

	#

