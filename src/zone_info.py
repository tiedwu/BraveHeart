from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.properties import ListProperty, ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.widget import Widget

Builder.load_string('''

<InfoLabel@Label>:
	font_size: '13sp'
	font_name: 'fonts/DroidSansFallback.ttf'
	size_hint: None, None
	size: self.texture_size
	halign: 'left'
	valign: 'middle'

<InfoButton@Button>:
	font_name: 'fonts/DroidSansFallback.ttf'

<ZoneInfo>:
	btn_exit: btn_exit
	btn_challenge: btn_challenge
	size_hint: None, None
	size: root.ww * 0.6, root.wh * 0.3
	pos: [root.ww * 0.2, root.wh * 0.15]

	level: 0

	canvas.before:
		Color:
			rgba: 59/255, 56/255, 53/255, 1
		Rectangle:
			pos: self.pos
			size: self.size

	InfoButton:
		id: btn_exit
		canvas:
			Color:
				rgba: 250/255, 148/255, 5/255, 1
			Line:
				width: 1
				rectangle: (self.x, self.y, self.width, self.height)
		size_hint: None, None
		text: 'X'
		color: 250/255, 148/255, 5/255, 1
		background_normal: ''
		background_color: 1, 1, 1, 0
		pos_hint: {'right': 0.95, 'center_y': 0.9}
		width: root.width * 0.05
		height: root.width * 0.05
		on_press: root.hide_me()
		#on_press: root.close()

	InfoLabel:
		text: f'当前副本: lv{root.level}_普通'
		pos_hint: {'x': 0.05, 'y': 0.8}
	InfoLabel:
		text: '推荐战力: 17.87'
		pos_hint: {'x': 0.05, 'y': 0.6}
	InfoLabel:
		text: f'副本等级: {root.level}'
		pos_hint: {'x': 0.6, 'y': 0.6}
	InfoLabel:
		text: '当前副本难度等级: 普通'
		pos_hint: {'x': 0.05, 'y': 0.5}
	InfoLabel:
		size_hint: None, None
		text: '-副本难度等级分为: 普通, 困难, 极难\\n-难度越高装备爆率也会相应提升\\n-困难， 极难仅能挑战一次'
		pos_hint: {'x': 0.05, 'y': 0.3}
		size: self.texture_size
		halign: 'left'
		valign: 'middle'
	CheckBox:
		canvas.before:
			Color:
				rgba: 1, 1, 1, 1
			Rectangle:
				pos: self.pos
				size: self.size
		size_hint: None, None
		#size: root.ckb_size
		width: root.width * 0.05
		height: root.height * 0.05
		#pos: root.ckb_pos
		pos: [root.x + root.width * 0.05, root.y + root.height * 0.1]
		on_active: root.repeat(self, self.active)
		#background_checkbox_normal: 'images/uncheck.png'
		#background_checkbox_down: 'images/checked.png'

	InfoLabel:
		text: '重复挑战'
		pos_hint: {'x': 0.13, 'center_y': 0.125}

	InfoButton:
		id: btn_challenge
		canvas.before:
			Color:
				rgba: 1, 1, 1, 1
			Rectangle:
				size: self.size
				pos:self.pos
		size_hint: 0.4, 0.15 
		pos_hint: {'right': 0.95, 'center_y': 0.125}
		text: '开始挑战'
		background_color: 230/255, 220/255, 209/255, 1
		#on_press: print(root.height, root.width)

<Root>:
	ZoneInfo:

''')

class ZoneInfo(FloatLayout):

	btn_exit = ObjectProperty(None)
	btn_challenge = ObjectProperty(None)
	ww, wh = Window.size[0], Window.size[1]
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.run_once = True

	def on_size(self, *args):
		print(self.size)
		print(self.pos)

	def hide_me(self):
		self.opacity = 0
		#self.disabled = True
		#print(self.exit_btn)
		#self.exit_btn.disabled = True
		self.btn_challenge.disabled = True

	def active_me(self):
		self.opacity = 1
		self.disabled = False
		self.btn_challenge.disabled = False

	def repeat(self, instance, value):
		print(value)
		self.run_once = not value

class Root(Screen):
	pass

class AwesomeApp(App):
	def build(self):
		return Root()

if __name__ == '__main__':
	Window.clearcolor = 1, 1, 1, 1
	Window.size = [800, 1000]
	AwesomeApp().run()
