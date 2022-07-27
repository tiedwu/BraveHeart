#import enemy

# damage = (me_ap - one_av * 0.9) - one_bv + me_fdi * me_ap
# hp_remain = current_hp - damage

import random


class Player():
	def __init__(self, max_hp=100, hp=100, ap=10, av=10, bv=10, fdi=10, cc=10, cd=10):
		self.ap = ap
		self.av = av
		self.bv = bv
		self.fdi = fdi
		#self.hp = hp
		self.max_hp = max_hp
		self.current_hp = hp

		self.cc = cc
		self.cd = cd

	def set_ap(self, ap):
		self.ap = ap

	def set_av(self, av):
		self.av = av

	def set_bv(self, bv):
		self.bv = bv

	def set_fdi(self, fdi):
		self.fdi = fdi

	def set_hp(self, hp):
		self.current_hp = hp

	def set_maxhp(self, maxhp):
		self.max_hp = maxhp

	def set_cc(self, cc):
		self.cc = cc

	def set_cd(self, cd):
		self.cd = cd

#class Enemy():
	#pass

class Combat():
	def __init__(self, player):
		self.player = player
		#self.enemy = enemy

	def set_player(self, player):
		self.player = player

	def set_enemy(self, enemy):
		self.enemy = enemy

	def set_im(self, im):
		self.im = im

	def calc(self):
		result = {'hp': 0, 'gold': 0, 'items': []}
		win = True
		while True:

			# hit from me to enemy
			one_damage = self.player.ap - self.enemy.av * 0.9 - \
				self.enemy.bv + self.player.fdi/100 * self.player.ap

			one_damage = 1 if one_damage < 1 else int(one_damage)
			print("hit point from me: ", one_damage)
			self.enemy.current_hp = self.enemy.current_hp - one_damage

			if self.enemy.current_hp <= 0:
				win = True
				break

			# hit from enemy to me
			me_damage = self.enemy.ap - self.player.av * 0.9 - \
				self.player.bv + self.enemy.fdi/100 * self.enemy.ap

			me_damage = 1 if me_damage < 1 else int(me_damage)
			print("hit point from enemy: ", me_damage)
			self.player.current_hp = self.player.current_hp - me_damage

			if self.player.current_hp <= 0:
				win = False
				break

		self.player.current_hp -= 1 
		result['hp'] = int(self.player.current_hp)
		if result['hp'] < 0:
			result['hp'] = 0

		if win:
			# instance: gold + drops
			# westfall: gold
			# trial: gold + drops(bead, rank=5 独特 item)
			# starship: gold + drops( rank=6 不朽-I/7 不朽-II(TBD) )

			low = (self.enemy.lv -1) * 70
			max = self.enemy.lv * 100
			result['gold'] = random.randint(low, max)

			if self.enemy.where == 'westfall':
				result['gold'] = 2 * result['gold'] 
			# get drops and gold

			if self.get_chance():
				all = ['weapon', 'suit', 'necklace', 'ring']
				if self.enemy.where == 'instance':
					ranks = [2, 3, 4, 5]
				elif self.enemy.where == 'trial':
					ranks = [5]
				elif self.enemy.where == 'starship':
					ranks = [6]
				item = self.im.random_eq(all, self.enemy.lv, 1, ranks)
				result['items'].append(item)
		return result

	def get_chance(self):
		n = random.randint(1, 100)
		if n >= 50:
			return True

		return False

if __name__ == '__main__':
	import enemy
	from item_manage import ItemManager
	#player = Player(hp=1000, ap=998, av=1000, bv=100, fdi=60)
	player = Player()
	enemy = enemy.Enemy(lv=110)
	combat_model = Combat(player)
	combat_model.set_enemy(enemy)
	combat_model.set_im(ItemManager(db='data/item.json'))
	#combat_model.set_player(player)
	#combat_model.set_enemy(enemy)
	print(combat_model.calc()) 
