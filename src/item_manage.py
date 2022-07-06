# 品质系数: QAC
# rank: 破旧, 普通, 神器, 史诗, 独特, 不朽I, 不朽II
# 品质: D, C, B, A, S, SS, SSS
# Ex: 破旧 普通D 普通 C, QAC = 1, 普通 A, QAC = 5, 神器 D, QAC = 13, 神器 A, QAC = 19
# Ex: 史诗 SS, QAC = 37, 史诗 A, QAC = 33, 史诗 C, QAC = 29
# Ex: 独特 B, QAC = 45
# 暴伤(damage): D(70%-75%), C(75%-80%), B(80%-85%), A(85%-90%), S(90%-95%), SS(95%-100%), SSS(100%-105%), 不朽I(105%-110%), 不朽II(110%-115%)
# 暴击(crit): D(11%), C(12%), B(13%), A(14%), S(15%-17%), SS(18%-20%), SSS(21%-23%), 不朽I(24%-26%), 不朽II(27%-29%)

DAMAGE = {'D': [70, 75], 'C': [75, 80], 'B': [80, 85], 'A': [85, 90],
			'S': [90, 95], 'SS': [95, 100], 'SSS': [100, 105]}

CRIT = {'D': [11, 12], 'C': [12, 13], 'B': [13, 14], 'A': [14, 15],
			'S': [15, 17], 'SS': [18, 20], 'SSS': [21, 23]}

# 随机属性
# 破旧: 1, 普通: 2, 神器: 3, 史诗: 4, 独特: 5
# EQ['wp'][0], EQ['armor'][0], EQ['necklace'][0], EQ['ring'][0]: 破旧, 其余普通开始

# implicit
# attack: [3, 6] * lv, attack(20% - 40%),
# armor: [3, 4] * lv, armor(20% - 40%),
# hp: [8, 11] * lv, hp(20% - 40%),
# block: [2, 4] * lv,
# damage(20 - 40%), crit(15% - 25%)
IMPLICIT = {'ATTACK': [300, 600], 'ATTACK_RATE': [2000, 4000],
			'ARMOR': [300, 400], 'ARMOR_RATE': [2000, 4000],
			'HP': [800, 1100], 'HP_RATE': [2000, 4000],
			'BLOCK': [200, 400], 'DAMAGE_RATE': [2000, 4000],
			'CRIT_RATE':[1500, 2500]}

QAC = {'1#1': 1, '1#2': 1, '1#3':1, '1#4': 1, '1#5': 1, '1#6': 1, '1#7': 1,
		'2#1': 1, '2#2': 1, '2#3': 3, '2#4': 5, '2#5': 7, '2#6': 9, '2#7': 11,
		'3#1': 13, '3#2': 15, '3#3': 17, '3#4': 19, '3#5': 21, '3#6': 23, '3#7': 25,
		'4#1': 27, '4#2': 29, '4#3': 31, '4#4': 33, '4#5': 35, '4#6': 37, '4#7': 39,
		'5#1': 41, '5#2': 43, '5#3': 45, '5#4': 47, '5#5': 49, '5#6': 51, '5#7': 53,
		'6#1': 55, '6#2': 57, '6#3': 59, '6#4': 61, '6#5': 63, '6#6': 65, '6#7': 67,
		'7#1': 69, '7#2': 71, '7#3': 73, '7#4': 75, '7#5': 77, '7#6': 79, '7#7': 81}

Quality = {'D': 1, 'C': 2, 'B': 3, 'A': 4, 'S': 5, 'SS': 6, 'SSS': 7}

import json
import random
file = 'data/item.json'

def get_qac(rank, qual):
	key = f'{rank}#{Quality[qual]}'
	return QAC[key]

def obtain_implicit_attrs(count, level):
	result = []
	selects = list(IMPLICIT.keys())
	for n in range(count):
		select = random.choice(selects)
		l, h = IMPLICIT[select][0], IMPLICIT[select][1]
		value = random.randint(l, h) / 100
		if select.find('RATE') < 0:
			#text = str(int(value * level))
			v = int(value * level)
		else:
			#text = f'{value}%'
			v = value
		#print(select, text)
		#e = {select: text}
		e = {select: v}
		result.append(e)
	return result

class ItemManager():
	def __init__(self, db):
		self.kind = 'weapon'
		self.kinds = []
		self.db_file = db
		self.limit = 5
		# read database
		with open(self.db_file) as f:
			self.eq_list = json.load(f)
		#print(self.eq_list['ring'])

	def set_kind(self, kind):
		self.kind = kind

	def set_kinds(self, kinds):
		self.kinds = kinds

	def get_attrs(self, rank, lv, attr):
		attrs = {}
		for key in attr.keys():
			attrs[key] = attr[key]
			qac = get_qac(rank, attrs[key]['class'])
			base = attrs[key]['value'][0]
			addition = attrs[key]['value'][1]
			if key not in ['damage', 'crit']:
				#value = str(int(base * qac + addition * lv))
				value = (base * qac) + (addition * lv)
				attrs[key]['value'] = int(value)
			else:
				min, max = 0, 0 # set default
				if key == 'damage':
					min, max = DAMAGE['D'][0], DAMAGE['D'][1]
				elif key == 'crit':
					min, max = CRIT['D'][0], CRIT['D'][1]
				v = random.choice(list(range(min, max)))
				#attrs[key]['value'] = f'{v + (base * addition)}%'
				attrs[key]['value'] = v + (base * addition)
		return attrs

	def get_init_eq(self, kind):
		item = self.eq_list[kind][0].copy()

		# set rank to 1
		item['rank'] = 1
		item['lv'] = 1
		# skip zero attrs
		attr = item['attr']
		attrs = {}
		for key in attr.keys():
			if attr[key]['value'][0] != 0:
				attrs[key] = attr[key]
				# set to "D"
				attrs[key]['class'] = 'D'

		item['attr'] = self.get_attrs(item['rank'], item['lv'], attrs)
		#item['attr'] = attrs

		# set implicit
		selected = obtain_implicit_attrs(count=1, level=1)
		#print(selected)

		item['implicit'] = selected
		return item

	def random_eq(self, kinds, level):
		amount = 4
		eqs = []
		for k in kinds:
			eqs = eqs + self.eq_list[k][1:]

		random.shuffle(eqs)

		result = []
		for i in range(amount):
			eq = random.choice(eqs)
			item = eq.copy()
			#print(item)
			# 选择级别
			rank = random.choice(item['rank'])
			item['rank'] = rank
			#print(rank)

			# 选择属性品质 （SSS, SS, S, A, B, C, D）
			attr = item['attr']
			attrs = {}
			for key in attr.keys():
				if attr[key]['value'][0] != 0:
					attrs[key] = attr[key]
					attr_class = random.choice(attr[key]['class'])
					#print(attr_class)
					attrs[key]['class'] = attr_class

			# set level
			levels = list(range(level, level+self.limit))
			select = random.choice(levels)
			item['lv'] = select

			#print(attrs)
			item['attr'] = self.get_attrs(item['rank'], item['lv'], attrs)

			implicit = obtain_implicit_attrs(item['rank'], item['lv'])
			item['implicit'] = implicit

			result.append(item)

		return result


if __name__ == '__main__':
	im = ItemManager(db=file)
	print(im.get_init_eq('weapon'))
	print(im.get_init_eq('armor'))
	print(im.get_init_eq('necklace'))
	print(im.get_init_eq('ring'))

	res = im.random_eq(['weapon', 'armor'], 120)
	#print(res)

