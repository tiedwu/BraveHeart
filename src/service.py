from kivy.utils import platform
from time import sleep

from oscpy.server import OSCThreadServer
from oscpy.client import OSCClient

import json

# data init
import init_data

from item_manage import ItemManager
import combat
import enemy

CLIENT = OSCClient('localhost', 3102)

class GameService(OSCThreadServer):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.listen('localhost', port=3100, default=True)
		self.bind(b'/instance_challenge', self.instance_challenge)
		self.bind(b'/item_swap', self.item_swap)

		#self.bind(b'/try_gold', self.try_gold)

		#self.init_data()
		#hp = self.profile_data['current_hp']

		#print("service_init() ", hp)
		self.player = combat.Player()
		#self.bind(b'/set_player', self.set_player)

		#enemy_obj = enemy.Enemy()
		#self.combat_model = combat.Combat(self.player)
		#self.combat_model.set_im(self.im)

		# define mobs
		enemy_inst1, enemy_inst2 = enemy.Enemy(), enemy.Enemy()
		enemy_inst3, enemy_inst4 = enemy.Enemy(), enemy.Enemy()
		boss_inst = enemy.Boss()
		enemy_west1, enemy_west2 = enemy.Enemy_Westfall(), enemy.Enemy_Westfall()
		enemy_west3, enemy_west4 = enemy.Enemy_Westfall(), enemy.Enemy_Westfall()
		boss_west = enemy.Boss_Westfall()
		enemy_trial1, enemy_trial2 = enemy.Enemy_Trial(), enemy.Enemy_Trial()
		enemy_trial3, enemy_trial4 = enemy.Enemy_Trial(), enemy.Enemy_Trial()
		boss_trial = enemy.Boss_Trial()
		enemy_star1, enemy_star2 = enemy.Enemy_Starship(), enemy.Enemy_Starship()
		enemy_star3, enemy_star4 = enemy.Enemy_Starship(), enemy.Enemy_Starship()
		boss_star = enemy.Boss_Starship()
		enemies_inst = [enemy_inst1, enemy_inst2, enemy_inst3, enemy_inst4, \
							boss_inst]
		enemies_west = [enemy_inst1, enemy_west2, enemy_west3, enemy_west4, \
							boss_west]
		enemies_trial = [enemy_trial1, enemy_trial2, enemy_trial3, \
							enemy_trial4, boss_trial]
		enemies_star = [enemy_star1, enemy_star2, enemy_star3, enemy_star4, \
							boss_star]
		self.enemies = {'instance': enemies_inst, 'westfall': enemies_west, \
						'trial': enemies_trial, 'starship': enemies_star}

		self.current_enemies = self.enemies['instance']

		# n mobs
		self.index_enemy = 0

		self.bind(b'/fighting', self.check_fight)

	def set_player(self, max_hp, cur_hp, ap, av, bv, fdi, cc, cd):
		self.player.set_hp(int(cur_hp.decode('utf8')))
		self.player.set_maxhp(int(max_hp.decode('utf8')))
		self.player.set_ap(int(ap.decode('utf8')))
		self.player.set_av(int(av.decode('utf8')))
		self.player.set_bv(int(bv.decode('utf8')))
		self.player.set_fdi(int(fdi.decode('utf8')))
		self.player.set_cc(float(cc.decode('utf8')))
		self.player.set_cd(float(cd.decode('utf8')))

		self.combat_model.set_player(self.player)

	def instance_challenge(self, instance, lv, max_hp, cur_hp, ap, av, \
			bv, fdi, cc, cd):
		print("service(): instance_challenge()")

		self.profile_data['current_instance_level'] = int(lv.decode('utf8'))
		self.profile_data['current_instance'] = instance.decode('utf8')

		print(self.profile_data['current_instance'])
		self.save_data()

		#self.profile_data['current_hp'] = int(hp.decode('utf8'))
		self.set_player(max_hp, cur_hp, ap, av, bv, fdi, cc, cd)

		#self.check_fight()

	def try_gold(self):
		self.fight()

	def init_data(self):
		#init_data.check()
		if platform == 'android':
			self.data_path = '/storage/emulated/0/BraveHeart/data'
		else:
			self.data_path = 'data'

		self.profile_path = f'{self.data_path}/profile.json'
		self.item_path = f'{self.data_path}/item.json'

		print(f'[Service]loading profile: {self.profile_path}')
		print(f'[Service]loading item: {self.item_path}')

		with open(self.profile_path, "r") as f:
			self.profile_data = json.load(f)

		#with open(self.item_path, "r") as f:
		self.im = ItemManager(db=self.item_path)

		print(self.profile_data)
		#print(self.item_data)

		self.combat_model = combat.Combat(self.player)
		self.combat_model.set_im(self.im)

		# send ready to main
		CLIENT.send_message(b'/init_done', [])


	def fight(self, obj):

		# damage:
		self.combat_model.set_enemy(obj)
		result = self.combat_model.calc()
		return result

	def reset_enemies(self):
		self.index_enemy = 0

	def check_fight(self, index):
		#print("do_fight()")
		instance = self.profile_data['current_instance']
		#instance = 'instance'
		level = self.profile_data['current_instance_level']
		#level = 200
		self.current_enemies = self.enemies[instance]

		enemy_index = int(index.decode('utf8'))

		#obj = self.current_enemies[self.index_enemy]
		obj = self.current_enemies[enemy_index]

		obj.set_lv(level)
		result = self.fight(obj)
		print(f'fight to [{self.index_enemy}] enemy', result)

		if not result['result']:
			damage = str(self.player.max_hp).encode('utf8')
			win = 'False'
		else:
			damage = str(result['damage']).encode('utf8')
			win = 'True'

		self.index_enemy += 1
		if self.index_enemy >= 5:
			self.index_enemy = 0

		# deal result
		self.profile_data['gold'] += result['gold']
		EQALL = ['weapon', 'suit', 'necklace', 'ring']
		#print((result['items'][0][0]['kind']) in EQALL)

		bag_index = -1
		item_name = ''
		if result['items'] != []:
			if (result['items'][0][0]) and (result['items'][0][0]['kind']) in EQALL:
				item_name = result['items'][0][0]["name"]
				self.profile_data['bag'].append(result['items'][0])
				bag_index = len(self.profile_data['bag']) - 1

		# set cur_hp
		#self.player.set_hp(result['hp'])

		gold = str(result['gold']).encode('utf8')
		where = instance.encode('utf8')
		instance_level = str(level).encode('utf8')
		who = str(obj.get_name()).encode('utf8')

		print("BAG_INDEX: ", bag_index)
		bag_index_str = str(bag_index).encode('utf8')
		item_name_str = str(item_name).encode('utf8')

		win = win.encode('utf8')

		# save data
		self.save_data()

		CLIENT.send_message(b'/fight_report', [win, gold, damage, where, \
			instance_level, who, bag_index_str, item_name_str])


	def item_swap(self, index):
		index_decode = int(index.decode('utf8'))
		print(f'[service.py]item_swap({index_decode})')

		item = self.profile_data['bag'][index_decode][0]

		kind = item['kind']
		equipped = self.profile_data['equipped'][kind]
		temp = []
		temp.append(equipped)
		self.profile_data['bag'][index_decode] = temp
		self.profile_data['equipped'][kind] = item
		self.save_data()

		# item activate
		CLIENT.send_message(b'/item_activate', [])

	def check_data(self):
		self.save_data()

	def save_data(self):
		with open(self.profile_path, "w", encoding='utf-8') as f:
			json.dump(self.profile_data, f, indent=4, ensure_ascii=False)
		print('save done')

	def gold_test(self):
		self.profile_data['gold'] += 1

		gold = str(self.profile_data['gold']).encode('utf8')

		# to main
		CLIENT.send_message(b'/gold_test', [gold])

		print(f'GOLD: {self.profile_data["gold"]}')

if __name__ == '__main__':
	loop = 0

	server = GameService()

	server.init_data()

	while True:
		print(f'[{loop}]service running...')
		loop += 1
		#server.gold_test()
		#if loop % 10 == 0:
			#server.check_fight()
		sleep(1)
