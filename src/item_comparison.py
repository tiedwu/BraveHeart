# item equipped vs assigned
# same top y(1320) with item info

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.properties import NumericProperty, ListProperty, ObjectProperty, StringProperty

import translate

Builder.load_string('''

<IILabel@Label>:
	font_name: 'fonts/DroidSansFallback.ttf'
	font_size: '13sp'

<InfoWidget>:
	size_hint: None, None
	size: root.size
	pos: root.pos
	btnbox_width: root.btnbox_width
	btnbox_height: root.btnbox_height
	btnbox_startx: root.btnbox_startx
	btnbox_starty: root.btnbox_starty
	info_width: root.info_width
	info_height: root.info_height
	info_startx: root.info_startx
	info_starty: root.info_starty
	count: root.count

	image_size: root.image_width, root.image_height
	image_source: 'icons/item/weapon/022.jpg'
	image_pos: (root.image_startx, root.image_starty)

	rim_width: root.rim_width
	#rim_width: 6
	separate_line_startx: root.separate_line_startx
	separate_line_width: root.separate_line_width
	separate_line_endx: root.separate_line_endx
	separate_line_1st_y: root.separate_line_1st_y
	separate_line_2nd_y: root.separate_line_2nd_y
	separate_line_3rd_y: root.separate_line_3rd_y

	item_name: 'sword'
	item_rank: ''
	item_kind: ''
	item_desc: ''
	canvas.before:
		Color:
			rgba: 0, 0, 0, 0
		Rectangle:
			pos: self.pos
			size: self.size

	Widget:
		size_hint: None, None
		size: (root.info_width, root.info_height)
		pos: [root.info_startx, root.info_starty]
		linew: 1
		canvas.before:
			Color:
				rgba: 0, 0, 0, 0.8

			RoundedRectangle:
				pos: self.pos
				size: self.size
				radius: [18]

			#rim
			Color:
				rgba: 1, 0, 0, 1
			Line:
				width: root.rim_width
				rounded_rectangle: (self.pos[0], self.pos[1], \
					self.size[0], self.size[1], 18)

			# 1st separate line
			Color:
				rgba: 255/255, 215/255, 0, 1
			Line:
				width: root.separate_line_width
				points:root.separate_line_startx, root.separate_line_1st_y, \
				 	root.separate_line_endx, root.separate_line_1st_y

			# 2nd separate line
			Color:
				rgba: 255/255, 215/255, 0, 1
			Line:
				width: root.separate_line_width
				points:root.separate_line_startx, root.separate_line_2nd_y, \
				 	root.separate_line_endx, root.separate_line_2nd_y

			# 3rd separate line
			Color:
				rgba: 255/255, 215/255, 0, 1
			Line:
				width: root.separate_line_width
				points:root.separate_line_startx, root.separate_line_3rd_y, \
				 	root.separate_line_endx, root.separate_line_3rd_y

		# four parts
		# part #1: show icons & name
		Image:
			size_hint: None, None
			size: self.parent.parent.image_size
			#size: 142, 142
			source: self.parent.parent.image_source
			allow_stretch: True
			pos: self.parent.parent.image_pos

		IILabel:
			id: lbl_name
			text: root.item_name
			size_hint: None, None
			text_size: self.size
			valign: 'middle'
			halign: 'left'
			width: 450

		# part #2: show rank
		IILabel:
			id: lbl_rank
			text: root.item_rank
			size_hint: None, None
			height: 50
			width: 120

		# show kind
		IILabel:
			id: lbl_kind
			text: root.item_kind
			text_size: self.size
			valign: 'middle'
			halign: 'right'
			size_hint: None, None
			height: 50
			width: 150

		# show item level
		IILabel:
			id: lbl_level
			text: f'lv{root.item_level}'
			text_size: self.size
			valign: 'middle'
			halign: 'right'
			size_hint: None, None
			height: 50
			width: 400

		# desc
		IILabel:
			font_name: 'fonts/DroidSansFallback.ttf'
			font_size: '13sp'
			id: lbl_desc
			text: f'{root.item_desc}'
			text_size: self.width, None
			valign: 'middle'
			halign: 'left'
			size_hint: 1, None
			height: self.texture_size[1]
			do_wrap: True
			multiline: True
			
		

<CompInfo>:
	btn_startx: root.btn_startx
	btn_starty: root.btn_starty
	btn_width: root.btn_width
	btn_height: root.btn_height
	btn_rim_width: root.btn_rim_width
	Button:
		canvas.after:
			Color:
				rgba: 1, 1, 1, 1
			Line:
				width: root.btn_rim_width
				rounded_rectangle: (self.pos[0], self.pos[1], \
					self.size[0], self.size[1], 18)
					
		font_name: 'fonts/DroidSansFallback.ttf'
		id: btn_exit
		text: '关闭对比'
		size_hint: None, None
		#pos: 100, 100
		pos: root.btn_startx, root.btn_starty
		width: root.btn_width
		#width: 100
		height: root.btn_height
		#height: 300
		background_normal: ''
		background_color: 0, 0, 0, 0.5

<CompInfo2>:
	Button:
		text: 'Hello'

	
<Root>:

''')

class ATTRLabel(Label):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.font_name = 'fonts/DroidSansFallback.ttf'
		self.size_hint = None, None
		self.size = 500, 60
		self.text_size = self.size
		self.valign = 'middle'
		self.halign = 'left'

class InfoWidget(Widget):
	info_width = NumericProperty()
	info_height = NumericProperty()
	btnbox_width = NumericProperty()
	btnbox_height = NumericProperty()
	btnbox_startx = NumericProperty()
	btnbox_starty = NumericProperty()
	info_startx = NumericProperty()
	info_starty = NumericProperty()

	# opposite to info_startx
	image_startx = NumericProperty()
	image_starty = NumericProperty()
	image_width = NumericProperty()
	image_height = NumericProperty()

	rim_width = NumericProperty(6)

	separate_line_startx = NumericProperty()
	separate_line_width = NumericProperty(4)
	separate_line_endx = NumericProperty()
	separate_line_1st_y = NumericProperty()
	separate_line_2nd_y = NumericProperty()
	separate_line_3rd_y = NumericProperty()

	item_level = NumericProperty(0)
	item_attrs = ObjectProperty()

	# item_desc = StringProperty()
	def __init__(self, kind, item, info_width, info_endy, info_startx, **kwargs):
		super().__init__(**kwargs)

		#self.size = kwargs['size']
		#self.pos = kwargs['pos']

		self.kind = kind
		self.info_width = info_width
		self.info_startx = info_startx
		self.item = item
		#self.info_height = info_height
		self.info_endy = info_endy

		print(f'[item_info]__init__(): info_endy={info_endy}')

		self.set_item(item)

		self.image_width, self.image_height = 142, 142
		image_xoffset, image_yoffset = 52, 60

		self.image_startx = self.info_startx + image_xoffset
		self.image_starty = info_endy - image_yoffset - self.image_height

		name_xoffset = 10
		name_startx = self.image_startx + self.image_width + name_xoffset
		name_starty = self.image_starty + self.image_height / 4
		self.ids.lbl_name.pos = (name_startx, name_starty)

		rim_offset = 30
		self.separate_line_startx = self.info_startx + rim_offset
		self.separate_line_endx = self.info_startx + self.info_width - \
								  rim_offset
		separate_line_1st_yoffset = 28
		self.separate_line_1st_y = self.image_starty - separate_line_1st_yoffset

		rank_yoffset = 73

		rank_starty = self.separate_line_1st_y - rank_yoffset
		rank_width = self.ids.lbl_rank.width
		rank_startx = self.image_startx + (self.image_width - rank_width) / 2
		self.ids.lbl_rank.pos = (rank_startx, rank_starty)

		kind_starty = rank_starty
		rank_xoffset = 200
		kind_startx = self.separate_line_endx - rank_xoffset
		self.ids.lbl_kind.pos = (kind_startx, kind_starty)
		kind_width = self.ids.lbl_kind.width
		kind_endx = kind_startx + kind_width

		level_yoffset = 95
		level_starty = kind_starty - level_yoffset
		level_width = self.ids.lbl_level.width
		level_startx = kind_endx - level_width
		self.ids.lbl_level.pos = (level_startx, level_starty)

		# attrs
		attrs_yoffset = 65

		# oppsite to rank
		attrs_xoffset = 10
		attr_startx = rank_startx - attrs_xoffset
		self.item = item
		attr_starty = level_starty
		for key in self.item_attrs.keys():
			label_text = f' {self.item_attrs[key]["class"]} {translate.item_attr[key]}: {self.item_attrs[key]["value"]}'
			if key in ['crit', 'gold', 'damage']:
				label_text += f'%'
			attr_starty = attr_starty - attrs_yoffset
			attr = ATTRLabel(text=label_text, pos=(attr_startx, attr_starty))
			self.add_widget(attr)

		# separate line 2nd
		line_yoffset = 20
		self.separate_line_2nd_y = attr_starty - line_yoffset

		implicit_endy = self.separate_line_2nd_y - line_yoffset
		implicit_height = 60
		implicit_space = 5
		implicit_yoffset = implicit_height + implicit_space
		imp_starty = implicit_endy

		imp_xoffset = 20
		imp_startx = attr_startx + imp_xoffset

		# implicit
		for imp in self.item_implicit:
			k, v = list(imp.keys())[0], list(imp.values())[0]
			label_text = f'{translate.item_implicit[k]}: {v}'
			if k in ['HP_RATE', 'ARMOR_RATE', 'ATTACK_RATE', 'DAMAGE_RATE', 'CRIT_RATE']:
				label_text += f'%'
			imp_starty = imp_starty - implicit_yoffset
			implicit = ATTRLabel(text=label_text, pos=(imp_startx, imp_starty))
			self.add_widget(implicit)

		# 3rd separate line
		self.separate_line_3rd_y = imp_starty - line_yoffset

		# desc
		desc_xoffset = 5
		# desc_startx = imp_startx + desc_xoffset # 1st line
		desc_startx = attr_startx
		desc_endx = kind_endx
		desc_width = desc_endx - desc_startx
		self.ids.lbl_desc.width = desc_width

		# self.item_desc = ' ' * 2 + self.item_desc
		self.item_desc = '☆' * 2 + self.item_desc
		lines, text = self.wrap_line(self.item_desc)
		self.item_desc = text
		#print(f'lines: {lines}')

		desc_height = implicit_yoffset * lines
		# desc_height = self.ids.lbl_desc.height
		self.ids.lbl_desc.height = desc_height
		# print(f'DESC HEIGHT: {self.ids.lbl_desc.height}')
		line_space = 20
		desc_starty = self.separate_line_3rd_y - desc_height - line_space
		self.ids.lbl_desc.pos = (desc_startx, desc_starty)

		# rechange frame size
		frame_space = 50
		self.info_starty = desc_starty - frame_space
		self.info_height = info_endy - self.info_starty

	def wrap_line(self, desc):
		text = ''
		#desc = "abcdefghijk"
		desc_length = len(desc)
		limit = 12
		n = 0
		if desc_length > limit:
			while desc_length > limit:

				# 1st 0..5
				# 2nd 5..10
				# 3rd 10..15
				start = n * limit
				end = (n+1) * limit
				text += desc[start:end:1]+"\n"
				desc_length -= limit
				n += 1
			print("left:", desc_length)
			if desc_length > 0:
				num = 0 - desc_length
				text += desc[num:]
		else:
			text = desc
		return n+1, text

	def set_item(self, item):
		print(item)

		print(self.ids.lbl_name)
		#kind = self.kind

		# item image
		idx = item["ID"]
		self.image_source = f'icons/item/{self.kind}/{idx}.jpg'

		# item name
		self.item_name = item["name"]

		# item rank
		self.item_rank = translate.item_rank[item["rank"]-1]

		# item kind
		self.item_kind = translate.item_kind[self.kind]
		#self.item_kind = self.kind

		# item_level
		self.item_level = item["lv"]

		# item attrs
		self.item_attrs = item["attr"]

		# item implicit
		self.item_implicit = item["implicit"]

		# item_desc
		self.item_desc = item["desc"]

class CompInfo(Widget):
	btn_startx = NumericProperty()
	btn_starty = NumericProperty()
	btn_width = NumericProperty()
	btn_height = NumericProperty()

	btn_rim_width = NumericProperty(2)

	def __init__(self, kind, item_equipped, item_backpack, info_width, info_endy, xpad, **kwargs):
		super().__init__(**kwargs)
		self.equipped_startx = xpad
		self.kind = kind
		self.info_width = info_width
		self.info_endy = info_endy
		self.item_equipped = item_equipped

		#self.ids.equipped = InfoWidget(item=item_equipped, info_width=info_width, info_endy=info_endy, info_startx=equipped_startx)
		item_equipped_info = InfoWidget(kind=kind, item=item_equipped, info_width=info_width, info_endy=info_endy, info_startx=self.equipped_startx)
		self.add_widget(item_equipped_info)

		screen_width = 1440
		assigned_startx = screen_width - xpad - info_width
		item_backpack_info = InfoWidget(kind=kind, item=item_backpack, info_width=info_width, info_endy=info_endy, info_startx=assigned_startx)
		self.add_widget(item_backpack_info)

		self.btn_width, self.btn_height = 267, 104
		screen_height = 2911
		btn_endy = screen_height - 851
		self.btn_startx = 604
		self.btn_starty = btn_endy - self.btn_height


class CompInfo2(Widget):
	def __init__(self, arg1, arg2, **kwargs):
		super().__init__(**kwargs)
		print(arg1, arg2)

def get_items(idx):
	import json
	file = 'data/profile.json'
	with open(file, "r") as f:
		data = json.load(f)

	item = data['bag'][idx][0]
	kind = item['kind']
	equipped = data['equipped'][kind]

	return kind, equipped, item

class Root(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		info_width = 690
		info_endy = 1320
		xpad = 5

		idx = 3
		kind, item_equipped, item_backpack = get_items(idx)

		#print(item_equipped)
		#print(item_backpack)

		ci = CompInfo(kind, item_equipped, item_backpack, info_width, info_endy, xpad)
		#arg1 = 1
		#c = CompInfo2(item_equipped, item_backpack)
		self.add_widget(ci)
		#self.add_widget(c)

class MainApp(App):
	def build(self):
		return Root()

if __name__ == '__main__':
	MainApp().run()
