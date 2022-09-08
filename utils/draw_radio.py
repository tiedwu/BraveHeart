from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.uix.stencilview import StencilView
from kivy.graphics import *

Builder.load_string('''

<Root>:
	canvas.before:
		Color:
			rgba: 1, 0, 0, 0.7
		Rectangle:
			pos: 400, 400
			size: 180, 180

		Ellipse:
			angle_start: 100
			angle_end: 400
			pos: 250, 250
			size: 130, 130

		# triangle
		Ellipse:
			segments: 3
			pos:210, 110
			size: 140, 140

		Triangle:
			points: 310, 110, 340, 190, 180, 130

		Triangle:
			points: 400, 100, 485, 100, 485, 15

		# rectangle:
		Color:
			rgba: 1, 1, 1, 0.6
		Line:
			width: 2
			rounded_rectangle: (451, 52, 27, 23, 2)
		Line:
			width: 2
			ellipse: (462, 61, 6, 8)
		Line:
			width: 1
			points: (465, 61, 465, 58)
		Line:
			width: 2
			ellipse: (454, 69, 20, 20, 90, -90)


		Color:
			rgba: 1, 1, 1, 0
		Rectangle:
			pos: 100, 100
			size: 48, 48
		Color:
			rgba: 1, 1, 1, 1
		Ellipse:
			pos: 100, 100
			size: 48, 48
		Color:
			rgba: 0, 0, 1, 1
		Ellipse:
			pos: 106, 106
			size: 36, 36

''')

class Radio(Widget):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		with self.canvas.before:
			Color(1, 1, 1, 0)
			Rectangle(pos=(100, 100), size=(48, 48))
			Color(1, 1, 1, 1)
			Ellipse(pos=(100, 100), size=(48, 48))
			#Color(0, 0, 1, 1)
			#Ellipse(pos=(106, 106),size=(36, 36))


class Root(Widget):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		#self.pos = 100, 100
		#self.size = 48, 48

class MainApp(App):
	def build(self):
		self.root = Root()
		Clock.schedule_once(self.export, 1)
		return self.root

	def export(self, dt):
		#self.root.export_to_png('test.png')
		stencil = StencilView(pos=(100, 100), size=(48, 48))
		w = Radio()
		stencil.add_widget(w)
		#image = self.root.export_as_image()
		image = stencil.export_as_image()
		#image = w.export_as_image()
		image.save('test.jpg')

if __name__ == '__main__':
	MainApp().run()
