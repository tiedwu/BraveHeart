from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
import json

Builder.load_string('''

<CustLabel@Label>:
	font_name: 'src/fonts/DroidSansFallback.ttf'

<CustWidget>:
	size: 400, 360//4
	ltext: ''
	item_image: ''
	item_id: '000'
	#Button:
		#text: 'Hello'
		#size_hint: None, None
		#size: 100, 30
		#pos_hint: {'center_y': 0.5}
	Image:
		size_hint: None, None
		#source: 'src/icons/sword.jpg'
		source: root.item_image
		size: 80, 80
		pos_hint: {'center_y': 0.5}
	CustLabel:
		#text: 'Wordld!!!'
		text: root.ltext

	Button:
		size_hint: 0.6, 0.9
		text: ''
		background_color: 0, 0, 0, 0
		on_press: root.hello_on(root.item_id)
		on_release: root.hello_off(root.item_id)
		Image:
			size_hint: None, None
			source: 'src/icons/upgrade.jpg'
			size: 80, 80
			center_x: self.parent.center_x
			center_y: self.parent.center_y

<MyWidget>:
	#width: 800
	#height: 600
	size: 800, 600
	BoxLayout
		orientation: 'vertical'
		size_hint: 0.5, 0.6
		pos: 200, 200
		CustWidget:
		#Button:
			id: weapon
		CustWidget:
		#Button:
			id: suit
		CustWidget:
		#Button:
			id: necklace
		CustWidget:
			id: ring
''')

class CustWidget(BoxLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

	def hello_on(self, item):
		print("on: ", item)

	def hello_off(self, item):
		print("off: ", item)

class MyWidget(Screen):

	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.item_data = self.load_data()['equipped']
		print(self.item_data)

		print(self.ids)

		self.ids.weapon.ltext = self.item_data['weapon']['name']
		self.ids.weapon.item_image = 'src/icons/sword.jpg'
		self.ids.weapon.item_id = self.item_data['weapon']['ID']

		self.ids.suit.ltext = self.item_data['suit']['name']
		self.ids.suit.item_image = 'src/icons/suit.jpg'
		self.ids.suit.item_id = self.item_data['suit']['ID']

		self.ids.necklace.ltext = self.item_data['necklace']['name'] 
		self.ids.necklace.item_image = 'src/icons/necklace.png'
		self.ids.necklace.item_id = self.item_data['necklace']['ID']

		self.ids.ring.ltext = self.item_data['ring']['name']
		self.ids.ring.item_image = 'src/icons/ring.jfif'
		self.ids.ring.item_id = self.item_data['ring']['ID']

	def load_data(self):
		data = {}

		file = 'src/data/profile.json'
		with open(file, "r") as f:
			data = json.load(f)
		return data

#class MyWidget(Screen):
	#def __init__(self, **kwargs):
	#	super().__init__(**kwargs)
#	pass

class MyApp(App):
	def build(self):
		return MyWidget()

if __name__ == '__main__':
	MyApp().run()
