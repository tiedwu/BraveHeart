__version__ = '0.1'

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout

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
	orientation: 'vertical'
	canvas.before:
		Color:
			rgba: utils.get_color_from_hex('#33322F7F')
		Rectangle:
			size: self.size
			pos: self.pos
	LVLabel:
		#font_size: 28
		color: (244/255, 252/255, 3/255, 1)
		text: ' '* 5 + 'LV ' + '196' + ' ' * 5
	BoxLayout:
		LVLabel:
			#font_size: 24
			text_size: self.size
			text: u' 轮回 1 次'
			halign: 'left'
			valign: 'bottom'
			color: (3/255, 252/255, 240/255, 1)
			#color: (3/255, 198/255, 252/255, 1)
		LVLabel:
			#font_size: 24
			text_size: self.size
			text: u'转生 3 次 '
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
			text: "45979/45979"
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
			text: "45808"
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
			text: "102%"
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
			text: "1124%"
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
			text: "4648\\n(94.85%) "
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
			text: "4128"
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

<EQWidget@BoxLayout>:
	#size: root.ww * 0.5, root.wh * 0.18 // 4
	size_hint: 1, None
	Image:
		canvas:
			Color:
				rgba: 1, 0, 0, 1
			Line:
				width: 2
				rectangle: self.x, self.y, self.width, self.height
		size_hint: None, None
		source: 'icons/sword.jpg'
		#size: 80, 80
		pos: 2, self.y

	Label:
		text: 'sword'

	Button:
		text: ''
		backgound_color: 0, 0, 0, 0
		Image:
			size_hint: None, None
			source: 'icons/upgrade.jpg'
			#size: 80, 80
			pos: self.x, self.y

<EQBox>:
	size: root.ww * 0.5, root.wh * 0.185
	#padding: 20
	canvas.before:
		Color:
			rgba: utils.get_color_from_hex('#33322F7F')
		Rectangle:
			size: self.size
			pos: self.pos
	BoxLayout:
		#size: root.ww * 0.5, root.wh * 0.185
		orientation: 'vertical'
		EQWidget:
		#Button:
			id: sword
		EQWidget:
		#Button:
			id: armor
		EQWidget:
		#Button
			id: necklace
		EQWidget:
		#Button:
			id: ring

<RootWidget>:
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
			rgba: utils.get_color_from_hex('#73B5D3')
		Rectangle:
			pos: 0, (root.wh // 15 + root.ww)
			size: root.ww, root.wh - root.wh // 15 - root.ww

	LVBox:
		x: 0
		y: 0.935 * root.wh
		size_hint: 0.5, 0.05

	GoldBox:
		x: 0.5 * root.ww + 5
		y: 0.95 * root.wh
		size_hint: 0.23, 0.03

	CEBox:
		x: 0.73 * root.ww + 10
		y: 0.95 * root.wh
		size_hint: 0.24, 0.03

	PFBox:
		x: 0
		y: 0.75 * root.wh
		size_hint: 0.5, 0.18 

	EQBox:
		x: 0
		y: 0.56 * root.wh
		size_hint: 0.5, 0.185

''')

#class EQWidget(Widget):
#	ww, wh = Window.size

class EQBox(BoxLayout):
	ww, wh = Window.size

class PFBox(BoxLayout):
	ww, wh = Window.size

class CEBox(BoxLayout):
	pass

class LVBox(BoxLayout):
	pass

class GoldBox(BoxLayout):
	pass

class SubWidget(Widget):
	ww, wh = Window.size
	mw, mh = 480, 480
	pass

class RootWidget(Screen):
	ww, wh = Window.size
	mw, mh = 480, 480
	pass

class TestApp(App):
	ww, wh = Window.size
	def build(self):
		return RootWidget()

if __name__ == '__main__':
	TestApp().run()
