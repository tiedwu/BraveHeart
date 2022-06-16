from kivy.utils import platform
from time import sleep

from oscpy.server import OSCThreadServer
from oscpy.client import OSCClient

import json

# data init
#import init_data


CLIENT = OSCClient('localhost', 3102)

class GameService(OSCThreadServer):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

	def init_items(self):
		#init_data.check()
		pass


if __name__ == '__main__':
	loop = 0

	server = GameService()

	server.init_items()

	while True:
		print(f'[{loop}]service running...')
		loop += 1
		sleep(1)
