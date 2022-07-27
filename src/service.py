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
		self.bind(b'/set_player', self.set_player)

		#self.bind(b'/try_gold', self.try_gold)

		self.init_data()
		#hp = self.profile_data['current_hp']
		#print("service_init() ", hp)
		self.player = combat.Player()
		#enemy_obj = enemy.Enemy()
		self.combat_model = combat.Combat(self.player)
		self.combat_model.set_im(self.im)

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

	def instance_challenge(self, hp, lv):
		print("service(): instance_challenge()", hp, lv)

		self.profile_data['current_hp'] = int(hp.decode('utf8'))
		self.profile_data['current_instance_level'] = int(lv.decode('utf8'))
		self.profile_data['current_instance'] = 'instance'

	def try_gold(self):
		self.fight()

	def init_data(self):
		init_data.check()
		if platform == 'andoid':
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

	def fight(self, obj):

		# damage:
		self.combat_model.set_enemy(obj)
		result = self.combat_model.calc()
		return result

	def reset_enemies(self):
		self.index_enemy = 0

	def check_fight(self):
		#print("do_fight()")
		instance = self.profile_data['current_instance']
		instance = 'instance'
		level = self.profile_data['current_instance_level']
		level = 200
		self.current_enemies = self.enemies[instance]
		obj = self.current_enemies[self.index_enemy]
		obj.set_lv(level)
		result = self.fight(obj)
		print(f'fight to [{self.index_enemy}] enemy', result)
		self.index_enemy += 1
		if self.index_enemy >= 5:
			self.index_enemy = 0

		# deal result
		self.profile_data['gold'] += result['gold']
		EQALL = ['weapon', 'suit', 'necklace', 'ring']
		#print((result['items'][0][0]['kind']) in EQALL)

		if result['items'] != []:
			if (result['items'][0][0]) and (result['items'][0][0]['kind']) in EQALL:
				self.profile_data['bag'].append(result['items'][0])

		# set cur_hp
		self.player.set_hp(result['hp'])

		hp = str(result['hp']).encode('utf8')
		gold = str(self.profile_data['gold']).encode('utf8')
		CLIENT.send_message(b'/fight_report', [gold, hp])

	def check_data(self):
		self.save_data()

	def save_data(self):
		with open(self.profile_path, "w", encoding='utf-8') as f:
			json.dump(self.profile_data, f, indent=4, ensure_ascii=False)

if __name__ == '__main__':
	loop = 0

	server = GameService()

	#server.init_data()

	while True:
		print(f'[{loop}]service running...')
		loop += 1
		server.check_data()
		if loop % 10 == 0:
			server.check_fight()
		sleep(1)
