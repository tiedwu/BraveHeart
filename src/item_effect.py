#KEYS: ['hp', 'ap', 'cc', 'cd', 'av', 'bv']


class ItemEffect():
	def __init__(self, items):
		self.items = items

	def calc_effect(self):
		effect = {'hp': 0, 'ap': 0, 'cc': 0, 'cd': 0, 'av': 0, 'bv': 0, 
			'gold': 0, 'hp_ratio': 0, 'ap_ratio': 0, 'av_ratio': 0}

		for k in self.items.keys():
			attrs = self.items[k]['attr']
			print("ATTRS: ", attrs)
			for attr in attrs.keys():
				if attr == 'hp':
					akey = 'hp'
				elif attr == 'attack':
					akey = 'ap'
				elif attr == 'armor':
					akey = 'av'
				elif attr == 'damage':
					akey = 'cd'
				elif attr == 'block':
					akey = 'bv'
				elif attr == 'crit':
					akey = 'cc'
				elif attr == 'gold':
					akey = 'gold'

				effect[akey] += attrs[attr]['value']

			implicits = self.items[k]['implicit']
			print("IMPLICITS: ", implicits)
			for implicit in implicits:
				for k in implicit.keys():
					if k == 'HP':
						ikey = 'hp'
					elif k == 'ATTACK':
						ikey = 'ap'
					elif k == 'ARMOR':
						ikey = 'av'
					elif k == 'DAMAGE_RATE':
						ikey = 'cd'
					elif k == 'BLOCK':
						ikey = 'bv'
					elif k == 'CRIT_RATE':
						ikey = 'cc'
					elif k == 'ATTACK_RATE':
						ikey = 'ap_ratio'
					elif k == 'ARMOR_RATE':
						ikey = 'av_ratio'
					elif k == 'HP_RATE':
						ikey = 'hp_ratio'

					effect[ikey] += implicit[k]

		return effect

if __name__ == '__main__':
	import json
	with open('data/profile.json', 'r') as f:
		data = json.load(f)
	items = data['equipped']
	print(items)
	ie = ItemEffect(items)
	print(ie.calc_effect())

	# check key exist
	d = {'a': 1}

	if 'b' in d.keys():
		print(d['b'])
	else:
		print('key not found')

