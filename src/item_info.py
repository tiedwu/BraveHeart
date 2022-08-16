from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import NumericProperty, ListProperty, ObjectProperty
from kivy.uix.label import Label

import translate

Builder.load_string('''

<IILabel@Label>:
	font_name: 'fonts/DroidSansFallback.ttf'
	font_size: '13sp'

<IIButton@ToggleButton>:
	#size_hint: None, None
	group: 'iib_select'

<ItemInfo>:
	size_hint: None, None
	size: root.size
	pos: root.pos
	btnbox_width: root.btnbox_width
	btnbox_height: root.btnbox_height
	btnbox_startx: root.btnbox_startx
	btnbox_starty: root.btnbox_starty
	#box_size: [255, 815]
	#info_size: [690, 1250]
	info_width: root.info_width
	info_height: root.info_height
	info_startx: root.info_startx
	info_starty: root.info_starty
	count: root.count

	image_size: root.image_width, root.image_height
	image_source: 'icons/item/weapon/022.jpg'
	image_pos: (root.image_startx, root.image_starty)

	rim_width: root.rim_width
	#separate_line_width: 4
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
		#orientation: 'vertical'
		size_hint: None, None
		size: (root.info_width, root.info_height)
		#pos: 70, 100
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
				#rgba: 1, 1, 1, 1
				rgba: 255/255, 215/255, 0, 1
			Line:
				#width: 4
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
			#pos_hint: {'x': 0.1, 'y': 0.5}
			#pos: 500, 600
		IILabel:
			id: lbl_name
			text: root.item_name
			size_hint: None, None
			text_size: self.size
			valign: 'middle'
			halign: 'left'
			width: 450
			#pos: self.parent.parent.itemname_pos


		# part #2: show rank
		IILabel:
		#Button
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
		#Button
			id: lbl_level
			text: f'lv{root.item_level}'
			text_size: self.size
			valign: 'middle'
			halign: 'right'
			size_hint: None, None
			height: 50
			width: 400

		# desc
		#Button:
		IILabel:
		#Button:
			font_name: 'fonts/DroidSansFallback.ttf'
			font_size: '13sp'
			id: lbl_desc
			text: f'{root.item_desc}'
			#text: ' ' * 10 + f'        aaa' + 'xxxxxxxxxxxxxx' * 5
			#text: " " * 15 +'aaaaaxxxxxx' * 3
			text_size: self.width, None
			valign: 'middle'
			halign: 'left'
			size_hint: 1, None
			height: self.texture_size[1]
			do_wrap: True
			#height: 200
			#width: 450
			multiline: True

	BoxLayout:
		orientation: 'vertical'
		size_hint: None, None
		#width: root.btnbox_width
		#height: root.btnbox_height
		size: (root.btnbox_width, root.btnbox_height)
		#pos: 800, 100
		pos: [root.btnbox_startx, root.btnbox_starty]
		IIButton:
			text: '对比'

		IIButton:
			text: '装备'

		IIButton:
			text: '强化'

		IIButton:
			text: '重铸'

		IIButton:
			text: '锁定'

		IIButton:
			text: '出售'

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

class ItemInfo(Widget):

	box_size = ListProperty()
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
	#item_desc = StringProperty()

	def __init__(self, item, info_size, box_size, info_pos, btnbox_xoffset, \
					btnbox_yoffset, **kwargs):
		super().__init__(**kwargs)

		self.size = kwargs['size']
		self.pos = kwargs['pos']

		self.info_width, self.info_height = info_size[0], info_size[1]
		self.btnbox_width, self.btnbox_height = box_size[0], box_size[1]
		self.info_startx, self.info_starty = info_pos[0], info_pos[1]

		self.btnbox_startx = self.info_startx + self.info_width + \
								btnbox_xoffset
		info_endy = self.info_starty + self.info_height
		btnbox_endy = info_endy - btnbox_yoffset
		self.btnbox_starty = btnbox_endy - self.btnbox_height

		self.set_item(item)

		self.image_width, self.image_height = 142, 142
		image_xoffset, image_yoffset = 52, 60
		self.image_startx = self.info_startx + image_xoffset
		self.image_starty = info_endy - image_yoffset - self.image_height

		name_xoffset = 10
		name_startx = self.image_startx + self.image_width + name_xoffset
		name_starty = self.image_starty + self.image_height / 4
		self.ids.lbl_name.pos = (name_startx, name_starty)
		self.count = 6

		rim_offset = 30
		self.separate_line_startx = self.info_startx + rim_offset
		#self.separate_line_width = 4
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
		#desc_startx = imp_startx + desc_xoffset # 1st line
		desc_startx = attr_startx
		desc_endx = kind_endx
		desc_width = desc_endx - desc_startx
		self.ids.lbl_desc.width = desc_width

		#self.item_desc = ' ' * 2 + self.item_desc
		self.item_desc = '☆' * 2 + self.item_desc
		lines, text = self.wrap_line(self.item_desc)
		self.item_desc = text
		print(f'lines: {lines}')

		desc_height = implicit_yoffset * lines
		#desc_height = self.ids.lbl_desc.height
		self.ids.lbl_desc.height = desc_height
		#print(f'DESC HEIGHT: {self.ids.lbl_desc.height}')
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
		#self.deal_info_desc()

	#def deal_info_rank(self):
		#pass
		#rank_startx = 100
		#rank_starty = 350

	#def deal_info_attr(self):
		#self.separate_line_2nd_y = 900

	#def deal_info_implicit(self):
		#self.separate_line_3rd_y = 500

	#def deal_info_desc(self):
		# rechange the size
		#pass

	def set_item(self, item):
		print(item)

		print(self.ids.lbl_name)
		kind = item[0]["kind"]

		# item image
		idx = item[0]["ID"]
		self.image_source = f'icons/item/{kind}/{idx}.jpg'

		# item name
		self.item_name = item[0]["name"]

		# item rank
		self.item_rank = translate.item_rank[item[0]["rank"]-1]

		# item kind
		self.item_kind = translate.item_kind[item[0]["kind"]]

		# item_level
		self.item_level = item[0]["lv"]

		# item attrs
		self.item_attrs = item[0]["attr"]

		# item implicit
		self.item_implicit = item[0]["implicit"]

		# item_desc
		self.item_desc = item[0]["desc"]

class Root(Screen):

	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		#self.ii = ItemInfo(size=(1200, 1300), pos=(10, 10))

		info_startx = 70
		info_width = 690
		btnbox_xoffset = 27
		btnbox_startx = info_startx + info_width + btnbox_xoffset
		info_starty = 70
		info_height = 1250
		info_endy = info_starty + info_height
		btnbox_yoffset = 240
		btnbox_endy = info_endy - btnbox_yoffset
		btnbox_width = 255
		btnbox_height = 815
		btnbox_starty = btnbox_endy - btnbox_height

		item = self.get_item()

		self.ii = ItemInfo(item=item, size=(1200, 1300), pos=(50, 50), \
						info_size=(info_width, info_height), \
						box_size=(btnbox_width, btnbox_height), \
						info_pos=(info_startx, info_starty), \
						btnbox_xoffset=btnbox_xoffset, \
						btnbox_yoffset=btnbox_yoffset)

		self.add_widget(self.ii)

	def get_item(self):

		# read from prifile
		import json
		profile = 'data/profile.json'
		with open(profile, 'r') as f:
			data = json.load(f)
		index = 3
		item = data['bag'][index]

		return item
		#self.ii.set_item(item)
		#self.add_widget(self.ii)

class MainApp(App):
	def build(self):
		root = Root()
		#root.display()
		return root

if __name__ == '__main__':

	from kivy.core.window import Window
	Window.clearcolor = 1, 1, 1, 1
	Window.size = [1500, 1400]
	MainApp().run()
