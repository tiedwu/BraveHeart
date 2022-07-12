__version__ = '0.2'

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import platform
from kivy.properties import ObjectProperty, NumericProperty
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
		text: "68.61亿" + "  "
		text_size: self.size
		halign: 'right'
		valign: 'middle'

<CEBox>:
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
		text: "227636.06" + " "

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
		#pos: [0, 0.5 * root.height]
		#size: [0.5 * root.width, 0.5 * root.height]
		window_width: 1440

		# hp full: 100%
		hp_remain: 100
		canvas:
			#Color:
			#	rgba: 0, 0, 0, 1
			#Rectangle:
			#	pos: 0, 0
			#	size: self.size

			# draw hp bar
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
			#size: [top_left.window_width/(top_left.window_width/80),\
			#	top_left.window_width/(top_left.window_width/80)]

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
			#size: [top_left.window_width/(top_left.window_width/80),\
			#	top_left.window_width/(top_left.window_width/80)]

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
	#weapon: weapon
	#suit: suit
	#necklace: necklace
	#ring: ring
	#size: root.ww * 0.5, root.wh * 0.185
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
	orientation: 'vertical'
	canvas.before:
		Color:
			rgba: 240/255, 166/255, 29/255, 0.2
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
			text: '系统: 获得了: 金币 [color=00ff00]7154[/color]'
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
		#orientation: 'tb-lr'
		pos: self.parent.pos
		size: self.parent.size
		Image:
			source: root.btn_image
			size_hint_y: 0.7
			#width: 100
			#height: 100
			#size: 115, 122
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
		#center_y: self.parent.center_y
		#background_color: 0, 0, 0, 1
	MenuButton:
		btn_text: '精气珠'
		btn_image: 'icons/menu/mbead.png'
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
		#pos_hint: {'x': 0, 'center_y': 0.025}
		#size_hint: 1, root.wh - root.wh // 15 - root.ww
		#x: 0
		#y: 10
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
	#ww, wh = Window.size
	#weapon = ObjectProperty(None)
	#suit = ObjectProperty(None)
	#necklace = ObjectProperty(None)
	#ring = ObjectProperty(None)

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
		print("LVBox: ", self.ids)

class GoldBox(BoxLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		print("GoldBox: ", self.ids)

class RootWidget(Screen):
	ww, wh = Window.size
	mw, mh = 480, 480

	# define
	max_hp = NumericProperty(0)
	current_hp = NumericProperty(0)
	ap = NumericProperty(0)
	crit_chance = NumericProperty(0)
	crit_damage = NumericProperty(0)
	av = NumericProperty(0)
	av_ratio = NumericProperty(0)
	bv = NumericProperty(0)
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		#print("RootWidget: ", self.ids.eq_box.ids)

		# init attributes
		self.max_hp = 0
		self.current_hp = 0
		self.ap = 0
		self.crit_chance = 0
		self.crit_damage = 0
		self.av = 0
		self.bv = 0

		self.av_ratio = 0

		self.init_player_data()

		# add dungeon for test
		self.dungeon = Dungeon()
		self.dungeon.ids.dungeon_exit.bind(on_press=self.exit_dungeon)

		# set hide and disabed
		self.dungeon.opacity = 0
		self.dungeon.disabled = True

		self.add_widget(self.dungeon)

		self.home = HomeWidget()
		self.add_widget(self.home)

	def init_player_data(self):
		init_data.check()

		self.player_data = self.load_data()

		# set lv_box
		self.lv_box.player_level = self.player_data['level']
		self.lv_box.samsara = self.player_data['samsara']
		self.lv_box.reincarnation = self.player_data['reincarnation']

		self.item_data = self.player_data['equipped']
		print("EQUIPPED: ", self.item_data)
		self.init_items()

		self.ie = item_effect.ItemEffect(self.item_data)
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

	def exit_dungeon(self, instance):
		self.remove_widget(self.dungeon)

	def init_items(self):

		#init_data.check()

		#self.item_data = self.load_data()['equipped']
		#print(self.item_data)

		item_weapon_data = self.item_data['weapon']
		item_weapon = self.ids.eq_box.ids.weapon
		item_weapon.ltext = item_weapon_data['name']
		item_weapon.item_id = item_weapon_data['ID']
		item_weapon.item_image = 'icons/weapon.jpg'

		item_suit_data = self.item_data['suit']
		item_suit = self.ids.eq_box.ids.suit
		item_suit.ltext = item_suit_data['name']
		item_suit.item_id = item_suit_data['ID']
		item_suit.item_image = 'icons/suit.jpg'

		item_necklace_data = self.item_data['necklace']
		item_necklace = self.ids.eq_box.ids.necklace
		item_necklace.ltext = item_necklace_data['name']
		item_necklace.item_id = item_necklace_data['ID']
		item_necklace.item_image = 'icons/necklace.png'

		item_ring_data = self.item_data['ring']
		item_ring = self.ids.eq_box.ids.ring
		item_ring.ltext = item_ring_data['name']
		item_ring.item_id = item_ring_data['ID']
		item_ring.item_image = 'icons/ring.jfif'

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

	def update(self, dt):
		self.dungeon.ids.hero.move()
		self.dungeon.check_collision()

class GameApp(App):
	ww, wh = Window.size

	def __init__(self, **kwargs):
		super().__init__(**kwargs)

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
		#root.max_hp = 12334
		#root.current_hp = 123
		Clock.schedule_interval(root.update, 1.0/60.0)
		return root

if __name__ == '__main__':
	GameApp().run()
