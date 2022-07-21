from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.button import Button

import zone_info
#import dungeon
#import zone_info2

import random

Window.size = [1440, 2911]


def get_distance(p, q):
	s_sq_difference = 0
	for p_i, q_i in zip(p, q):
		s_sq_difference += (p_i - q_i) ** 2

	distance = s_sq_difference ** 0.5
	return distance

Builder.load_string('''
<ZoneWidget>:
	size_hint: None, None
	pos: self.pos
	size: self.size
	label_text: ''
	level: 1
	img_path: 'icons/main/flag_yellow.png'
	Button:
		canvas.before:
			Color:
				rgba: 1, 0, 0, 1
			Line:
				width: 2
				rectangle: self.x, self.y, self.width, self.height
		text: ''
		size_hint: None, None
		size: self.parent.size
		pos: self.parent.pos
		on_press: root.show_instance_info()
		BoxLayout:
			orientation: 'vertical'
			pos: self.parent.pos
			size: self.parent.size
			Image:
				source: root.img_path
			Label:
				text: str(root.level)

<HomeLabel@Label>:
	font_name: 'fonts/DroidSansFallback.ttf'
	font_size: '12sp'

<HomeButton@ToggleButton>:
	group: 'homebtn_select'
	text: ''
	btn_size: 100
	size: [self.btn_size, self.btn_size]
	btn_image: 'icons/instance/trial.png'
	background_normal: self.btn_image
	background_down: self.btn_image

<HomeWidget>:
	# trial
	HomeButton:
		btn_image: 'icons/instance/trial.png'
		pos: root.ww * 0.02, root.wh * 0.5
		btn_size: root.btn_size
	HomeButton:
		btn_image: 'icons/instance/challenge_westfall.png'
		pos: root.ww * 0.12, root.wh * 0.5
		btn_size: root.btn_size
	HomeButton:
		btn_image: 'icons/instance/challenge_starship.png'
		pos: root.ww * 0.22, root.wh * 0.5
		btn_size: root.btn_size
	# manor
	HomeButton:
		btn_image: 'icons/main/manor.png'
		pos: root.ww * 0.32, root.wh * 0.5
		btn_size: root.btn_size

	HomeLabel:
		text: '副本等级(点击可输入): '
		pos: root.ww * 0.4, root.wh * 0.5
		size: [self.texture_size[0], root.btn_size]

	TextInput:
		id: instance_level
		text_hint: ''
		pos: root.ww * 0.7, root.wh * 0.505
		size: [150, 80]

	HomeButton:
		id: gen_instance
		btn_image: 'icons/main/random_generate.png'
		pos: root.ww * 0.82, root.wh * 0.5
		btn_size: root.btn_size
		#on_release: root.random_generate()

	HomeButton:
		btn_image: 'icons/main/fight.png'
		pos: root.ww * 0.9, root.wh * 0.5
		btn_size: root.btn_size

<Root>:
	HomeWidget:

''')

class ZoneWidget(Widget):
	#label_text = ''
	def __init__(self, level, **kwargs):
		super(ZoneWidget, self).__init__(**kwargs)
		self.level = level
		#print(self.level_text)

	def show_instance_info(self):
		print(self.level, self.parent.parent)
		self.parent.parent.show_instance_info(self.level)

class HomeWidget(Widget):
	ww, wh = Window.size[0], Window.size[1]
	btn_size = int(ww * 100 / 1440)
	rtop = int(wh * 0.5 - btn_size)
	#rtop = int(wh * 0.5 - 2 * btn_size)
	rbottom = int(wh * 0.2)
	rleft = int(ww * 0.15)
	rright = int(ww * 0.85)
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.zone_widget = Widget()
		self.add_widget(self.zone_widget)

		# setup zone info widget
		self.zone_info = zone_info.ZoneInfo()
		self.zone_info.disable = True
		self.zone_info.opacity = 0
		self.add_widget(self.zone_info)

		# setup dungeon
		#self.dungeon = dungeon.Dungeon()
		#self.dungeon.disable = True
		#self.dungeon.opacity = 0
		#self.add_widget(self.dungeon)
		#self.dungeon.

	def show_instance_info(self, lv):
		print('Hello', lv)
		self.zone_info.level = lv
		self.zone_info.opacity = 1
		self.zone_info.disable = False

	def create_zone(self, coordinates, r, lv):
		n = lv
		for x, y in coordinates:
			zone = ZoneWidget(pos=(x - r, y - r), size=(r, r), level=n)
			n += 1
			self.zone_widget.add_widget(zone)

	def random_generate(self, level=1):

		#if self.ids.instance_level.text == '':
			#print(self.parent)
			#level = self.parent.lv_box.player_level
		#else:
			#level = int(self.ids.instance_level.text)

		if self.zone_widget:
			print('removed!')
			self.zone_widget.clear_widgets()

		count = 12
		diff = 20
		print('random_generate, btn_size: ', self.btn_size)
		coordinates = []
		while len(coordinates) < count:
			x = random.choice(range(self.rleft, self.rright))
			y = random.choice(range(self.rbottom, self.rtop))
			p = (x, y)
			collision = False
			if len(coordinates) > 0:
				for coord in coordinates:
					if get_distance(coord, p) < self.btn_size * 1.44 + diff:
						collision = True
						break
			if not collision:
				coordinates.append(p) 
		print(coordinates)

		self.create_zone(coordinates, self.btn_size, level)

class Root(Screen):
	pass

class AwesomeApp(App):
	def build(self):
		Window.clearcolor = [0.8, 0.7, 0.6, 1]
		root = Root()
		return root

if __name__ == '__main__':
	AwesomeApp().run()

