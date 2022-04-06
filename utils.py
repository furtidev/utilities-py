# Libraries
import json
import requests

# Main Class
class utils:
	def __init__(self) -> None:
		pass
	
	def use_rest_api(self, url: str):
		response = requests.get(url)
		return response.json()
