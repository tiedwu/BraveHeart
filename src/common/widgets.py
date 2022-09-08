from kivy.uix.label import Label
from kivy.uix.behaviors import ButtonBehavior, ToggleButtonBehavior
from kivy.uix.image import Image
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.button import Button
from kivy.graphics import Color, RoundedRectangle, Line, Rectangle, Callback
from kivy.properties import ListProperty, NumericProperty, BooleanProperty
from kivy.graphics.instructions import Canvas

class ImageButton(ButtonBehavior, Image):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

class CFontLabel(Label):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.font_name = self.font_name = 'fonts/DroidSansFallback.ttf'

class AL_Label(CFontLabel):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		if 'halign' in list(kwargs.keys()):
			self.halign = kwargs["halign"]
		self.size_hint = None, None
		self.text_size = self.size
		#self.halign = "left"
		self.valign = "middle"
		self.font_size = '10sp'

# gray color label
class GC_Label(CFontLabel):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		#self.center_x = kwargs["center_x"]
		#self.center_y = kwargs["center_y"]
		self.color = [153 / 255, 153 / 255, 153 / 255, 1]

		with self.canvas.before:
			Color(0, 0, 0.2)
			Rectangle(pos=self.pos, size=self.size)

		print(f'[widgets.py] GC_Label.__init__(center={self.center})')

class SlotToggleButton(ToggleButton):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.background_color = 21/255, 31/255, 20/255, 1
		self.background_normal = ""
		self.background_down = ""

class BH_Button(Button):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.font_name = 'fonts/DroidSansFallback.ttf'
		self.background_normal = ''
		self.background_down = ''
		self.background_color = (0, 0, 0, 0)
		self.font_size = '11sp'

		with self.canvas.before:
			Color(119 / 255, 102 / 255, 74 / 255, 1)
			RoundedRectangle(pos=self.pos, size=self.size)

		with self.canvas.after:
			Color(1, 1, 1, 1)
			Line(rounded_rectangle=[self.pos[0], self.pos[1], self.size[0], self.size[1], 18], width=2)

if __name__ == '__main__':
	from kivy.app import App
	from kivy.uix.widget import Widget
	class MainApp(App):
		def build(self):
			return Widget()
	MainApp().run()
	print("Hello")
	state = "normal"
	d = {'normal': (1, 0, 1, 1), 'down': (1, 1, 0, 1)}[state]
	print(d)