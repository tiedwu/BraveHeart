from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

Builder.load_string('''
<CustWidget>:
	size: 400, 360//3
	ltext: ''
	Button:
		text: 'Hello'
		size_hint: None, None
		size: 100, 30
		pos_hint: {'center_y': 0.5}
	Image:
		size_hint: None, None
		#source: 'src/icons/sword.jpg'
		source: root.item_image
		size: 80, 80
		pos_hint: {'center_y': 0.5}
	Label:
		#text: 'Wordld!!!'
		text: root.ltext
	Image:
		size_hint: None, None
		source: 'src/icons/upgrade.jpg'
		size: 80, 80
		pos_hint: {'center_y': 0.5}

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
			id: cust1
		CustWidget:
		#Button:
			id: cust2
		CustWidget:
		#Button:
			id: cust3
''')

class CustWidget(BoxLayout):
	pass

class MyWidget(Screen):
	def __init__(self, **kwares):
		self.ids.cust1.ltext = 'sword'

class MyApp(App):
	def build(self):
		return MyWidget()

if __name__ == '__main__':
	MyApp().run()
