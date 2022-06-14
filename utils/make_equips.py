
weapon = {'ID': '001', 'name': '新手剑', 'desc': '一把普通的剑', 'rank': 1,
          'attr': {'attack': {'class': 'D', 'value': '50'}}, 'lv': 1, 'implicit': [{'HP': '8'}]}
suit = {'ID': '101', 'name': '新手铠甲', 'desc': '普通的衣甲', 'rank': 1,
         'attr': {'armor': {'class': 'D', 'value': '20'}}, 'lv': 1, 'implicit': [{'CRIT_RATE': '17.16%'}]}
necklace = {'ID': '201', 'name': '新手项链', 'desc': '一条普通的项链', 'rank': 1,
            'attr': {'damage': {'class': 'D', 'value': '72%'}}, 'lv': 1, 'implicit': [{'HP_RATE': '35.03%'}]}
ring = {'ID': '301', 'name': '新手指环', 'desc': '一个普通的指环', 'rank': 1,
        'attr': {'hp': {'class': 'D', 'value': '20'}}, 'lv': 1, 'implicit': [{'ATTACK': '4'}]}

profile = {'equipped': {'weapon': weapon, 'suit': suit, 'necklace': necklace, 'ring': ring}}

import json

with open('profile.json', "w", encoding='utf-8') as f:
	json.dump(profile, f, indent=4, ensure_ascii=False)
