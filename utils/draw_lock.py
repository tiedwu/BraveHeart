from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget


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


''')

class Root(Widget):
	pass

class MainApp(App):
	def build(self):
		return Root()

if __name__ == '__main__':
	MainApp().run()
