from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.properties import ObjectProperty, ListProperty
from kivy.utils import  platform

#Window.size = [800, 1000]
Window.size = [1440, 2911]

from item_info import ItemInfo
from item_comparison import CompInfo

import json
from functools import partial

Builder.load_string('''
#:set button_border_width 1
#:import utils kivy.utils
<BagItem>:
	#item_pos: 500, 500
	size_hint: None, None
	width: 145
	height: 145
	pos: self.pos
	item_image: ''
	backpack_index: 0
	
	#bg_colr: root.bg_color
	#lock_color: root.lock_color
	canvas.after:
		Color:
			rgba: 1, 1, 1, 1
		Line:
			width: 1
			rectangle: self.x, self.y, self.width, self.height
	ToggleButton:
		group: 'item_select'
		text: ''
		size: self.parent.size
		pos: self.parent.pos
		on_press: self.parent.parent.show_item_info(root.backpack_index)
		canvas.after:
			Color:
				#rgba: 1, 0, 0, 0.6
				rgba: self.parent.bg_color
			Triangle:
				points: self.parent.pos[0] + self.parent.size[0] * 0.3, self.parent.pos[1] + self.parent.size[1],\
					self.parent.pos[0] + self.parent.size[0], self.parent.pos[1] + self.parent.size[1],\
					self.parent.pos[0] + self.parent.size[0], self.parent.pos[1] + self.parent.size[1] * 0.3
					
			# rectangle:
			Color:
				#rgba: 1, 1, 1, 0.6
				rgba: self.parent.lock_color
			Line:
				width: 2
				rounded_rectangle: (self.parent.pos[0] + self.parent.size[0] * 0.7, \
					self.parent.pos[1] + self.parent.size[1] * 0.57, \
					self.parent.size[0] * 0.25, self.parent.size[1] * 0.2, 2)
			Line:
				width: 2
				ellipse: (self.parent.pos[0] + self.parent.size[0] * 0.8, \
					self.parent.pos[1] + self.parent.size[1] * 0.66, \
					self.parent.size[0] * 0.05, self.parent.size[1] * 0.05)
			Line:
				width: 2
				points: (self.parent.pos[0] + self.parent.size[0] * 0.825, \
					self.parent.pos[1] + self.parent.size[1] * 0.66, \
					self.parent.pos[0] + self.parent.size[0] * 0.825, \
					self.parent.pos[1] + self.parent.size[1] * 0.62)
			Line:
				width: 2
				ellipse: (self.parent.pos[0] + self.parent.size[0] * 0.75, \
					self.parent.pos[1] + self.parent.size[1] * 0.695, \
					self.size[0] * 0.15, self.size[1] * 0.15, 90, -90)
				
		Image:
			size_hint: None, None
			size: self.parent.size
			#source: 'icons/item/weapon/003.png'
			source: root.item_image
			allow_stretch: True
			center_x: self.parent.center_x
			center_y: self.parent.center_y

<BagLabel@Label, BagButton@Button>:
	font_name: 'fonts/DroidSansFallback.ttf'
	font_size: '12sp'

<BagToggleButton@ToggleButton>:
	group: 'bag_tgbtn_select'
	font_name: 'fonts/DroidSansFallback.ttf'
	font_size: '12sp'
	size_hint: None, None
	background_color: (0, 0, 0, 0)
	background_normal: ''
	linew: 1
	canvas.before:
		Color:
			#rgba: (48/255, 84/255, 150/255, 1)
			#rgba: (214/255, 205/255, 150/255, 1)
			#rgba: (158/255, 151/255, 111/255, 1)
			rgba: (138/255, 132/255, 99/255, 1)
		RoundedRectangle:
			size: self.size
			pos: self.pos
			radius: [18]

		# rim
		Color:
			#rgba: 0, 0, 1, 1
			rgba: 1, 1, 1, 1
		Line:
			width: button_border_width
			#rectangle: (root.rim_startx, root.rim_starty, \
			#	root.rim_width, root.rim_height)
			rounded_rectangle: (self.pos[0], self.pos[1], \
				self.size[0], self.size[1], 18)


<Bag>:
	ticket_label: ticket_label
	stone_amount: 3961
	ticket_amount: 3961
	item_amount: 30
	pack_limit: 40
	size_hint: None, None
	#size: root.ww * 0.9, root.wh * 0.5
	width: root.mw
	height: root.mh
	pos: [root.bag_startx, root.bag_starty]
	canvas.before:
		Color:
			rgba: 61/255, 60/255, 57/255, 1
			#rgba: 1, 0, 0, 1
		Rectangle:
			pos: self.pos
			size: self.size

		# border
		Color:
			rgba: 0, 0, 0, 0.5
		Line:
			width: root.frame_border
			#rectangle: (root.ww * 0.05, root.wh * 0.2, root.mw, root.mh)
			rectangle: (root.bag_startx, root.bag_starty, root.mw, root.mh)

		Color:
			#rgba: 1, 0, 0, 1
			rgba: utils.get_color_from_hex('#302606')
		Rectangle:
			pos: root.rect_startx, root.rect_starty
			size: root.grid_width, root.grid_height

		# rim
		Color:
			#rgba: 0, 0, 1, 1
			rgba: 255/255, 215/255, 0/255, 1
		Line:
			width: root.linew
			#rectangle: (root.rim_startx, root.rim_starty, \
			#	root.rim_width, root.rim_height)
			rounded_rectangle: (root.rim_startx, root.rim_starty, \
				root.rim_width, root.rim_height, 18)


		Color:
			rgba: 1, 1, 1, 1
		Line: # grid: 80x80, 8x5 grids
			width: root.linew
			rectangle: (root.rect_startx, root.rect_starty, root.grid_width, \
				root.grid_height)
		Line:
			width: root.linew
			points: root.grid_col_x[0], root.grid_col_y[0], \
					root.grid_col_x[0], root.grid_col_y[1]
		Line:
			width: root.linew
			points: root.grid_col_x[1], root.grid_col_y[0], \
					root.grid_col_x[1], root.grid_col_y[1]
		Line:
			width: root.linew
			points: root.grid_col_x[2], root.grid_col_y[0], \
					root.grid_col_x[2], root.grid_col_y[1]
		Line:
			width: root.linew
			points: root.grid_col_x[3], root.grid_col_y[0], \
					root.grid_col_x[3], root.grid_col_y[1]
		Line:
			width: root.linew
			points: root.grid_col_x[4], root.grid_col_y[0], \
					root.grid_col_x[4], root.grid_col_y[1]
		Line:
			width: root.linew
			points: root.grid_col_x[5], root.grid_col_y[0], \
					root.grid_col_x[5], root.grid_col_y[1]
		Line:
			width: root.linew
			points: root.grid_col_x[6], root.grid_col_y[0], \
					root.grid_col_x[6], root.grid_col_y[1]
		Line:
			width: root.linew
			points: root.grid_row_x[0], root.grid_row_y[0], \
					root.grid_row_x[1], root.grid_row_y[0]
		Line:
			width: root.linew
			points: root.grid_row_x[0], root.grid_row_y[1], \
					root.grid_row_x[1], root.grid_row_y[1]
		Line:
			width: root.linew
			points: root.grid_row_x[0], root.grid_row_y[2], \
					root.grid_row_x[1], root.grid_row_y[2]
		Line:
			width: root.linew
			points: root.grid_row_x[0], root.grid_row_y[3], \
					root.grid_row_x[1], root.grid_row_y[3]

	BagLabel:
		text: '背包'
		center_x: root.ww / 2
		center_y: root.rim_starty + (root.rim_height / 2)
		size_hint: None, None

	Button:
		size_hint: None, None
		size: root.exit_size, root.exit_size
		pos: root.exit_x, root.exit_y
		on_press: root.hide_me()
		Image:
			source: 'icons/exit.jpg'
			center_x: self.parent.center_x
			center_y: self.parent.center_y

	# ticket image
	Image:
		size_hint: None, None
		source: 'icons/misc/ticket.jpg'
		pos: root.ticket_image_x, root.ticket_image_y

	# ticket label
	BagLabel:
	#BagButton:
		id: ticket_label
		size_hint: None, None
		size: root.ticket_label_w, root.ticket_label_h
		#size: self.texture_size
		pos: root.ticket_label_x, root.ticket_label_y
		text: f'星舰入场券: {root.ticket_amount}张'
		#background_normal: ''
		#background_color: 0.1, 0.5, 0.6, 1
		#valign: 'middle'
		#halign: 'right'

	# stone image
	Image:
		size_hint: None, None
		source: 'icons/misc/stone.jpg'
		pos: root.stone_image_x, root.stone_image_y


	# stone label
	BagLabel:
	#BagButton:
		#id: stone_label
		size_hint: None, None
		size: root.stone_label_w, root.stone_label_h
		pos: root.stone_label_x, root.stone_label_y
		text: f'星舰石: {root.stone_amount}'
		#background_normal: ''
		#background_color: 0.1, 0.5, 0.6, 1

	# count label
	Label:
	#Button:
		size_hint: None, None
		size: root.count_label_w, root.count_label_h
		pos: root.count_label_x, root.count_label_y
		text: f'{root.item_amount}/{root.pack_limit}'
		background_normal: ''
		background_color: 0.1, 0.5, 0.6, 1

	# sale setting label
	BagLabel:
		size_hint: None, None
		size: root.setting_label_w, root.setting_label_h
		pos: root.setting_label_x, root.setting_label_y
		text: f'自动出售设置'
		background_normal: ''
		background_color: 0.1, 0.5, 0.6, 1


	# setting image
	Image:
		size_hint: None, None
		source: 'icons/misc/setting.jpg'
		pos: root.setting_image_x, root.setting_image_y

	# transfer button
	BagToggleButton:
		text: '转化'
		pos: root.transfer_btn_x, root.transfer_btn_y
		size: root.btn_w, root.btn_h

	# sort button
	BagToggleButton:
		text: '整理'
		pos: root.sort_btn_x, root.sort_btn_y
		size: root.btn_w, root.btn_h

	# sale button
	BagToggleButton:
		text: '出售'
		pos: root.sale_btn_x, root.sale_btn_y
		size: root.btn_w, root.btn_h

<BagWidget>:
	size_hint: None, None
	width: root.mw
	height: root.mh
	pos: root.ww * 0.05, root.wh * 0.1
	Bag:
		id: bag

	BoxLayout:
		size_hint_y: None
		height: 50
		size_hint_x: None
		width: root.ww * 0.9
		pos: root.ww * 0.05, root.wh * 0.65 
		Label:
			text: 'col#1'
		Label:
			text: 'col#2'
	# lines

<Root>:
	BagWidget:
		id:bag_widget
''')

class BagItem(Widget):

	bg_color = ListProperty()
	lock_color = ListProperty()
	def __init__(self, lock, item_image, backpack_index, **kwargs):
		super().__init__(**kwargs)
		#print(**kwargs)
		self.item_image = item_image
		self.backpack_index = backpack_index

		self.bg_color = (0, 0, 0, 0)
		self.lock_color = (0, 0, 0, 0)
		self.lock = lock
		#print(f'[bag.py] __init__() lock={lock}')
		#lock = True
		if self.lock:
			self.bg_color = (1, 0, 0, 0.6)
			self.lock_color = (1, 1, 1, 0.6)

class Bag(Widget):

	ticket_label = ObjectProperty()

	#ww, wh = app().window_size[0], app().window_size[1]
	ww, wh = Window.size[0], Window.size[1]
	mw, mh = Window.size[0] * 0.9, Window.size[1] * 0.4

	# bag
	bag_startx = ww * 0.05
	bag_starty = wh * 0.3

	# grids
	grid_size = 145
	linew = 1
	grid_width = grid_size * 8 + linew * 9
	grid_height = grid_size * 5 + linew * 6
	y_offset = 125
	rect_startx = (mw - grid_width) / 2 + ww * 0.05
	#rect_starty = (wh * 0.4 - grid_height) / 2 + wh * 0.15 + y_offset
	rect_starty = bag_starty + wh * 0.05 + y_offset
	grid_col_x = [rect_startx + (grid_size + linew) * 1, \
					rect_startx + (grid_size + linew) * 2, \
					rect_startx + (grid_size + linew) * 3, \
					rect_startx + (grid_size + linew) * 4, \
					rect_startx + (grid_size + linew) * 5, \
					rect_startx + (grid_size + linew) * 6, \
					rect_startx + (grid_size + linew) * 7]
	grid_col_y = [rect_starty, rect_starty + grid_height]
	grid_row_x = [rect_startx, rect_startx + grid_width]
	grid_row_y = [rect_starty + (grid_size + linew) * 1, \
					rect_starty + (grid_size + linew) * 2, \
					rect_starty + (grid_size + linew) * 3, \
					rect_starty + (grid_size + linew) * 4]

	# frame border
	frame_border = 10

	# rim
	rim_yoffset = 30
	#rim_width = grid_size * 8 + linew * 9
	rim_width = mw - 2 * frame_border
	rim_height = 100
	#rim_startx = (mw - grid_width) / 2 + ww * 0.05
	rim_startx = bag_startx + frame_border
	rim_starty = rect_starty + grid_height + rim_yoffset 

	# exit button
	exit_size = 74
	exit_xoffset = 30
	exit_x = rim_startx + rim_width - exit_size - exit_xoffset 
	exit_y = rim_starty + (rim_height - exit_size) / 2

	# ticket image
	ticket_image_w = 94
	ticket_image_h = 74
	ticket_image_yoffset = 50
	ticket_image_x = ww * 0.3
	ticket_image_y = rect_starty - ticket_image_yoffset - ticket_image_h

	# ticket lable
	ticket_label_w = 360
	ticket_label_h = 50
	ticket_label_padx = 10
	ticket_label_xoffset = 10
	ticket_label_yoffset = 10
	ticket_label_x = ticket_image_x + ticket_image_w + ticket_label_padx + \
		ticket_label_xoffset
	ticket_label_y = ticket_image_y + (ticket_image_h - ticket_label_h) / 2 + \
		ticket_label_yoffset

	# stone image
	stone_image_w = 75
	stone_image_h = 75
	stone_image_yoffset = 50
	stone_image_padx = 10
	stone_image_x = ticket_label_x + ticket_label_w + stone_image_padx
	stone_image_y = rect_starty - stone_image_yoffset - stone_image_h

	# stone lable
	stone_label_w = 260
	stone_label_h = 50
	stone_label_padx = 10
	stone_label_xoffset = 10
	stone_label_yoffset = 10
	stone_label_x = stone_image_x + stone_image_w + stone_label_padx + \
		stone_label_xoffset
	stone_label_y = stone_image_y + (stone_image_h - stone_label_h) / 2 + \
		stone_label_yoffset

	# item count label
	count_label_w = 150
	count_label_h = 50
	count_label_yoffset = 50
	count_label_x = rect_startx
	count_label_y = bag_starty + count_label_yoffset + frame_border

	# auto sale setting label
	setting_label_w = 260
	setting_label_h = 50
	setting_label_yoffset = 50
	setting_label_padx = 50
	setting_label_x = count_label_x + count_label_w + setting_label_padx
	setting_label_y = bag_starty + count_label_yoffset + frame_border

	# setting image
	setting_image_w = 62
	setting_image_h = 60
	setting_image_yoffset = 30
	setting_image_padx = 20
	setting_image_x = setting_label_x + setting_label_w - setting_image_padx
	setting_image_y = bag_starty + setting_image_yoffset + frame_border

	btn_padx = 40
	btn_space = 30
	btnbox_startx = setting_image_x + setting_image_w + btn_padx
	btnbox_endx = rect_startx + grid_width
	btnbox_w = btnbox_endx - btnbox_startx
	btn_w = (btnbox_w - 2 * btn_space) / 3
	btn_h = 100
	btn_yoffset = 30
	# transfer button
	transfer_btn_x = btnbox_startx
	transfer_btn_y = bag_starty + frame_border + btn_yoffset

	# sort button
	sort_btn_x = transfer_btn_x + btn_w + btn_space
	sort_btn_y = bag_starty + frame_border + btn_yoffset

	# sale button
	sale_btn_x = sort_btn_x + btn_w + btn_space
	sale_btn_y = bag_starty + frame_border + btn_yoffset

	bag_storage = []
	def __init__(self, **kwargs):
		super(Bag, self).__init__(**kwargs)

		# define bag_storage
		n, m = 8, 5
		for i in range(m):
			for j in range(n):
				#print(i, j)
				self.bag_storage.append(\
					[self.rect_startx + j * (self.grid_size + self.linew), \
					self.rect_starty + ((m-1)-i) * (self.grid_size + self.linew)])

		# for test storage position correct or not
		#for each in self.bag_storage:
		#	print(each)
		#	self.add_item(pos=each, item='item')

		#self.next_position = 0
		# occupied: [{'position_id': 0, 'item': item}]
		self.occupied = []
		self.info_widget = Widget()
		self.add_widget(self.info_widget)

		self.compare_widget = Widget()
		self.add_widget(self.compare_widget)

		self.grid_items = []

	def get_items(self, index):
		file = 'data/profile.json'
		if platform == 'android':
			file = f'/storage/emulated/0/BraveHeart/{file}'
		with open(file, "r") as f:
			data = json.load(f)
		item = data['bag'][index]
		equipped = data['equipped']
		print("[bag.py(get_item)]Got Item: ", item)
		return equipped, item

	def exit_compare(self, instance):
		print(f'[bag.py]exit_compare()')
		self.compare_widget.clear_widgets()
		self.remove_widget(self.compare_widget)

	def compare(self, instance):
		print(f'[bag.py]compare: {self.index}')

		item_backpack = self.item
		kind = self.item['kind']

		item_equipped = self.equipped[kind]

		info_width = 690
		info_endy = 1905
		xpad = 5
		ci = CompInfo(kind, item_equipped, item_backpack, info_width, info_endy, xpad)
		ci.ids.btn_exit.bind(on_release=self.exit_compare)

		self.info_widget.clear_widgets()
		self.compare_widget.clear_widgets()
		self.remove_widget(self.compare_widget)
		self.compare_widget.add_widget(ci)
		self.add_widget(self.compare_widget)

	def wear(self, instance):
		print(f'[bag.py]wear: {self.index} ({self.parent})')
		# close item_info
		self.info_widget.clear_widgets()
		self.remove_widget(self.info_widget)
		self.parent.item_wear(self.index)

		# backpack index replace to old item equipped
		# wear self.item[0]
		# self.update_backpack()

	def enforce_item(self, instance):
		print(f'[bag.py]enforce_item: {self.index} ({self.parent})')

		# close item_info
		self.info_widget.clear_widgets()
		self.remove_widget(self.info_widget)
		self.parent.enforce_item(self.index)

	def show_item_info(self, index):
		print(f'[bag.py]show_item_info: {index}')

		self.index = index

		#info_startx = 70
		screen_width = 1440
		info_width = 690
		info_startx = (screen_width - info_width) / 2
		#info_width = 690
		btnbox_xoffset = 27
		btnbox_startx = info_startx + info_width + btnbox_xoffset

		info_endy = self.rim_starty
		#print(self.rim_starty)
		info_height = 1250
		info_starty = info_endy - info_height
		#info_endy = info_starty + info_height
		btnbox_yoffset = 240
		btnbox_endy = info_endy - btnbox_yoffset
		btnbox_width = 255
		btnbox_height = 815
		btnbox_starty = btnbox_endy - btnbox_height

		self.equipped, item = self.get_items(index)

		self.item = item[0]
		self.kind = self.item['kind']
		self.image_id = self.item["ID"]

		ii = ItemInfo(item=item, size=(1200, 1300), pos=(50, 50), \
						   info_size=(info_width, info_height), \
						   box_size=(btnbox_width, btnbox_height), \
						   info_pos=(info_startx, info_starty), \
						   btnbox_xoffset=btnbox_xoffset, \
						   btnbox_yoffset=btnbox_yoffset)

		print(f'[bag.py]show_item_info: ii.ids {ii.ids}')
		ii.ids.btn_compare.bind(on_release=self.compare)
		ii.ids.btn_wear.bind(on_release=self.wear)
		ii.ids.btn_lock.bind(on_release=self.check_lock)
		ii.ids.btn_item_enforce.bind(on_release=self.enforce_item)
		ii.ids.btn_item_rebuild.bind(on_release=self.enforce_item)
		ii.ids.btn_item_sell.bind(on_release=partial(self.sell_item, index=self.index))

		self.info_widget.clear_widgets()
		self.remove_widget(self.info_widget)
		self.info_widget.add_widget(ii)
		self.add_widget(self.info_widget)

	def sell_item(self, *args, **kwargs):
		index = kwargs["index"]
		print(f'[bag.py] Bag.sell_item(index={index})')
		self.parent.item_sell(index)

	def check_lock(self, instance):
		print(f'[bag.py] check_lock()')
		# close item_info
		self.info_widget.clear_widgets()
		self.remove_widget(self.info_widget)
		self.parent.item_check_lock(self.index)

	def hide_me(self):
		#self.opacity = 0
		self.info_widget.clear_widgets()
		self.parent.close_bag()

	def init_bag(self, bag_data):
		# init bag by read bag json
		#print("init_bag()")

		self.occupied = []
		self.grid_items = []
		for item in bag_data:
			self.add_item(item)
			self.occupied.append(item)
			
	def backpack_add_item(self, index):
		file = 'data/profile.json'
		if platform == 'android':
			file = f'/storage/emulated/0/BraveHeart/{file}'
		with open(file, "r") as f:
			data = json.load(f)
		item = data['bag'][index]
		self.occupied.append(item)
		self.add_item_by_index(item, index)

	def add_item_by_index(self, item, index):
		item_image = f'icons/item/{item[0]["kind"]}/{item[0]["ID"]}.jpg'
		lock = item[0]["lock"]
		bi = BagItem(lock=lock, pos=self.bag_storage[index], \
					 item_image=item_image, backpack_index=index)
		self.grid_items.append(bi)
		self.add_widget(bi)

	def add_item(self, item, insert=False):
		#print("add_item() ", item)

		pos_index = len(self.occupied)

		if insert:
			pos_index -= 1

		item_image = f'icons/item/{item[0]["kind"]}/{item[0]["ID"]}.jpg'
		#print(f'[bag.py] add_item() item_image={item_image}')
		#self.occupied.append(item)

		lock = item[0]["lock"]
		bi = BagItem(lock=lock, pos=self.bag_storage[pos_index], \
						item_image=item_image, backpack_index=pos_index)
		self.grid_items.append(bi)
		#self.add_widget(BagItem(pos=self.bag_storage[pos_index], \
		#				item_image=item_image, backpack_index=pos_index))

		self.add_widget(bi)
		# send to server to update json in main.py

	def get_update_item(self):
		file = 'data/profile.json'
		if platform == 'android':
			file = f'/storage/emulated/0/BraveHeart/{file}'
		with open(file, "r") as f:
			data = json.load(f)
		item = data['bag'][self.index]
		return item

	def update_item(self):
		print(f'[bag.py]update_item: {self.index}')
		item = self.get_update_item()
		self.occupied[self.index] = item
		item_image = f'icons/item/{item[0]["kind"]}/{item[0]["ID"]}.jpg'
		self.grid_items[self.index].item_image = item_image

	def update_item_lock(self):
		print(f'[bag.py]update_item_lock: {self.index}')
		item = self.get_update_item()
		self.occupied[self.index] = item
		lock = item[0]["lock"]
		#self.grid_items[self.index].lock = lock
		if lock:
			self.grid_items[self.index].bg_color = (1, 0, 0, 0.6)
			self.grid_items[self.index].lock_color = (1, 1, 1, 0.6)
		else:
			self.grid_items[self.index].bg_color = (0, 0, 0, 0)
			self.grid_items[self.index].lock_color = (0, 0, 0, 0)

	# position means position-th instead of index
	def remove_item(self, position):
		print(f'[bag.py] Bag.remove_item(position={position})')
		#print(self.children)
		print(f'[bag.py] Bag.remove_item(len_occupied={len(self.occupied)})')
		self.occupied.pop(position-1)
		print(f'[bag.py] Bag.remove_item(len_occupied={len(self.occupied)})')
		#print(self.occupied)

		# clear all grids
		for item in self.grid_items:
			self.remove_widget(item)

		self.grid_items = []
		index = 0
		for item in self.occupied:
			# print(item)
			self.add_item_by_index(item, index)
			index += 1

		# close info widget
		self.info_widget.clear_widgets()
		self.remove_widget(self.info_widget)
	#def on_size(self, *args):
		#print("Bag(on_size): ", *args)
		#print(self.parent.height)

class BagWidget(Widget):
	ww, wh = Window.size[0], Window.size[1]
	mw, mh = Window.size[0] * 0.9, Window.size[1] * 0.5

class Root(Screen):

	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		print(self.ids)
	#def on_size(self, *args):
		#print("Root(on_size): ", *args)

class AwesomeApp(App):

	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.window_size = [800, 1000]

	def build_data_from_profile(self):

		import json
		profile = 'data/profile.json'
		with open(profile, "r") as f:
			data = json.load(f)
		bag_data = data['bag']

		return bag_data

	def build_data_from_item(self):
		import json
		import item_manage
		item_file = 'data/item.json'

		im = item_manage.ItemManager(db=item_file)
		item = im.random_eq(['weapon'], 120, 1, [5])
		bag_data = []
		bag_data.append(item)

		item2 = im.random_eq(['suit'], 120, 1, [5])
		bag_data.append(item2)

		return bag_data

	def build(self):
		root = Root()

		#bag_data = self.build_data_from_item()
		bag_data = self.build_data_from_profile()

		root.ids.bag_widget.ids.bag.init_bag(bag_data)
		#root.ids.bag_widget.ids.bag.add_item(item)

		#root.ids.bag_widget.ids.bag.remove_item(1)
		return root

if __name__ == '__main__':
	Window.size = [800, 1000]
	Window.clearcolor = 1, 1, 1, 1
	AwesomeApp().run() 
