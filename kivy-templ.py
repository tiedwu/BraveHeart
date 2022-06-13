from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

Builder.load_string('''

<CustomWidget>:
	size: root.size
	size_hint: 1, None
	ltext: '111'
	#img_src: ''
	#pos: root.x + 20, root.top - self.height - 20
	Image:
		canvas:
			Color:
				rgba: 255/255, 0/255, 0, 1
			Line:
				width: 2
				rectangle: self.x, self.y, self.width, self.height 
		size_hint: None, None
		source: 'sword.jpg'
		size: 80, 80
		pos: 2, self.y

	Label:
		size_hint: .7, .5
		text: root.ltext

	Button:
		size_hint: .3,.25
		text: ''
		color: .7, .6, .4, 1
		pos_hint: {'y': .5}
		background_color: 0, 0, 0, 0
		Image:
			source: 'upgrade.jpg'
			center_x: self.parent.center_x
			center_y: self.parent.center_y
			size: 80, 80

<RootWidget>:
	size: root.size
	CustomWidget:
		id: cust1
		pos: 0, 0
	CustomWidget:
		id: cust2
		pos: 0, 1/3 * root.height
	CustomWidget:
		id: cust3
		pos: 0, 2/3 * root.height
''')

class CustomWidget(BoxLayout):
	def __init__(self, **kwargs):
		super(CustomWidget, self).__init__(**kwargs)
		#print(self.pos)
		self.size = Window.width, Window.height/3
		print(self.size)
		#self.ltext =  StringProperty()

	def set_ltext(self, text):
		self.ltext = text

class RootWidget(Widget):
	def __init__(self, **kwargs):
		super(RootWidget, self).__init__(**kwargs)
		#print(self.pos)
		self.size = Window.width, Window.height
		print(self.size)

		#self.ids.cust1.set_ltext('CUST1')
		self.ids.cust1.ltext = 'sword'
		self.ids.cust2.ltext = 'armor'
		self.ids.cust3.ltext = 'necklace'

class TemplApp(App):
	def build(self):
		return RootWidget()

if __name__ == '__main__':
	TemplApp().run()
