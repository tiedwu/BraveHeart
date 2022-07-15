from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.properties import ListProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout

Builder.load_string('''

<InfoLabel@Label>:
	font_name: 'fonts/DroidSansFallback.ttf'
	size_hint: None, None
	size: self.texture_size
	halign: 'left'
	valign: 'middle'

<InfoButton@Button>:
	font_name: 'fonts/DroidSansFallback.ttf'

<ZoneInfo>:
	#orientation: 'vertical'
	#size_hint: None, None
	#size: self.size
	#size_hint: 0.8, 0.4
	size_hint: 0.3, 0.2
	#exit_btn_size: self.exit_btn_size
	pos_hint: {'center_x': 0.5, 'center_y': 0.3}
	#exit_btn_size: [96, 96]

	canvas.before:
		Color:
			#rgba: 92/255, 90/255, 84/255, 1
			#rgba: 1, 0, 0, 1
			rgba: 59/255, 56/255, 53/255, 1
		Rectangle:
			pos: self.pos
			size: self.size

	InfoButton:
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
		size: root.exit_btn_size

	InfoLabel:
		#size_hint: None, None
		text: '当前副本: lv2_普通'
		pos_hint: {'x': 0.05, 'y': 0.8}
	InfoLabel:
		#size_hint: None, None
		text: '推荐战力: 17.87'
		pos_hint: {'x': 0.05, 'y': 0.6}
	InfoLabel:
		#size_hint: None, None
		text: '副本等级: 2'
		pos_hint: {'x': 0.6, 'y': 0.6}
	InfoLabel:
		#size_hint: None, None
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
			#pos: self.ww * 0.1, self.wh * 0.1
			#pos: self.ww * 0.4, self.wh * 0.3
				#pos: self.sw * 0.2 + self.ww * 0.1, self.sh * 0.15 + self.wh * 0.1
				#size: root.ckb_size
				pos: self.pos
				size: self.size
		size_hint: None, None
		size: self.parent.ckb_size
		pos: self.parent.ckb_pos
		#pos: self.sw * 0.2 + self.ww * 0.1, self.sh * 0.15 + self.wh * 0.1

		background_checkbox_normal: 'images/uncheck.png'
		background_checkbox_down: 'images/checked.png'

	InfoLabel:
		#size_hint: None, None
		text: '重复挑战'
		pos_hint: {'x': 0.13, 'center_y': 0.125}

	InfoButton:
		canvas.before:
			Color:
				rgba: 1, 1, 1, 1
			Rectangle:
				size: self.size
				pos:self.pos
		#size_hint: None, None
		size_hint: 0.4, 0.15 
		#size: [self.parent.size[0] * 0.4, size.parent.size[1] *  0.15]
		#size: self.parent.start_btn_size
		pos_hint: {'right': 0.95, 'center_y': 0.125}
		text: '开始挑战'
		background_color: 230/255, 220/255, 209/255, 1

<Root>:
	ZoneInfo:

''')

class ZoneInfo(FloatLayout):
#class ZoneInfo(RelativeLayout):
	sw, sh = Window.size[0], Window.size[1]
	ww, wh = Window.size[0] * 0.6, Window.size[1] * 0.7
	#ckb_size = ListProperty()
	exit_btn_size = [ww * 0.05, ww * 0.05]
	ckb_size = [ww * 0.05, ww * 0.05]
	ckb_pos_x = sw * 0.2 + ww * 0.05
	ckb_pos_y = sh * 0.15 + wh * 0.1
	ckb_pos = [ckb_pos_x, ckb_pos_y]
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.size = [self.ww, self.wh]
		#self.exit_btn_size = [self.ww * 0.05, self.ww * 0.05]
		#self.ckb_size = [self.ww * 0.05, self.ww * 0.05]
		#self.ckb_pos = [self.sw * 0.2 + self.ww * 0.05, 
		#	self.sh * 0.15 + self.wh * 0.1]
		#self.start_btn_size = [self.ww * 0.4, self.wh * 0.15]
		print(self.exit_btn_size)

	def on_size(self, *args):
		print(self.size)
		print(self.pos)

class Root(Screen):
	pass

class AwesomeApp(App):
	def build(self):
		return Root()

if __name__ == '__main__':
	Window.clearcolor = 1, 1, 1, 1
	Window.size = [800, 1000]
	AwesomeApp().run()
