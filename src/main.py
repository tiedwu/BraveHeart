__version__ = '0.3'

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import platform
from kivy.properties import ObjectProperty, NumericProperty, StringProperty
from kivy.config import Config

from kivy.clock import Clock

Config.set('graphics', 'resizable', True)

# import os to show gif?
import os
os.environ["KIVY_IMAGE"] = "pil,sdl2"
import kivy

import json

# import osc
from oscpy.client import OSCClient
from oscpy.server import OSCThreadServer

# data init
import init_data
import item_effect

from dungeon import Dungeon
from home import HomeWidget
from bag import Bag
from bead_box import BeadWidget
from item_enforce import ItemEnforce

ratio = 1

Window.size = 1440 // ratio, 2911 // ratio

mw, mh = map_size = 480, 480

Builder.load_string('''
#:import utils kivy.utils

<LVLabel@Label,GoldLabel@Label,CELabel@Label>:
	#font_name: 'fonts/JetBrainsMono-Regular.ttf'
	font_name: 'fonts/DroidSansFallback.ttf'
	#font_name: 'fonts/sarasa-ui-cl-regular.ttf'
<LVBox>:
	player_level: 0
	samsara: 0
	reincarnation: 0
	orientation: 'vertical'
	canvas.before:
		Color:
			rgba: utils.get_color_from_hex('#33322F7F')
		Rectangle:
			size: self.size
			pos: self.pos
	LVLabel:
		id: lv_label
		#font_size: 28
		color: (244/255, 252/255, 3/255, 1)
		text: ' '* 5 + 'LV ' + str(root.player_level) + ' ' * 5
	BoxLayout:
		LVLabel:
			#font_size: 24
			id: samsara
			text_size: self.size
			text: u' 轮回 ' + str(root.samsara) + u' 次'
			halign: 'left'
			valign: 'bottom'
			color: (3/255, 252/255, 240/255, 1)
			#color: (3/255, 198/255, 252/255, 1)
		LVLabel:
			id: reincarnation
			#font_size: 24
			text_size: self.size
			text: u'转生 ' + str(root.reincarnation) + ' 次 '
			halign: 'right'
			valign: 'bottom'
			color: (3/255, 252/255, 240/255, 1)

<GoldBox>:
	gold: self.parent.gold
	canvas.before:
		Color:
			rgba: utils.get_color_from_hex('#33322F7F')
		Rectangle:
			size: self.size
			pos: self.pos
	Image:
		source: 'icons/coin.png'
		size: 80, 80
		size_hint: None, None
	GoldLabel:
		id: gold_label
		text: f'{root.gold}'
		text_size: self.size
		halign: 'right'
		valign: 'middle'

<CEBox>:
	ce: self.parent.ce
	canvas.before:
		Color:
			rgba: utils.get_color_from_hex('#33322F7F')
		Rectangle:
			size: self.size
			pos: self.pos

	Image:
		source: 'icons/combat.png'
		size: 80, 80
		size_hint: None, None
	CELabel:
		text_size: self.size
		halign: 'right'
		valign: 'middle'
		text: f'{root.ce} '

<PFLabel@Label>:
	font_size: '14sp'
	font_name: 'fonts/DroidSansFallback.ttf'

<PFBox>:

	max_hp: self.parent.max_hp
	current_hp: self.parent.current_hp
	ap: self.parent.ap
	crit_chance: self.parent.crit_chance
	crit_damage: self.parent.crit_damage
	av: self.parent.av
	bv: self.parent.bv
	av_ratio: self.parent.av_ratio

	padding: 20
	canvas.before:
		Color:
			rgba: utils.get_color_from_hex('#33322F7F')
		Rectangle:
			size: self.size
			pos: self.pos

	RelativeLayout:
		width: root.ww * 0.5 - 40
		height: root.wh * 0.18 - 40
		id: top_left
		size_hint: None, None
		window_width: 1440

		# hp full: 100%
		hp_remain: 100
		canvas:
			Color:
				rgba: 1, 1, 1, 1
			Rectangle:
				pos: top_left.size[0] * 0.15, top_left.size[1] * 0.9
				size: top_left.size[0] * 0.85, 30
			Color:
				rgba: 0, 1, 0, 1
			Rectangle:
				pos: self.size[0] * 0.15, self.size[1] * 0.9
				#size: self.size[0] * 0.7 * (self.hp_remain / 100), 30
				size: self.size[0] * 0.85, 30

		# HP
		Image:
			size_hint: None, None
			source: 'icons/hp.png'
			pos_hint: {'x': 0, 'y': 0.82}
			size: [top_left.window_width/(top_left.window_width/80),\
					top_left.window_width/(top_left.window_width/80)]

		Label:
			#font_size: '10sp'
			id: show_hp
			size_hint: None, None
			size: top_left.size[0] * 0.6, self.size[1]
			pos_hint: {'x': 0.4, 'y': 0.73}
			text_size: self.size
			text: f'{root.current_hp}/{root.max_hp}'
			halign: 'right'
			valign: 'middle'

		# ATTACK
		Image:
			size_hint: None, None
			source: 'icons/attack.png'
			pos_hint: {'x': 0, 'y': 0.55}

		PFLabel:
			id: show_attack
			size_hint: None, None
			#font_size: '12sp'
			size: top_left.size[0] * 0.35, self.size[1]
			x: top_left.size[0] * 0.1
			y: top_left.size[1] * 0.55
			text_size: self.size
			text: f'{root.ap}'
			halign: 'right'
			valign: 'middle'

		# critical rate
		Image:
			size_hint: None, None
			source: 'icons/crit_rate.png'
			pos_hint: {'x': 0.5, 'y': 0.55}

		PFLabel:
			id: show_critrate
			size_hint: None, None
			size: top_left.size[0] * 0.6, self.size[1]
			x: top_left.size[0] * 0.4
			y: top_left.size[1] * 0.55
			#font_size: '12sp'
			text_size: self.size
			text: f'{root.crit_chance}%'
			halign: 'right'
			valign: 'middle'

		# crit damage
		Image:
			size_hint: None, None
			source: 'icons/crit_dmg.png'
			pos_hint: {'x': 0, 'y': 0.3}

		PFLabel:
			id: show_critdmg
			size_hint: None, None
			#font_size: '12sp'
			size: top_left.size[0] * 0.35, self.size[1]
			x: top_left.size[0] * 0.1
			y: top_left.size[1] * 0.3
			text_size: self.size
			text: f'{root.crit_damage}%'
			halign: 'right'
			valign: 'middle'

		# armor
		Image:
			size_hint: None, None
			source: 'icons/armor.png'
			pos_hint: {'x': 0.5, 'y': 0.3}

		PFLabel:
			id: show_armor
			size_hint: None, None
			size: top_left.size[0] * 0.6, self.size[1]
			x: top_left.size[0] * 0.4
			y: top_left.size[1] * 0.3
			font_size: '11sp'
			text_size: self.size
			text: f'{root.av}\\n({root.av_ratio}%) '
			halign: 'right'
			valign: 'middle'

		# block
		Image:
			size_hint: None, None
			source: 'icons/block.png'
			pos_hint: {'x': 0, 'y': 0.05}
			#size: 125, 125

		PFLabel:
			id: show_block
			size_hint: None, None
			#font_size: '12sp'
			size: top_left.size[0] * 0.35, self.size[1]
			x: top_left.size[0] * 0.1
			y: top_left.size[1] * 0.05
			text_size: self.size
			text: f'{root.bv}'
			halign: 'right'
			valign: 'middle'

		# profile
		Image:
			size_hint: None, None
			source: 'icons/profile.png'
			pos_hint: {'x': 0.5, 'y': 0.05}

		PFLabel:
			id: show_profile
			size_hint: None, None
			size: top_left.size[0] * 0.6, self.size[1]
			x: top_left.size[0] * 0.4
			y: top_left.size[1] * 0.05
			#font_size: '11sp'
			text_size: self.size
			text: "详细属性"
			halign: 'right'
			valign: 'middle'

<EQLabel@Label>:
	font_name : 'fonts/DroidSansFallback.ttf'

<EQWidget>:
	size: root.ww * 0.5, (root.wh * 0.185 - 40 ) // 4
	size_hint: 1, None
	ltext: ''
	item_id: ''
	item_image: ''
	Label:
		size_hint: 0.05, 1
		text: ''
	Image:
		canvas:
			Color:
				rgba: 1, 0, 0, 1
			Line:
				width: 3
				rectangle: self.x, self.y, self.width, self.height
		size_hint: None, None
		source: root.item_image
		#source: 'icons/weapon.jpg'
		size: 80, 80
		#pos: 2, self.y
		pos_hint: {'center_y': 0.5}

	EQLabel:
		text: root.ltext
		#text: 'sword'

	Button:
		size_hint: 0.2, 0.8
		center_x: self.parent.center_x
		center_y: self.parent.center_y
		text: ''
		background_color: 0, 0, 0, 0
		on_press: root.show_on(root.item_id)
		Image:
			size_hint: None, None
			source: 'icons/upgrade.jpg'
			size: 80, 80
			center_x: self.parent.center_x
			center_y: self.parent.center_y

<EQBox>:
	padding: 20
	orientation: 'vertical'
	canvas.before:
		Color:
			#rgba: utils.get_color_from_hex('#33322F7F')
			rgba: 0, 0, 0, 1
		Rectangle:
			size: self.size
			pos: self.pos
	EQWidget:
		id: weapon
	EQWidget:
		id: suit
	EQWidget:
		id: necklace
	EQWidget:
		id: ring

<LOGLabel@Label>:
	font_size: '14sp'
	font_name: 'fonts/DroidSansFallback.ttf'

<LOGBox>:
	log_text: self.parent.log_text
	orientation: 'vertical'
	canvas.before:
		Color:
			#rgba: 240/255, 166/255, 29/255, 0.2
			rgba: 14/255, 28/255, 11/255, 1
		Rectangle:
			pos: self.pos
			size: self.size

	BoxLayout:
		size_hint_y: None
		height: 64

		canvas.before:
			Color:
				rgba: 3/255, 3/255, 2/255, 0.8
			Rectangle:
				pos: self.pos
				size: self.size

		Image:
			size_hint: None, None
			source: 'icons/info.png'
			size: 64, 64

		LOGLabel:
			text: '系统信息'
			text_size: self.size
			valign: 'middle'
			halign: 'center'

	ScrollView:
		scroll_type: ['bars', 'content']
		bar_width: 10
		LOGLabel:
			id: log_label
			markup: True
			size_hint_y: None
			height: self.texture_size[1]
			text_size: self.width, None
			text: root.log_text
			padding: 5, 5

<BeadLabel@Label>:
	font_size: '14sp'
	font_name: 'fonts/DroidSansFallback.ttf'

<BeadButton@ToggleButton>:
	group: 'bead_select'
	size_hint: None, None
	size: 60, 60
	pos_hint: {'center_y': 0.5}

<BeadBox>:
	canvas.before:
		Color:
			rgba: 2/255, 2/255, 2/255, 0.8
		Rectangle:
			pos:self.pos
			size: self.size

	spacing: 30
	padding: 20, 0
	Image:
		source: 'icons/bead.png'
		size_hint: None, None
		#size: 80, 80
		center_y: self.parent.center_y

	BeadLabel:
		text: '切换'
		text_size: self.size
		halign: 'left'
		valign: 'middle'

	BeadButton:
		text: '1'
		state: 'down'
	BeadButton:
		text: '2'
	BeadButton:
		text: '3'

<MenuLabel@Label>:
	font_size: '12sp'
	font_name: 'fonts/DroidSansFallback.ttf'

<MenuButton@ToggleButton>:
	group: 'menu_select'
	size_hint: None, None
	size: 140, 160
	pos_hint: {'center_y': 0.5}
	background_color: 0, 0, 0, 1
	btn_image: 'icons/menu/bag.png'
	btn_text: ''
	
	BoxLayout:
		orientation: 'vertical'
		pos: self.parent.pos
		size: self.parent.size
		Image:
			source: root.btn_image
			size_hint_y: 0.7
			allow_stretch: True
		MenuLabel:
			size_hint_y: 0.3
			width: 140
			text: root.btn_text
			text_size: self.size
			halign: 'center'

<MenuBox>:
	padding: 50, 5
	spacing: 60
	MenuButton:
		btn_text: '背包'
		btn_image: 'icons/menu/bag.png'
		on_press: self.parent.parent.show_bag()
	MenuButton:
		btn_text: '精气珠'
		btn_image: 'icons/menu/mbead.png'
		on_press: self.parent.parent.show_beadbox()
	MenuButton:
		btn_text: '宠物'
		btn_image: 'icons/menu/pet.png'
	MenuButton:
		btn_text: '商店'
		btn_image: 'icons/menu/store.png'
	MenuButton:
		btn_text: '转生'
		btn_image: 'icons/menu/reincarnate.png'
	MenuButton:
		btn_text: '成就'
		btn_image: 'icons/menu/achievement.png'
	MenuButton:
		btn_text: '图鉴'
		btn_image: 'icons/menu/illustrate.png'

<FuncBox>:
	ToggleButton:
		group: 'func_select'
		text: ''
		background_normal: 'icons/func/setting.png'
		background_down: 'icons/func/setting.png'
		size_hint: None, None
		size: 100, 100

<RootWidget>:
	lv_box: lv_box
	canvas:
		Color:
			rgba: utils.get_color_from_hex('#6B6863')
			#rgba: 0, 0, 1, 1
		Rectangle:
			pos: 0, 0
			size: root.ww, root.wh/15

		Color:
			rgba: utils.get_color_from_hex('#73B5D3')
		Rectangle:
			pos: 0, root.wh // 15
			size: root.ww, root.ww
			#source: 'worldmap_480_480.png'
			source: 'images/worldmap.png'

		Color:
			rgba: utils.get_color_from_hex('#615D51')
		Rectangle:
			pos: 0, (root.wh // 15 + root.ww)
			size: root.ww, root.wh - root.wh // 15 - root.ww

		Color:
			#rgba: utils.get_color_from_hex('#615D51')
			rgba: 179.255, 156/255, 93/255, 1
		Rectangle:
			pos: 0, 0
			size: root.ww, root.wh * 0.065

	LVBox:
		id: lv_box
		x: 0
		y: 0.935 * root.wh
		size_hint: 0.5, 0.05

	GoldBox:
		id: gold_box
		x: 0.5 * root.ww + 5
		y: 0.95 * root.wh
		size_hint: 0.23, 0.03

	CEBox:
		id: ce_box
		x: 0.73 * root.ww + 10
		y: 0.95 * root.wh
		size_hint: 0.255, 0.03

	PFBox:
		id: pf_box
		x: 0
		y: 0.75 * root.wh
		size_hint: 0.5, 0.18 

	EQBox:
		id: eq_box
		x: 0
		y: 0.56 * root.wh
		size_hint: 0.5, 0.185

	LOGBox:
		id: log_box
		x: 0.5 *  root.ww + 5
		y: 0.6 * root.wh
		#size: 300, 500
		size_hint: 0.49, 0.345

	BeadBox:
		id: bead_box
		x: 0.5 * root.ww + 5
		y: 0.56 * root.wh
		size_hint: 0.49, 0.037

	MenuBox:
		id: menu_box
		size_hint: 1, 0.065

	FuncBox:
		id: func_box
		size_hint: 0.1, 0.05
		pos_hint: {'center_x': 0.95, 'center_y': 0.1}

''')

class FuncBox(BoxLayout):
	pass

class MenuBox(BoxLayout):
	pass

class BeadBox(BoxLayout):
	ww, wh = Window.size

class LOGBox(BoxLayout):
	ww, wh = Window.size

class EQWidget(BoxLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.ww, self.wh = Window.size

	def show_on(self, item):
		print("show_on(): ", item)

class EQBox(BoxLayout):

	def __init__(self, **kwargs):
		super().__init__(**kwargs)

class PFBox(BoxLayout):
	ww, wh = Window.size
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		#self.max_hp = 123

class CEBox(BoxLayout):
	pass

class LVBox(BoxLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		#print("LVBox: ", self.ids)

class GoldBox(BoxLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		#print("GoldBox: ", self.ids)

class RootWidget(Screen):
	ww, wh = Window.size
	mw, mh = 480, 480

	# define attributes
	max_hp = NumericProperty(0)
	current_hp = NumericProperty(0)
	ap = NumericProperty(0)
	crit_chance = NumericProperty(0)
	crit_damage = NumericProperty(0)
	av = NumericProperty(0)
	av_ratio = NumericProperty(0)
	bv = NumericProperty(0)

	# define combat effectiveness
	ce = NumericProperty(0)

	# define gold
	gold = NumericProperty(0)

	# define log text
	log_text = StringProperty('')

	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		#print("RootWidget: ", self.ids.eq_box.ids)

		# init attributes
		self.player_level = 0
		self.max_hp = 0
		self.current_hp = 0
		self.ap = 0
		self.crit_chance = 0
		self.crit_damage = 0
		self.av = 0
		self.bv = 0

		self.av_ratio = 0

		self.ce = 0
		self.gold = 0

		self.init_player_data()

		# load backpack
		self.bag = Bag()
		#from kivy.core.window import Window
		# get screen_size
		#screen_width, screen_height = Window.size[0], Window.size[1]
		#print(f'[main.py] __init__(screen_width={screen_width}, screen_height={screen_height})')

		self.beadbox = BeadWidget(screen_width=self.ww, screen_height=self.wh)
		self.load_backpack()

		# add dungeon
		self.dungeon = Dungeon()
		self.dungeon.ids.dungeon_exit.bind(on_press=self.exit_dungeon)

		self.add_widget(self.dungeon)
		self.dungeon.hide_me()

		self.home = HomeWidget()
		self.home.random_generate(level=1)
		self.add_widget(self.home)

		# bind zone_info button calls
		self.home.zone_info.ids.btn_challenge.bind(
			on_press=self.instance_challenge)

		# bind home button calls
		self.home.ids.gen_instance.bind(on_release=self.generate_instance)

		# set data_path
		if platform == 'android':
			self.data_path = '/storage/emulated/0/BraveHeart/data'
		else:
			self.data_path = 'data'

		#self.log_text += 'OK.'
		# define wait_fight
		self.wait_fight = False

		# 0: unfight, 1: win, 2: lost
		self.fight_status = 0

		# LOG
		self.log_list = []

		# check if renew item display
		self._backpack_add_item_required = False
		self.backpack_max_cap = 36

	def show_beadbox(self):
		self.add_widget(self.beadbox)

	def item_wear(self, index):
		print(f'[main.py]item_wear({index})')

		index_str = str(index).encode('utf8')
		App.get_running_app().client.send_message( \
			b'/item_swap', [index_str])
		
	def item_check_lock(self, index):
		print(f'[main.py]check_lock({index})')

		index_str = str(index).encode('utf8')
		App.get_running_app().client.send_message( \
			b'/item_check_lock', [index_str])

	def enforce_item(self, index):
		print(f'[main.py]enforce_item({index})')

		index_str = str(index).encode('utf8')

		self.ie = ItemEnforce(ww=1440, wh=2911, width=1225, backpack_idx=index)
		self.ie.ids.btn_exit_item_enforce.bind(on_release=self.exit_item_enforce)
		self.add_widget(self.ie)

		#App.get_running_app().client.send_message( \
		#	b'/item_swap', [index_str])

	def exit_item_enforce(self, instance):
		self.remove_widget(self.ie)

	def item_sell(self, index):
		print(f'[main.py] RootWidget.item_sell(index={index})')
		# send to service
		index_str = str(index).encode('utf8')
		App.get_running_app().client.send_message( \
			b'/item_sell', [index_str])

		self.bag.remove_item(index+1)

	def load_backpack(self):
		data = self.load_data()
		backpack_data = data['bag']
		self.bag.init_bag(backpack_data)

	def show_bag(self):
		#print('show_bag()')
		#data = self.load_data()
		#backpack_data = data['bag']
		self.remove_widget(self.bag)
		#self.bag.init_bag(backpack_data)
		self.add_widget(self.bag)

	def close_bag(self):
		print('close_bag()')
		if self.bag:
			self.remove_widget(self.bag)

	def generate_instance(self, instance):
		if self.home.ids.instance_level.text == '':
			level = self.lv_box.player_level
		else:
			level = int(self.home.ids.instance_level.text)
		self.home.random_generate(level=level)

	def instance_challenge(self, instance):
		if not self.home.selected:
			return

		if len(self.bag.occupied) >= 36:
			self.show_log(f'系统: [color=f16b07]请先清理背包哦, 不然无法进行重复挑战[/color]\n')
			return

		#print(self.home.zone_info.level)
		self.home.opacity = 0
		self.home.zone_info.hide_me()

		# check run once
		self.dungeon.run_once = self.home.zone_info.run_once
		print(self.dungeon.run_once)
		self.dungeon.start()

		self.dungeon.active_me()

		self.instance = 'instance'
		self.instance_level = self.home.zone_info.level

		where_list = {'instance': '副本', 'westfall': '无尽', \
						'trial': '试炼', 'starship': '星舰'}
		where_desc = where_list[self.instance]

		self.show_log(f'系统: [color=f16b07]你已进入{where_desc} (lv={self.instance_level})[/color]\n')
		self.service_instance_challenge()

	def player_load_data(self):
		self.player_data = self.load_data()

		# set lv_box
		self.lv_box.player_level = self.player_data['level']
		self.lv_box.samsara = self.player_data['samsara']
		self.lv_box.reincarnation = self.player_data['reincarnation']

		self.item_data = self.player_data['equipped']
		print("EQUIPPED: ", self.item_data)
		self.show_items()

		self.ie = item_effect.ItemEffect(self.item_data)
		self.make_effect()

	def init_player_data(self):
		init_data.check()

		self.player_load_data()

	def make_effect(self):
		#self.ie = item_effect.ItemEffect(self.item_data)
		self.ie.set_items(self.player_data['equipped'])
		effect = self.ie.calc_effect()
		print("ITEM EFFECT: ", effect)

		# set hp = bhp + hp from items
		self.max_hp = self.player_data['bhp'] + effect['hp']
		self.max_hp = int(self.max_hp * (1 + effect['hp_ratio'] / 100))
		self.current_hp = self.max_hp
		print(f'MAX_HP: {self.max_hp}, CUR_HP: {self.current_hp}')

		# set ap = bap + ap from items
		self.ap = self.player_data['bap'] + effect['ap']
		self.ap = int(self.ap * (1 + effect['ap_ratio'] / 100))
		print(f'ATTACK POWER: {self.ap}')

		# set critical chance and damage
		self.crit_chance = self.player_data['bcc'] + effect['cc']
		self.crit_damage = self.player_data['bcd'] + effect['cd']
		print(f'CRITICAL CHANCE: {self.crit_chance}%')
		print(f'CRITICAL DAMAGE: {self.crit_damage}%')

		# set armor value
		self.av = self.player_data['bav'] + effect['av']
		self.av_ratio = effect['av_ratio']
		self.av = int(self.av * (1 + self.av_ratio / 100))
		print(f'ARMOR VALUE: {self.av}')

		# set block value
		self.bv = self.player_data['bbv'] + effect['bv']
		print(f'BLOCK VALUE: {self.bv}')

		# set fdi
		self.fdi = self.player_data['fdi']

		# sync to service player
		#self.service_set_player()

		# calculate combat effectiveness
		# AP = 0.75 * ap * (1 + (cc / 100)) * (1 + (cd / 100))
		# HP = 0.12 * max_hp
		# AV = 1 * av + 1.1 * bv 
		W1, W2 = 1.5, 2.0
		self.ce = 0.12 * self.max_hp + \
			(1.2 * self.ap * (W1 + self.crit_chance / 100) * (W2 + self.crit_damage / 100)) + \
			(0.9 * self.av) + (1 * self.bv)
		self.ce = float(f'{self.ce:.2f}')
		print(f'COMBAT EFFECTIVENESS: {self.ce}')

		# set gold
		self.gold = self.player_data['gold']

	def exit_dungeon(self, instance):
		self._exit_dungeon(self)

	def _exit_dungeon(self):
		#print("removed dungeon")
		self.dungeon.hide_me()
		self.home.opacity = 1
		self.home.zone_info.hide_me()
		self.dungeon.actived = False

	def show_items(self):
		item_weapon_data = self.item_data['weapon']
		item_weapon = self.ids.eq_box.ids.weapon
		item_weapon.ltext = item_weapon_data['name']
		item_weapon.item_id = item_weapon_data['ID']
		item_weapon.item_image = f'icons/item/weapon/{item_weapon.item_id}.jpg'

		item_suit_data = self.item_data['suit']
		item_suit = self.ids.eq_box.ids.suit
		item_suit.ltext = item_suit_data['name']
		item_suit.item_id = item_suit_data['ID']
		item_suit.item_image = f'icons/item/suit/{item_suit.item_id}.jpg'

		item_necklace_data = self.item_data['necklace']
		item_necklace = self.ids.eq_box.ids.necklace
		item_necklace.ltext = item_necklace_data['name']
		item_necklace.item_id = item_necklace_data['ID']
		item_necklace.item_image = f'icons/item/necklace/{item_necklace.item_id}.jpg'

		item_ring_data = self.item_data['ring']
		item_ring = self.ids.eq_box.ids.ring
		item_ring.ltext = item_ring_data['name']
		item_ring.item_id = item_ring_data['ID']
		item_ring.item_image = f'icons/item/ring/{item_ring.item_id}.jpg'

	def load_data(self):
		data = {}

		file = 'data/profile.json'
		if platform == 'android':
			import os
			from android.storage import primary_external_storage_path
			file = os.path.join(primary_external_storage_path(),
				'BraveHeart/data/profile.json')

		print(f'loading file: {file}')
		with open(file, 'r') as f:
			data = json.load(f)
		return data

	def service_instance_challenge(self):

		instance_level = str(self.instance_level).encode('utf8')

		instance = str(self.instance).encode('utf8')

		max_hp = str(self.max_hp).encode('utf8')
		cur_hp = str(self.current_hp).encode('utf8')

		ap = str(self.ap).encode('utf8')
		av = str(self.av).encode('utf8')
		bv = str(self.bv).encode('utf8')
		fdi = str(self.fdi).encode('utf8')
		cc = str(self.crit_chance).encode('utf8')
		cd = str(self.crit_damage).encode('utf8')

		App.get_running_app().client.send_message(\
			b'/instance_challenge', [instance, instance_level, max_hp, \
				cur_hp, ap, av, bv, fdi, cc, cd])

	def item_lock_checked(self):
		self.bag.update_item_lock()

	def item_activate(self):
		self.player_load_data()

		# backpack to update item
		self.bag.update_item()
		#kind = self.bag.kind
		#id = self.bag.image_id
		#image = f'icons/item/{kind}/{id}.jpg'
		#print(f'[main.py] item_activate image={image}')
		#self.bag.grid_items[self.bag.index].item_image = image

	def earn_gold(self, gold):
		gold_decode = int(gold.decode('utf8'))
		self.gold += gold_decode
		self.show_log(f'系统: [color=00ff00]出售装备获得金币 {gold_decode}[/color]')

	def fight_report(self, win, gold, damage, where, instance_level, who, \
						bag_index, item_name):
		gold_decode = int(gold.decode('utf8'))
		self.gold += gold_decode

		damage= int(damage.decode('utf8'))
		self.current_hp -= damage
		if self.current_hp < 0:
			self.current_hp = 0

		where = where.decode('utf8')
		where_list = {'instance': '副本', 'westfall': '无尽', \
						'trial': '试炼', 'starship': '星舰'}
		where_desc = where_list[where]

		instance_level = int(instance_level.decode('utf8'))
		who = who.decode('utf8')

		self.show_log(f'系统: [color=ff0000]你遭遇了{who}(lv={instance_level}), 正在战斗中...[/color]\n')

		win = win.decode('utf8')
		if win == 'True':
			self.show_log(f'系统: [color=0000ff]击杀了{who}({where_desc}:{instance_level}), 受到{damage}点伤害[/color]\n')

			msg= f'系统: [color=00ff00]获得了: 金币 {gold_decode}[/color]'
			n_bag = int(bag_index.decode('utf8'))
			if n_bag == -1:

				msg += '\n'
			else:
				item_name = item_name.decode('utf8')

				msg += f' {item_name}\n'

				# update bag
				if self.bag:
					self._backpack_add_item_required = True
					self._backpack_add_item_index = n_bag
					#self.backpack_add_item(n_bag)
					#self.bag.backpack_add_item(n_bag)

			self.show_log(msg)
			self.fight_status = 1
		else:
			# player defeat
			self.show_log(f'系统: [color=0000ff]击杀了{who}({where_desc}:{instance_level}), 受到{damage}点伤害[/color]\n')

			self.fight_status = 2

	def backpack_add_item(self, index):
		self.bag.backpack_add_item(index)

	def check_obj(self):
		if self.fight_status == 0:
			return

		if self.fight_status == 1:
			self.dungeon.current_enemy_die()
		elif self.fight_status == 2:
			self.back_home()
		self.wait_fight = False

	def back_home(self):
		self.dungeon.reset_enemies()
		self.dungeon.hide_me()

	def get_item_from_bag(self, n):
		data = self.load_data()

	def service_fighting(self):
		# know index of enemies
		enemy_index = self.dungeon.current_enemy_index

		# send fighting to service
		index = str(enemy_index).encode('utf8')
		App.get_running_app().client.send_message(\
			b'/fighting', [index])

	def service_init_done(self):

		self.show_log('系统: [color=0000ff]游戏进度已经保存[/color]\n')
		self.show_log('系统: [color=0000ff]读取存档成功[/color]\n')
		self.show_log('[color=f16b07]欢迎你勇士, 点击地图上的副本开始战斗[/color]\n')
		self.show_log('[color=f16b07]系统地图右上角可以刷新当前副本[/color]\n')

	def append_log(self, msg):
		if len(self.log_list) >= 5:
			self.log_list.pop(0)
		self.log_list.append(msg)

	def show_log(self, msg):
		self.log_text = ''

		self.log_list.append(msg)
		if len(self.log_list) >= 15:
			self.log_list.pop(0)

		for line in self.log_list:
			self.log_text += line

	def update(self, dt):
		#self.gold += 1
		if (self.dungeon.actived):
			if len(self.bag.occupied) >= 36:
				self.show_log(f'系统: [color=f16b07]请先清理背包哦, 不然无法进行重复挑战[/color]\n')
				self._exit_dungeon()
				return

			if not self.wait_fight:
				self.dungeon.ids.hero.move()
				collision = self.dungeon.check_collision()
				if collision:
					#print('fight')
					self.wait_fight = True
					self.service_fighting()
			else:
				self.check_obj()
				self.fight_status = 0
		# display backpack item
		if self._backpack_add_item_required and len(self.bag.occupied) < self.backpack_max_cap:
			self.backpack_add_item(self._backpack_add_item_index)
			self._backpack_add_item_required = False

	def gold_test(self, gold):
		self.gold = int(gold.decode('utf8'))

class GameApp(App):
	ww, wh = Window.size

	def __init__(self, **kwargs):
		super().__init__(**kwargs)

	def check_service(self):
		if platform == 'android':
			self.start_service()
		elif platform in ('linux', 'win'):
			from runpy import run_path
			from threading import Thread
			self.service = Thread(
				target=run_path,
				args=['service.py'],
				kwargs={'run_name': '__main__'},
				daemon=True
			)
			self.service.start()
		else:
			raise NotImplementedError(
				"service start not implemented on this platform"
			)

	@staticmethod
	def start_service():
		from jnius import autoclass
		service = autoclass('org.kivy.brave_heart.ServiceBrave')
		mActivity = autoclass('org.kivy.android.PythonActivity').mActivity
		service.start(mActivity, "")
		return service

	def build(self):
		self.server = server = OSCThreadServer()
		server.listen(address=b'localhost', port=3102, default=True)
		self.client = OSCClient(b'localhost', 3100)

		root = RootWidget()
		self.check_service()
		# bind triggers
		server.bind(b'/fight_report', root.fight_report)
		server.bind(b'/gold_test', root.gold_test)
		server.bind(b'/item_activate', root.item_activate)
		server.bind(b'/item_lock_checked', root.item_lock_checked)
		server.bind(b'/earn_gold', root.earn_gold)

		#root.max_hp = 12334
		#root.current_hp = 123
		Clock.schedule_interval(root.update, 1/60.0)
		root.service_init_done()
		return root

if __name__ == '__main__':
	GameApp().run()
