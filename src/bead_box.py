from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen
from kivy.graphics import Color, RoundedRectangle, Line

Builder.load_string('''
<Root>:

''')
class BeadWidget(Widget):
	def __init__(self, screen_width, screen_height, **kwargs):
		super().__init__(**kwargs)

		self.width = screen_width * 0.9
		self.height = screen_height * 0.65
		# endy = screen_height * 0.7
		widget_startx = (screen_width - self.width) / 2
		#starty = (screen_height - self.height) / 2
		widget_starty = screen_height * 0.2
		widget_endy = widget_starty + self.height
		self.pos = [widget_startx, widget_starty]

		# title field
		title_pad_x = 5
		title_width = self.width - title_pad_x * 2
		title_startx = widget_startx + title_pad_x
		title_height = 150
		title_pad_y = 5
		title_endy = widget_endy - title_pad_y
		title_starty = title_endy - title_height

		# background
		widget_pad_y = 5
		bg_startx =title_startx
		bg_starty = widget_starty + widget_pad_y
		bg_width = title_width
		bg_height = title_endy - bg_starty

	# widget rim
		transparent_width = 5

		with self.canvas.before:
			# background
			Color(43/255, 41/255, 46/255, 1)
			RoundedRectangle(pos=[bg_startx, bg_starty], size=[bg_width, bg_height])

			# title rim
			Color(119 / 255, 102 / 255, 74 / 255, 1)
			Line(rounded_rectangle=[title_startx, title_starty, \
									title_width, title_height, 18], width=2)

			# widget rim
			Color(43 / 255, 41 / 255, 46 / 255, 0.6)
			Line(rounded_rectangle=[widget_startx, widget_starty, \
									self.width, self.height, 18], width=transparent_width)




class Root(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		#ie = ItemEnforce(pos=(50, 250), size=(100, 200))
		bw = BeadWidget(screen_width=1440, screen_height=2911)
		self.add_widget(bw)

class MainApp(App):
	def build(self):
		from kivy.core.window import Window
		Window.size = [1440, 2911]
		#Window.size = [1400, 800]
		Window.clearcolor = 1, 1, 1, 1
		return Root()

if __name__ == '__main__':
	MainApp().run()
