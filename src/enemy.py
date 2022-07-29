
# ap, av, bv, fdi(Boss)
# damage = (me_ap - one_av * 0.9) - one_bv + me_fdi * me_ap
# hp_remain = current_hp - damage

class Enemy():
	def __init__(self, lv=1):
		self.where = 'instance'
		self.lv = lv

		self.max_hp = self.lv * 15
		self.current_hp = self.max_hp
		self.ap = self.lv * 10
		self.av = self.lv * 5
		self.bv = self.lv * 0
		self.fdi = self.lv * 0
		self.name = '小幽灵'

	def set_lv(self, lv):
		self.lv = lv

	def reset(self):
		self.current_hp = self.max_hp

	def get_name(self):
		return self.name

class Boss(Enemy):
	def __init__(self, lv=1):
		super().__init__(lv)

		self.max_hp = self.lv * 25
		self.current_hp = self.max_hp
		self.ap = self.lv * 20
		self.av = self.lv * 10
		self.bv = self.lv * 5
		#self.fdi = self.lv * 0
		self.name = '幽灵队长'

class Enemy_Westfall(Enemy):
	def __init__(self, lv=1):
		super().__init__(lv)
		self.where = 'westfall'
		self.lv = lv

		self.max_hp = self.lv * 17
		self.current_hp = self.max_hp
		self.ap = self.lv * 12
		self.av = self.lv * 7
		self.bv = self.lv * 3
		self.name = '荒野幽灵'
		#self.fdi = self.lv * 0

class Enemy_Trial(Enemy):
	def __init__(self, lv=1):
		super().__init__(lv)
		self.where = 'trial'
		self.lv = lv

		self.max_hp = self.lv * 25
		self.current_hp = self.max_hp
		self.ap = self.lv * 20
		self.av = self.lv * 10
		self.bv = self.lv * 5
		self.name = '试炼幽灵'
		#self.fdi = self.lv * 0

class Enemy_Starship(Enemy):
	def __init__(self, lv=1):
		super().__init__(lv)
		self.where = 'starship'
		self.lv = lv

		self.max_hp = self.lv * 30
		self.current_hp = self.max_hp
		self.ap = self.lv * 25
		self.av = self.lv * 20
		self.bv = self.lv * 15
		self.fdi = self.lv * 2
		self.name = '星舰幽灵'

class Boss_Westfall(Boss):
	def __init__(self, lv=1):
		super().__init__(lv)
		self.where = 'westfall'
		self.lv = lv

		self.max_hp = self.lv * 30
		self.current_hp = self.max_hp
		self.ap = self.lv * 25
		self.av = self.lv * 10
		self.bv = self.lv * 10
		self.fdi = self.lv * 1
		self.name = '荒野幽灵队长'

class Boss_Trial(Boss):
	def __init__(self, lv=1):
		self.where = 'trial'
		self.lv = lv

		self.max_hp = self.lv * 45
		self.curren_hp = self.max_hp
		self.ap = self.lv * 35
		self.av = self.lv * 25
		self.bv = self.lv * 15
		self.fdi = self.lv * 10
		self.name = '试炼幽灵队长'

class Boss_Starship(Boss):
	def __init__(self, lv=1):
		super().__init__(lv)
		self.where = 'starship'
		self.lv = lv

		self.max_hp = self.lv * 40
		self.curren_hp = self.max_hp
		self.ap = self.lv * 30
		self.av = self.lv * 30
		self.bv = self.lv * 20
		self.fdi = self.lv * 7
		self.name = '星舰幽灵队长'

if __name__ == '__main__':
	boss = Boss_Starship(lv=100)
	print(boss.get_name())
