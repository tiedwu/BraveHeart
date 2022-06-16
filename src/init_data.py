from kivy.utils import platform
from kivy.logger import Logger

import os
import json

from item_manage import ItemManager 

def check():


	dir = 'data'
	profile_file = 'profile.json'
	item_file = 'item.json'
	INIT = False
	# /storage/emulated/0/BraveHeart/data/profile.json
	# /storage/emulated/0/BraveHeart/data/item.json
	if platform == 'android':
		from android.permissions import Permission, request_permissions
		from android.permissions import check_permission
		from android.storage import app_storage_path
		from android.storage import primary_external_storage_path
		from android.storage import secondary_external_storage_path

		perms = [Permission.WRITE_EXTERNAL_STORAGE,
					Permission.READ_EXTERNAL_STORAGE]

		def check_permissions(perms):
			for perm in perms:
				if check_permission(perm) != True:
					return False

			return True

		if check_permissions(perms) != True:
			request_permissions(perms)
			# app has to be restarted, permissions will be work on 2nd start
			exit()

		try:
			# check item_file
			dir = os.path.join(primary_external_storage_path(), 'BraveHeart')
			Logger.info(dir)
			if not os.path.isdir(dir):
				os.mkdir(dir)
				Logger.info(f'created directory {dir}')

				dir = os.path.join(dir, 'data')
				os.mkdir(dir)
				Logger.info(f'created directory {dir}')

			# copy item.json
			import shutil
			origin = 'data/item.json'
			shutil.copy(origin, dir)
			Logger.info(f'item data copied')

			# set profile_file, item_file
			item_file = os.path.join(dir, item_file)
			profile_file = os.path.join(dir, profile_file)

			INIT = True

		except:
			Logger.info('missing permissions?')

	# data/profile.json
	# data/item.json
	elif platform in ('linux', 'win'):
		if not os.path.isdir(dir):
			print('data not found')
			return
		item_file = os.path.join(dir, item_file)
		if not os.path.isfile(item_file):
			print('data not found')
			return
		profile_file = os.path.join(dir, profile_file)
		if not os.path.isfile(profile_file):
			print('create profile.json')
			INIT = True

	if INIT:
		im = ItemManager(db=item_file)
		weapon = im.get_init_eq('weapon')
		suit = im.get_init_eq('armor')
		necklace = im.get_init_eq('necklace')
		ring = im.get_init_eq('ring')

		profile_data = {'equipped': {'weapon': weapon, 'suit': suit,
						'necklace': necklace, 'ring': ring}}

		print('profile_file: ', profile_file)
		with open(profile_file, 'w', encoding='utf-8') as f:
			json.dump(profile_data, f, indent=4, ensure_ascii=False)
