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
			else:
				dir = os.path.join(dir, 'data')

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
		suit = im.get_init_eq('suit')
		necklace = im.get_init_eq('necklace')
		ring = im.get_init_eq('ring')

		profile_data = {
						'level': 1, # 等级
						'samsara': 0, # 轮回
						'reincarnation': 0, # 转生
						'bhp': 32668, 'hp': 0, # 基础生命值(base health point) bhp 生命值(health point) hp
						'bap': 11671, 'ap': 0, # 基础攻击力(base attack point) bap，攻击力(attack point) ap
						'bcc': 0, 'cc': 0, # 基础暴击(base crit chance) bcc， 暴击(crit chance) cc
						'bcd': 0, 'cd': 0, # 基础暴伤(base crit damage) bcd， 暴伤(crit damage) cd
						'bav': 2113, 'av': 0, # 基础护甲值(base armor value) bav， 护甲值(armor value) av
						'bbv': 4120, 'bv': 0, # 基础格挡值(base block value) bbv， 格挡值(block value) bv
						'eec': 0, # 强化概率额外加成(enforce extra chance) eec
						'bie': 0, # 装备初始强化等级(base item enforce) bie
						'hprps': 0, # 每秒生命回复(health point recover per second) hprps
						'goc': 0, # 金币获取率(gold obtain chance) goc
						'ioc': 0, # 装备爆率(item obtain change) ioc
						'rptr': 0, # 转生点获取倍率(reincarnation point transformation ratio) rptr
						'paff': 0, # 宠物杀敌属性获取(pet attributes from fighting) paff
						'fdi': 0, # 最终伤害提升(final damage increment) fdi
						'cs': 0, # 挑战速度加快(challenge speedup) cs
						'apir': 0, # 攻击提升百分比(attack point increment ratio) apir
						'avir': 0, # 护甲提升百分比(armor value increment ratio) avir
						'hpir': 0, # 生命提升百分比(health point increment ratio) hpir
						'bvir': 0, # 格挡提升百分比(block value increment ratio) bvir
						'drp': 0, # 减伤比例(damage reduce proportion) drp
						'dops': 0, # 每秒输出伤害(damage output per second) dops
						'ce': 0, # 战斗力(combat effectiveness) ce
						'gold': 0,
						'equipped': {'weapon': weapon, 'suit': suit,
						'necklace': necklace, 'ring': ring},
						'bag': [],
						'crystal': 0,
						'current_hp': 0,
						'current_instance': '',
						'current_instance_level': 0,
						}

		print('creating profile_file: ', profile_file)
		with open(profile_file, 'w', encoding='utf-8') as f:
			json.dump(profile_data, f, indent=4, ensure_ascii=False)
