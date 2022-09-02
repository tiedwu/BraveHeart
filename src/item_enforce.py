from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import NumericProperty
from kivy.utils import platform
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.stacklayout import StackLayout
from kivy.graphics import *

import json
import translate
from functools import partial

Builder.load_string('''

<IELabel@Label>:
	font_name: 'fonts/DroidSansFallback.ttf'
	#font_size: '13sp'
	
<ComboBox@BoxLayout>:
	ltext: ''
	size: 198, 48
	#orientation: 'lr-tb'
	orientation: 'horizontal'
	canvas.before:
		Color:
			rgba: 0, 0, 1, 1
		Rectangle:
			size: self.size
			pos: self.pos
	ToggleButton:
		size_hint: None, None
		size: 48, 48
			#size_hint: 0.5, 1
		text: ''
		background_normal: 'icons/uncheck.jpg'
		background_down: 'icons/checked.jpg'
	IELabel:
		font_size: '10sp'
		width: 150
		height: 48
		text: root.ltext
		#size_hint: None, None
		text_size: self.size
		valign: 'middle'
		halign: 'left'

<RadioBox@BoxLayout>:
	ltext: ''
	size: 198, 48
	#orientation: 'lr-tb'
	orientation: 'horizontal'
	canvas.before:
		Color:
			rgba: 0, 0, 1, 1
		Rectangle:
			size: self.size
			pos: self.pos
	ToggleButton:
		size_hint: None, None
		size: 48, 48
			#size_hint: 0.5, 1
		text: ''
		background_normal: 'icons/radio_uncheck.jpg'
		background_down: 'icons/radio_checked.jpg'
	IELabel:
		font_size: '10sp'
		width: 150
		height: 48
		text: root.ltext
		#size_hint: None, None
		text_size: self.size
		valign: 'middle'
		halign: 'left'

<IEButton@Button>:
	canvas.after:
		Color:
			rgba: 1, 1, 1, 1
		Line:
			width: 2
			rounded_rectangle: (self.pos[0], self.pos[1], self.size[0], self.size[1], 18)
	font_name: 'fonts/DroidSansFallback.ttf'
	background_normal: ''
	background_color: 119/255, 102/255, 74/255, 1

<ItemEnforce>:
	widget_startx: root.widget_startx
	widget_starty: root.widget_starty
	widget_width: root.widget_width
	widget_height: root.widget_height
	image_source: ''
	item_name: ''
	image_harrow: 'icons/harrow.jpg'
	image_varrow: 'icons/varrow.jpg'
	upgrade_level: ''
	item_upgrade_cost: ''
	canvas.before:
		#Color:
		#	rgba: 43/255, 41/255, 46/255, 0.5
		#RoundedRectangle:
		#	pos: root.widget_startx, root.widget_starty
		#	#pos: 100, 100
			#size: 100, 100
		##	radius: [18]
		Color:
			rgba: 43/255, 41/255, 46/255, 1
		RoundedRectangle:
			pos: root.widget_bg_startx, root.widget_bg_starty
			size: root.widget_bg_width, root.widget_bg_height
		
		# title rim
		Color:
			rgba: 119/255, 102/255, 74/255, 1
		Line:
			width: 2
			rounded_rectangle: (root.title_startx, root.title_starty, root.title_width, root.title_height, 18)	
			
		# widget rim
		Color: 
			rgba: 43/255, 41/255, 46/255, 0.6
		Line:
			width: root.alpha
			rounded_rectangle: (root.widget_startx, root.widget_starty, root.widget_width, root.widget_height, 18)
			
		# check image center x
		#Color:
		#	rgba: 0, 0, 0, 0
		#Rectangle:
		#	pos: 580 - root.image_width / 2, root.title_starty
		#	size: 20, 20
			
		# check attr length
		#Color:
		#	rgba: 0, 0, 1, 1
		#Rectangle:
		#	pos: 212.5, 2112
		#	size: 300, 40
	IELabel:
		text: '装备强化'
		#size_hint: 0.5, 1
		center_x: root.widget_startx + root.widget_width / 2
		center_y: root.title_starty + root.title_height / 2
		color: 193/255, 170/255, 154/255, 1
	Button:
		id: btn_exit_item_enforce
		size_hint: None, None
		size: 74, 74
		center_x: root.widget_startx + root.widget_width * 0.95
		center_y: root.title_starty + root.title_height / 2
		#on_press: root.hide_me()
		Image:
			source: 'icons/exit.jpg'
			center_x: self.parent.center_x
			center_y: self.parent.center_y
	IELabel:
		text: '- 强化 -'
		center_x: root.widget_startx + root.widget_width / 2
		height: root.title_word_height
		center_y: root.title_word_centery
		color: 234/255, 186/255, 120/255, 1
	Image:
		size_hint: None, None
		#size: self.parent.parent.image_size
		size: root.image_width, root.image_height
		source: root.image_source
		allow_stretch: True
		center_x: root.image_centerx
		center_y: root.image_centery
	IELabel:
		canvas:
			Color:
				rgba: 0, 0, 0, 0
			Rectangle:
				size: 405, self.size[1]
				pos: root.item_name_x, root.image_centery - root.image_height / 2

	#Button:
		#background_normal: ''
		#background_color: 1, 0, 0, 1
		font_size: '12sp'
		id: lbl_item_name
		size_hint_x: None
		size: self.texture_size[0], self.size[1]
		text: root.item_name
		x: root.item_name_x
		#valign: 'middle'
		center_y: root.image_centery
		
	Image:
		size_hint: None, None
		#size: self.parent.parent.image_size
		size: root.image_arrow_width, root.image_arrow_height
		source: root.image_harrow
		allow_stretch: True
		center_y: root.harrow_center_y
		x: root.harrow_x
		
	IEButton:
		size_hint: None, None
		text: root.upgrade_level
		width: root.btn_upgrade_width
		height: root.btn_upgrade_height
		center_x: root.btn_upgrade_centerx
		center_y: root.btn_upgrade_centery
		
	IELabel:
		text: '- 词条重铸 -'
		center_x: root.widget_startx + root.widget_width / 2
		height: root.title_word_height
		center_y: root.implicit_rebuild_centery
		color: 234/255, 186/255, 120/255, 1
		
	IELabel:
		text: '自动重铸设置'
		width: root.rebuild_setting_width
		height: root.rebuild_setting_height
		font_size: '10sp'
		size_hint: None, None
		text_size: self.size
		valign: 'middle'
		halign: 'left'
		pos: root.rebuild_setting_startx, root.rebuild_setting_starty
		color: 153/255, 153/255, 153/255, 1
		
	ComboBox:
		ltext: '攻击'
		pos: root.ap_rebuild_startx, root.ap_rebuild_starty
		#pos: 300, 300
	ComboBox:
		ltext: '生命'
		pos: root.hp_rebuild_startx, root.ap_rebuild_starty
	ComboBox:
		ltext: '防御'
		pos: root.av_rebuild_startx, root.ap_rebuild_starty
	ComboBox:
		ltext: '格挡'
		pos: root.bv_rebuild_startx, root.ap_rebuild_starty
	ComboBox:
		ltext: '暴击率'
		pos: root.cc_rebuild_startx, root.ap_rebuild_starty
	ComboBox:
		ltext: '攻击%'
		pos: root.ap_rebuild_startx, root.apr_rebuild_starty
	ComboBox:
		ltext: '生命%'
		pos: root.hp_rebuild_startx, root.apr_rebuild_starty
	ComboBox:
		ltext: '防御%'
		pos: root.av_rebuild_startx, root.apr_rebuild_starty
	ComboBox:
		ltext: '格挡%'
		pos: root.bv_rebuild_startx, root.apr_rebuild_starty
	ComboBox:
		ltext: '暴伤'
		pos: root.cc_rebuild_startx, root.apr_rebuild_starty
		
	IELabel:
		text: f'重铸词条稀有度设置({root.minimal_degree}%)'
		width: 500
		height: root.rebuild_setting_height
		font_size: '10sp'
		size_hint: None, None
		text_size: self.size
		valign: 'middle'
		halign: 'left'
		pos: root.rebuild_setting_startx, root.minimal_setting_starty
		color: 153/255, 153/255, 153/255, 1
	
	RadioBox:
		ltext: '60%'
		pos: root.ap_rebuild_startx, root.degree_rebuild_starty
		#pos: 300, 300
	RadioBox:
		ltext: '70%'
		pos: root.hp_rebuild_startx, root.degree_rebuild_starty
	RadioBox:
		ltext: '80%'
		pos: root.av_rebuild_startx, root.degree_rebuild_starty
	RadioBox:
		ltext: '90%'
		pos: root.bv_rebuild_startx, root.degree_rebuild_starty
	RadioBox:
		ltext: '95%'
		pos: root.cc_rebuild_startx, root.degree_rebuild_starty
		
<Root>:

''')

class TicketCB(ToggleButton):
	def __init__(self, **kwagrs):
		super().__init__(**kwagrs)
		self.background_normal = 'icons/uncheck.jpg'
		self.background_down = 'icons/checked.jpg'
		self.size_hint = None, None
		self.text = ''

class DTextInput(TextInput):
	def __init__(self, **kwagrs):
		super().__init__(**kwagrs)

class DLabel(Label):
	#def __init__(self, label_startx, label_centery, **kwagrs):
	def __init__(self, **kwagrs):
		super().__init__(**kwagrs)
		self.font_size = '10sp'
		self.size_hint = None, None
		#self.size = self.texture_size[0], self.size[1]
		#text: root.item_upgrade_cost
		#self.pos = 373.5, 1742
		#self.x = label_startx
		#self.center_y = label_centery
		self.font_name = 'fonts/DroidSansFallback.ttf'

		with self.canvas.before:
			Color(0, 0, 1, 1)
			Rectangle(pos=self.pos, size=self.size)

class ImplicitLabel(Label):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.font_size = '11sp'
		self.size_hint = None, None
		self.font_name = 'fonts/DroidSansFallback.ttf'
		self.locked = False

		with self.canvas.before:
			Color(16/255, 16/255, 16/255, 1)
			Rectangle(pos=self.pos, size=self.size)

	def check_lock(self):
		if self.locked:
			height = self.size[1]
			width = height
			p1_x = self.pos[0] + self.size[0] - self.size[1]
			rect_xpad = 5
			rect_endx = self.pos[0] + self.size[0] - rect_xpad
			rect_startx = p1_x + width / 2 + rect_xpad
			rect_width = rect_endx - rect_startx
			rect_starty = self.pos[1] + height / 2
			rect_height = rect_width * 0.8
			print(f'[item_enforce.py] ImplicitLabel check_lock()')
			hole_r = rect_height * 0.1
			hole_startx = rect_startx + (rect_width - 2 * hole_r) / 2
			hole_starty = rect_starty + 0.5 * rect_height
			line_startx = hole_startx + hole_r
			line_endy = hole_starty
			line_length = 2 * hole_r
			line_starty = line_endy - line_length
			handle_r = rect_width / 2 * 0.7
			handle_startx = rect_startx + (rect_width - 2 * handle_r) / 2
			handle_starty = rect_starty + rect_height - handle_r
			with self.canvas.after:
				Color(1, 0, 0, 0.6)
				Triangle(points=[p1_x, \
								self.pos[1] + self.size[1], \
								self.pos[0] + self.size[0], \
								self.pos[1] + self.size[1], \
								self.pos[0] + self.size[0], \
								self.pos[1]])

				Color(1, 1, 1, 0.6)
				Line(rounded_rectangle=[rect_startx, rect_starty, rect_width, rect_height, 2], width=2)

				# keyhole
				Line(ellipse=[hole_startx, hole_starty, 2 * hole_r, 2 * hole_r], width=2)
				Line(points=[line_startx, line_starty, line_startx, line_endy], width=2)
				
				# handle
				Line(ellipse=[handle_startx, handle_starty, 2 * handle_r, 2 * handle_r, 90, -90], width=2)
				#Line(ellipse=[self.pos[0] + self.size[0] * 0.75, \
				#		self.pos[1] + self.size[1] * 0.695, \
				#		self.size[0] * 0.15, self.size[1] * 0.15, 90, -90], \
				#		width=2)
		else:
			if self.canvas.after:
				self.canvas.after.clear()

class UpArrowImage(Image):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		#self.x, self.y = kwargs['x'], kwargs['y']
		self.size_hint = None, None
		self.size = 45, 45
		self.allow_stretch = True
		self.source = 'icons/varrow.jpg'

class TicketImage(Image):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		#self.x, self.y = kwargs['x'], kwargs['y']
		self.size_hint = None, None
		self.size = 85, 80
		self.allow_stretch = True
		self.source = 'icons/misc/enforce_protect_ticket.jpg'

class DButton(Button):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.font_name = 'fonts/DroidSansFallback.ttf'
		#self.width, self.height = kwargs["width"], kwargs["height"]
		self.background_normal = ''
		self.background_color = (119 / 255, 102 / 255, 74 / 255, 1)

		with self.canvas.after:
			Color(1, 1, 1, 1)
			Line(rounded_rectangle=[self.pos[0], self.pos[1], self.size[0], self.size[1], 18], width=2)

class LockButton(Button):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.font_name = 'fonts/DroidSansFallback.ttf'
		#self.width, self.height = kwargs["width"], kwargs["height"]
		self.background_normal = ''
		self.background_color = (16 / 255, 16 / 255, 16 / 255, 1)
		self.font_size = '11sp'
		self.locked = False
		#self.bind(on_press=self.select)

		#color = Color(62/255, 123/255, 107/255)
		#with self.canvas.after:
		#	Color(62/255, 123/255, 107/255, 0.8)
		#	Line(rectangle=[self.pos[0], self.pos[1], self.size[0], self.size[1]], width=3)
		#with self.canvas.after:
		#	Color(1, 1, 1, 1)
		#	Line(rounded_rectangle=[self.pos[0], self.pos[1], self.size[0], self.size[1], 18], width=2)

		#if not self.selected:
		#	self.canvas.after.clear()
	def select(self):
		with self.canvas.after:
			Color(62/255, 123/255, 107/255, 0.8)
			Line(rectangle=[self.pos[0], self.pos[1], self.size[0], self.size[1]], width=3)

	def unselect(self):
		if self.canvas.after:
			self.canvas.after.clear()

	def display_text(self):
		if self.locked:
			self.text = "解锁"
		else:
			self.text = "锁定"

class ATTRLabel(Label):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.width, self.height = kwargs["width"], kwargs["height"]
		self.font_name = 'fonts/DroidSansFallback.ttf'
		self.font_size = '10sp'
		self.size_hint = None, None
		self.text_size = self.size
		self.valign = 'middle'
		self.halign = 'left'

class ItemEnforce(Widget):
	widget_startx = NumericProperty()
	widget_starty = NumericProperty()
	widget_width = NumericProperty()
	widget_height = NumericProperty()
	title_startx = NumericProperty()
	title_starty = NumericProperty()
	title_width = NumericProperty()
	title_height = NumericProperty()
	alpha = NumericProperty(5)
	title_word_height = NumericProperty(150)
	title_word_centery = NumericProperty()
	widget_bg_startx = NumericProperty()
	widget_bg_starty = NumericProperty()
	widget_bg_width = NumericProperty()
	widget_bg_height = NumericProperty()
	image_width = NumericProperty(125)
	image_height = NumericProperty(125)
	image_centerx = NumericProperty()
	image_centery = NumericProperty()
	item_name_x = NumericProperty()
	image_arrow_width = NumericProperty(45)
	image_arrow_height = NumericProperty(45)
	harrow_center_y = NumericProperty()
	harrow_x = NumericProperty()
	item_upgrade_x = NumericProperty()
	item_upgrade_centery = NumericProperty()
	btn_upgrade_width = NumericProperty(275)
	btn_upgrade_height = NumericProperty(95)
	btn_upgrade_centerx = NumericProperty()
	btn_upgrade_centery = NumericProperty()
	lbl_upgrade_width = NumericProperty(100)
	cb_ticket_startx = NumericProperty()
	cb_ticket_starty = NumericProperty()
	implicit_rebuild_centery = NumericProperty()
	rebuild_setting_startx = NumericProperty()
	rebuild_setting_starty = NumericProperty()
	rebuild_setting_width = NumericProperty(500)
	rebuild_setting_height = NumericProperty(95)
	ap_rebuild_startx = NumericProperty()
	ap_rebuild_starty = NumericProperty()
	hp_rebuild_startx = NumericProperty()
	av_rebuild_startx = NumericProperty()
	bv_rebuild_startx = NumericProperty()
	cc_rebuild_startx = NumericProperty()
	apr_rebuild_starty = NumericProperty()
	minimal_degree = NumericProperty()
	minimal_setting_starty = NumericProperty()
	degree_rebuild_starty = NumericProperty()
	def __init__(self, ww, wh, backpack_idx, **kwargs):
		super().__init__(**kwargs)
		#self.pos = kwargs['pos']
		#w, h = 1400, 800
		#self.alpha = alpha
		self.widget_width = kwargs['width']
		#alpha = 5
		self.widget_startx = (ww - self.widget_width) / 2
		self.title_startx = self.widget_startx + self.alpha
		self.widget_bg_startx = self.title_startx
		self.title_width = self.widget_width - 2 * self.alpha
		self.widget_bg_width = self.title_width
		widget_yoffset = 304 - self.alpha
		#widget_endy = wh - widget_yoffset
		widget_endy = 2800
		title_endy = widget_endy - self.alpha
		self.title_height = 150
		self.title_starty = title_endy - self.title_height

		# title word
		title_word_starty = self.title_starty - self.title_word_height
		self.title_word_centery = title_word_starty + self.title_word_height / 2

		# image
		item = self.from_backpack(backpack_idx)
		kind = item[0]['kind']
		item_id = item[0]['ID']
		self.image_source = f'icons/item/{kind}/{item_id}.jpg'

		#2407 - 125 = 2282
		image_starty = title_word_starty - self.image_height
		print(f'[item_enforce.py] __init__ (titel_word_starty={title_word_starty}, image_starty={image_starty})')
		#self.image_centerx = self.title_startx + self.title_width / 2
		self.image_centery = image_starty + self.image_height / 2

		# item name
		name = item[0]['name']
		self.item_name = f'{name}(+15)'

		# name label length
		pixel_per_word = 32
		name_len = len(self.item_name) * pixel_per_word
		print(f'[item_enforce.py] __init__ (name_len={name_len}, len_word{len(self.item_name)}))')

		name_spacex = 15

		# name + image
		total_name_len = self.image_width + name_len + name_spacex

		# title_startx = 112.5
		# len = 405
		# title_width = 1215 - 405 = 810 / 2 = 405 + 62.5 =
		print(f'[item_enforce.py] __init__ (title_startx={self.title_startx})')
		self.image_centerx = self.title_startx + (self.title_width - total_name_len) / 2 + self.image_width / 2
		print(f'[item_enforce.py] __init__ (total_name_len={total_name_len}, image_centerx={self.image_centerx})')

		image_endx = self.image_centerx + self.image_width
		self.item_name_x = image_endx + name_spacex

		# attrs to upgrade
		attrs = item[0]['attr']

		# 5% for upgrade
		# arror = "⇨"
		attr_spacey = 20
		attr_endy = image_starty - attr_spacey
		label_height = 40
		label_space = 10
		label_yoffset = label_height + label_space
		attr_starty = attr_endy
		label_xpad = 100
		attr_startx = self.title_startx + label_xpad
		up_spacex = 600
		attr_up_startx = attr_startx + up_spacex
		#max_label_length
		attr_label_width = 300
		attr_up_label_width = 500
		attr_pixel_per_word = 22
		for key in attrs.keys():
			label_text = f' {translate.item_attr[key]}: + {attrs[key]["value"]}'
			print(print(f'[item_enforce.py] __init__ (attrs[{label_text}])'))
			#if key in ['crit', 'gold', 'damage']:
			#	label_text += f' %'

			up_value = int(attrs[key]["value"] * 1.05)
			diff = round(up_value - attrs[key]["value"], 1)
			diff_text = f'({diff})'
			label_text_upgrade = f' {translate.item_attr[key]}: + {up_value}' # ⇧ ({diff})'
			attr_starty = attr_starty - label_yoffset
			attr_label_width = attr_pixel_per_word * len(label_text)
			attr = ATTRLabel(text=label_text, pos=(attr_startx, attr_starty), width=attr_label_width, height=40)
			print(print(f'[item_enforce.py] __init__ (attr_label_width={attr_label_width})'))
			print(print(f'[item_enforce.py] __init__ (attr_startx={attr_startx}, attr_starty={attr_starty})'))
			self.add_widget(attr)
			attr_up_label_width = attr_pixel_per_word * len(label_text_upgrade)
			attr_up = ATTRLabel(text=label_text_upgrade, pos=(attr_up_startx, attr_starty), \
								width=attr_up_label_width, height=40)
			self.add_widget(attr_up)

			# Arrow Image
			image_space_x = 10
			image_startx = attr_up_startx + attr_up_label_width + image_space_x
			image_starty = attr_starty
			arrow_image = UpArrowImage(pos=(image_startx, image_starty))
			self.add_widget(arrow_image)

			diff_space_x = 5
			diff_startx = image_startx + self.image_arrow_width + diff_space_x
			diff_label_width = attr_pixel_per_word * len(diff_text)
			diff_label = ATTRLabel(text=diff_text, pos=(diff_startx, attr_starty), \
								width=diff_label_width, height=40)
			self.add_widget(diff_label)

		attrs_height = attr_endy - attr_starty
		self.harrow_center_y = attr_starty + attrs_height / 2
		#self.harrow_x = self.title_startx + self.title_width / 2
		#self.harrow_x = attr_startx + up_spacex / 2
		attr_endx = attr_startx + attr_label_width
		harrow_centerx = attr_endx + (attr_up_startx - attr_endx) / 2
		self.harrow_x = harrow_centerx - self.image_arrow_width / 2

		# upgrade
		upgrade_space_y = 70
		upgbtn_endy = attr_starty - upgrade_space_y
		upgbtn_starty = upgbtn_endy - self.btn_upgrade_height

		# pixel per word for upg label
		lbl_upg_ppw = 24
		chance = 92.5
		cost = "8875.11万"
		self.item_upgrade_cost = f'需要金币({chance} %成功): {cost}'
		text_len = len(self.item_upgrade_cost)
		self.lbl_upgrade_width = lbl_upg_ppw * text_len
		print(f'[item_enforce.py] __init__(lbl_upgrade_width={self.lbl_upgrade_width})')
		total_upg_width = self.lbl_upgrade_width + self.btn_upgrade_width
		self.item_upgrade_x = self.title_startx + (self.title_width - total_upg_width) / 2
		print(f'[item_enforce.py] __init__(item_upgrade_x={self.item_upgrade_x})')
		self.item_upgrade_centery = upgbtn_starty + self.btn_upgrade_height / 2

		lbl_upg = DLabel(text=self.item_upgrade_cost, pos=(self.item_upgrade_x, upgbtn_starty), \
							 width=self.lbl_upgrade_width, height=self.btn_upgrade_height)
		self.add_widget(lbl_upg)

		upgbtn_space_x = 10
		upgbtn_startx = self.item_upgrade_x + self.lbl_upgrade_width + upgbtn_space_x
		print(f'[item_enforce.py] __init__(upgbtn_startx={upgbtn_startx})')
		self.btn_upgrade_centerx = upgbtn_startx + self.btn_upgrade_width / 2
		self.btn_upgrade_centery = upgbtn_starty + self.btn_upgrade_height / 2
		lv = item[0]["lv"]
		self.upgrade_level = f'强化至+{lv+1}'

		auto_enforce = True
		dstarty = upgbtn_starty
		if auto_enforce:
			# success cost
			success_space_y = 30
			btnsuccess_endy = upgbtn_starty - success_space_y
			btnsuccess_starty = btnsuccess_endy - self.btn_upgrade_height
			success_cost = "4.54亿"
			lbl_success_text = f'需要金币(100%成功): {success_cost}'
			success_label_width = lbl_upg_ppw * len(lbl_success_text)
			print(f'[item_enforce.py] __init__(success_label_width={success_label_width})')
			total_succ_width = success_label_width + self.btn_upgrade_width
			print(f'[item_enforce.py] __init__(total_succ_width={total_succ_width})')
			lbl_success_startx = self.title_startx + (self.title_width - total_succ_width) / 2
			print(f'[item_enforce.py] __init__(lbl_success_startx={lbl_success_startx}, btnsuccess_starty={btnsuccess_starty})')

			#lbl_height = self.btn_upgrade_height
			#lbl_success_startx = self.title_startx + label_xpad
			lbl_success_centery = btnsuccess_starty + self.btn_upgrade_height / 2
			#lbl_success = DLabel(text=lbl_success_text, label_startx=lbl_success_startx, \
			#					 label_centery=lbl_success_centery)
			#lbl_success = DLabel(text=lbl_success_text, x=lbl_success_startx, center_y=lbl_success_centery)
			lbl_success = DLabel(text=lbl_success_text, pos=(lbl_success_startx, btnsuccess_starty), \
								 width=success_label_width, height=self.btn_upgrade_height)
			self.add_widget(lbl_success)

			btn_space_x = 10
			succ_btn_startx = lbl_success_startx + success_label_width + btn_space_x
			succ_btn_centerx = succ_btn_startx + self.btn_upgrade_width / 2
			succ_btn_centery = btnsuccess_starty + self.btn_upgrade_height / 2
			succ_level_text = self.upgrade_level
			print(f'[item_enforce.py] __init__(succ_btn_startx={succ_btn_startx})')
			succ_btn = DButton(text=succ_level_text, pos=(succ_btn_startx, btnsuccess_starty),\
							   width=self.btn_upgrade_width, height=self.btn_upgrade_height)
			self.add_widget(succ_btn)

			# auto_enforce label
			btn_auto_enforce_endy = btnsuccess_starty - success_space_y
			btn_auto_enforce_starty = btn_auto_enforce_endy - self.btn_upgrade_height
			autoenforce_text = f'自动强化目标等级: '
			lbl_auto_ppw = 31
			auto_label_width = lbl_auto_ppw * len(autoenforce_text)
			input_width = 120
			auto_input_space_x = 10
			total_auto_width = auto_label_width + input_width + auto_input_space_x * 2 + self.btn_upgrade_width
			lbl_auto_startx = self.title_startx + (self.title_width - total_auto_width) / 2
			print(f'[item_enforce.py] __init__(lbl_auto_startx={lbl_auto_startx}, auto_label_width={auto_label_width})')
			lbl_auto = DLabel(text=autoenforce_text, pos=(lbl_auto_startx, btn_auto_enforce_starty), \
								 width=auto_label_width, height=self.btn_upgrade_height)
			self.add_widget(lbl_auto)

			# text input
			auto_input_startx = lbl_auto_startx + auto_label_width + auto_input_space_x
			auto_input = DTextInput(pos=(auto_input_startx, btn_auto_enforce_starty), \
								 width=input_width, height=self.btn_upgrade_height)
			self.add_widget(auto_input)

			# auto enforce btn
			btn_auto_enforce_startx = auto_input_startx + input_width + auto_input_space_x
			auto_btn = DButton(text='自动强化', pos=(btn_auto_enforce_startx, btn_auto_enforce_starty), \
							   width=self.btn_upgrade_width, height=self.btn_upgrade_height)
			self.add_widget(auto_btn)

			dstarty = btn_auto_enforce_starty
		else:
			pass

		# Ticket Image
		ticket_yoffset = 50
		ticket_image_endy = dstarty - ticket_yoffset
		ticket_width = 85
		ticket_height = 80
		ticket_image_starty = ticket_image_endy - ticket_height
		ticket_padx = 120
		ticket_image_startx = self.title_startx + ticket_padx
		ticket_image = TicketImage(pos=(ticket_image_startx, ticket_image_starty))
		self.add_widget(ticket_image)
		lbl_ticket_spacex = 20
		lbl_ticket_startx = ticket_image_startx + ticket_width + lbl_ticket_spacex
		ticket_num = 15
		lbl_ticket_text = f'强化保护券：X{ticket_num}'
		lbl_ticket_ppw = 31
		lbl_ticket_width = lbl_ticket_ppw * len(lbl_ticket_text)
		lbl_ticket = DLabel(text=lbl_ticket_text, pos=(lbl_ticket_startx, ticket_image_starty), \
						  width=lbl_ticket_width, height=ticket_height)
		self.add_widget(lbl_ticket)

		# ticket used
		lbl_ticket_used_endx = self.title_startx + self.title_width - ticket_padx
		lbl_ticket_used_text = f'使用保护券'
		lbl_ticket_used_ppw = 35
		lbl_ticket_used_width = lbl_ticket_used_ppw * len(lbl_ticket_used_text)
		lbl_ticket_used_startx = lbl_ticket_used_endx - lbl_ticket_used_width
		lbl_ticket_used = DLabel(text=lbl_ticket_used_text, pos=(lbl_ticket_used_startx, ticket_image_starty), \
								 width=lbl_ticket_used_width, height=ticket_height)
		self.add_widget(lbl_ticket_used)

		cb_width = 48
		cb_height = 48
		cb_ticket_startx = lbl_ticket_used_startx - cb_width - lbl_ticket_spacex
		cb_ticket_starty = ticket_image_starty + (ticket_height - cb_height) / 2
		cb_ticket = TicketCB(pos=(cb_ticket_startx, cb_ticket_starty), size=(cb_width, cb_height))
		self.add_widget(cb_ticket)

		# implioit rebuild
		implicit_rebuild_yoffset = 50
		implicit_rebuild_starty = ticket_image_starty - implicit_rebuild_yoffset - self.title_word_height
		self.implicit_rebuild_centery = implicit_rebuild_starty + self.title_word_height / 2

		# rebuild setting
		rebuild_setting_yoffset = 20
		self.rebuild_setting_startx = attr_startx
		self.rebuild_setting_starty = implicit_rebuild_starty - rebuild_setting_yoffset - self.btn_upgrade_height

		btn_auto_rebuild_endx = self.title_startx + self.title_width - label_xpad
		btn_auto_rebuild_startx = btn_auto_rebuild_endx - self.btn_upgrade_width

		auto_rebuild_btn = DButton(text='自动重铸', pos=(btn_auto_rebuild_startx, self.rebuild_setting_starty), \
						   width=self.btn_upgrade_width, height=self.btn_upgrade_height)
		self.add_widget(auto_rebuild_btn)

		# rebuild settings
		rebuild_settings_yoffset = 20
		self.ap_rebuild_startx = attr_startx
		print(f'[item_enforce.py] __init__(rebuild_setting_starty={self.rebuild_setting_starty})')
		self.ap_rebuild_starty = self.rebuild_setting_starty - cb_height - rebuild_settings_yoffset
		print(f'[item_enforce.py] __init__(ap_rebuild_starty={self.ap_rebuild_starty})')
		settings_xspace = 200
		self.hp_rebuild_startx = self.ap_rebuild_startx + settings_xspace
		self.av_rebuild_startx = self.hp_rebuild_startx + settings_xspace
		self.bv_rebuild_startx = self.av_rebuild_startx + settings_xspace
		self.cc_rebuild_startx = self.bv_rebuild_startx + settings_xspace

		# setting 2nd line
		self.apr_rebuild_starty = self.ap_rebuild_starty - cb_height - rebuild_settings_yoffset

		# degree setting
		degree_settings_yoffset = 20
		self.minimal_setting_starty = self.apr_rebuild_starty - degree_settings_yoffset - self.rebuild_setting_height
		# set degree
		self.minimal_degree = 80

		# radio setting
		degree_rebuild_yoffset = 20
		radio_height = 48
		self.degree_rebuild_starty =  self.minimal_setting_starty - degree_rebuild_yoffset - radio_height

		# implicits
		implicits_yoffset = 20
		implicits_yspace = 50
		lbl_implicit_starty = self.degree_rebuild_starty
		lbl_implicit_height = 70
		lbl_implicit_width = 700
		implicits = item[0]['implicit']
		print(f'[item_enforce.py] __init__(implicits={implicits})')
		btn_lock_endx = btn_auto_rebuild_endx
		btn_lock_width = 250
		btn_lock_height = 70
		btn_lock_startx = btn_lock_endx - btn_lock_width

		self.btn_locks = []
		self.lbl_implicits = []
		for imp in implicits:
			k, v = list(imp.keys())[0], list(imp.values())[0]
			label_text = f'{translate.item_implicit[k]}: +{v}'
			if k in ['HP_RATE', 'ARMOR_RATE', 'ATTACK_RATE', 'DAMAGE_RATE', 'CRIT_RATE']:
				label_text += f'%'
			lbl_implicit_starty = lbl_implicit_starty - lbl_implicit_height - implicits_yspace
			lbl_implicit = ImplicitLabel(text=label_text, pos=(attr_startx, lbl_implicit_starty), \
								 width=lbl_implicit_width, height=lbl_implicit_height)
			#imp_starty = imp_starty - implicit_yoffset
			#implicit = ATTRLabel(text=label_text, pos=(imp_startx, imp_starty))
			self.add_widget(lbl_implicit)
			self.lbl_implicits.append(lbl_implicit)
			#text = translate.item_implicit[k]
			#print(f'[item_enforce.py] __init__(text={text})')
			btn_lock = LockButton(text='锁定', pos=(btn_lock_startx, lbl_implicit_starty), \
						   width=btn_lock_width, height=btn_lock_height)
			self.add_widget(btn_lock)
			self.btn_locks.append(btn_lock)

		btn_index = 0
		for btn in self.btn_locks:
			# partial(self.on_anything, "1", "2", monthy="python")
			#btn.bind(on_press=partial(self.btn_lock_select, "1", "2", monthy="python"))
			btn.bind(on_press=partial(self.btn_lock_select, index=btn_index))
			btn_index += 1
		self.widget_bg_starty = lbl_implicit_starty - implicits_yspace
		self.widget_bg_height = title_endy - self.widget_bg_starty

		self.widget_starty = self.widget_bg_starty - self.alpha
		self.widget_height = widget_endy - self.widget_starty

		print(self.widget_startx, self.widget_starty, self.widget_width, self.widget_height)
		print(self.title_startx, self.title_starty, self.title_width, self.title_height)


	#def btn_lock_select(self, *args, **kwargs):
	#	print(f'[item_enforce.py] btn_lock_select(index={str(args)}, {str(kwargs)})')

	def btn_lock_select(self, *args, **kwargs):
		index = kwargs["index"]
		print(f'[item_enforce.py] btn_lock_select(index={index})')
		self.btn_locks[index].select()
		self.btn_locks[index].locked = not self.btn_locks[index].locked
		self.btn_locks[index].display_text()

		# lock image display
		self.lbl_implicits[index].locked = not self.lbl_implicits[index].locked
		self.lbl_implicits[index].check_lock()


	def from_backpack(self, idx):
		file = 'data/profile.json'
		if platform == 'android':
			file = f'/storage/emulated/0/BraveHeart/{file}'
		with open(file, "r") as f:
			data = json.load(f)
		item = data['bag'][idx]
		return item

class Root(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		#ie = ItemEnforce(pos=(50, 250), size=(100, 200))
		ie = ItemEnforce(ww=1400, wh=800, width=1225, backpack_idx=0)
		self.add_widget(ie)

class MainApp(App):
	def build(self):
		from kivy.core.window import Window
		#Window.size = [1440, 2911]
		Window.size = [1400, 800]
		Window.clearcolor = 1, 1, 1, 1
		return Root()

if __name__ == '__main__':
	MainApp().run()
