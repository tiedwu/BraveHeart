from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder


Builder.load_string('''
<Main>:
	width: root.width
	height: root.height
	canvas:
		Color:
			rgba: 1, 1, 1, 1
		Rectangle:
			size: self.size
			pos: self.pos

	# top-left black region
	RelativeLayout:
		id: top_left
		size_hint: None, None
		pos: [0, 0.5 * root.height]
		size: [0.5 * root.width, 0.5 * root.height]

		# hp full: 100%
		hp_remain: 100
		canvas:
			Color:
				rgba: 0, 0, 0, 1
			Rectangle:
				pos: 0, 0
				size: self.size

			# draw hp bar
			Color:
				rgba: 1, 1, 1, 1
			Rectangle:
				#id: hpbar
				pos: self.size[0] * 0.2, self.size[1] * 0.8
				size: self.size[0] * 0.5, 5
			Color:
				rgba: 0, 1, 0, 1
			Rectangle:
				pos: self.size[0] * 0.2, self.size[1] * 0.8
				size: self.size[0] * 0.5 * (self.hp_remain / 100), 5

		Label:
			id: show_hp
			size_hint: None, None
			pos_hint: {'x': 0.1, 'y': 0.6}
			text: "HP: 100%"

		Button:
			size_hint: None, None
			#pos:top_left.size[0] * 0.5, top_left.size[1] * 0.5
			pos_hint: {'center_x': 0.5, 'center_y': 0.5}
			size: [100, 30]
			text: "Fight"
			on_press: root.press_me()

		# slider
		Slider:
			orientaton: 'horizontal'
			size_hint: None, None
			pos_hint: {'x': 0.1, 'y': 0.2}
			value: 100
			min: 0
			max: 100
			step: 1

			width: top_left.size[0]* 0.8
			on_value: root.control_me(*args)

		Button:
			size_hint: None, None
			size: [100, 30]
			pos_hint: {'x': 0.1, 'y':0.1}
			text: 'B2'

	# bottom-left blue region
	RelativeLayout:
		size_hint: None, None
		pos: [0, 0]
		size: [0.5 * root.width, 0.5 * root.height]
		canvas:
			Color:
				rgba: 0, 0, 1, 1
			Rectangle:
				pos: 0, 0
				size: self.size

	# top-right green region
	RelativeLayout:
		size_hint: None, None
		pos: [0.5 * root.width, 0.5 * root.height]
		size: [0.5 * root.width, 0.5 * root.height]
		canvas:
			Color:
				rgba: 0, 1, 0, 1
			Rectangle:
				pos: 0, 0
				size: self.size

	# bottom-right yellow region
	RelativeLayout:
		size_hint: None, None
		pos: [0.5 * root.width, 0]
		size: [0.5 * root.width, 0.5 * root.height]
		canvas:
			Color:
				rgba: 1, 1, 0, 1
			Rectangle:
				pos: 0, 0
				size: self.size

		Button:
			size_hint: None, None
			#pos:top_left.size[0] * 0.5, top_left.size[1] * 0.5
			pos_hint: {'center_x': 0.5, 'center_y': 0.5}
			size: [100, 30]
			text: "B3"
		Button:
			size_hint: None, None
			size: [100, 30]
			pos_hint: {'x': 0.1, 'y':0.1}
			text: 'B4'
''')

class Main(Widget):
	def press_me(self):
		remain = self.ids.top_left.hp_remain
		remain -= 25
		if remain == 0:
			remain = 100
		self.ids.top_left.hp_remain = remain
		self.ids.show_hp.text = f'HP: {remain}%' 

	def control_me(self, *args):
		#print(*args)
		value = args[1]
		self.ids.top_left.hp_remain = int(value) 
		self.ids.show_hp.text = f'HP: {value}%' 

class MyApp(App):
	def build(self):
		return Main()

if __name__ == '__main__':
	MyApp().run()
