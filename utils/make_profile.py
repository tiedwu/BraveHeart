# -*- coding: utf-8 -*-
#file: make_profile.py

import json

# read from profile.json
data = dict()
with open('profile.json', 'r') as f:
	data = json.load(f)

data['samsara'] = 0
data['incarnation'] = 0

# write data
with open('profile.json', 'w', encoding='utf-8') as f:
	json.dump(data, f, indent=4, ensure_ascii=False)
