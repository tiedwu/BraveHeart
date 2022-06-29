from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.core.window import Window

Window.size = [800, 1000]


Builder.load_string('''
<HomeLabel@Label>:
	font_name: 'fonts/DroidSansFallback.ttf'
	font_size: '20sp'

<HomeButton@ToggleButton>:
	group: 'homebtn_select'
	text: ''
	btn_size: 100
	size: [self.btn_size, self.btn_size]
	btn_image: 'icons/instance/trial.png'
	background_normal: self.btn_image
	background_down: self.btn_image

<HomeWidget>:
	btn_size: root.ww * 100 / 1400
	# trial
	HomeButton:
		btn_image: 'icons/instance/trial.png'
		pos: root.ww * 0.02, root.wh * 0.5
		btn_size: root.btn_size
	HomeButton:
		btn_image: 'icons/instance/challenge_westfall.png'
		pos: root.ww * 0.12, root.wh * 0.5
		btn_size: root.btn_size
	HomeButton:
		btn_image: 'icons/instance/challenge_starship.png'
		pos: root.ww * 0.22, root.wh * 0.5
		btn_size: root.btn_size
	# manor
	HomeButton:
		btn_image: 'icons/main/manor.png'
		pos: root.ww * 0.32, root.wh * 0.5
		btn_size: root.btn_size

	HomeLabel:
		text: 'say somethings...: '
		pos: root.ww * 0.4, root.wh * 0.5
		size: [self.texture_size[0], root.btn_size]

	TextInput:
		text_hint: ''
		pos: root.ww * 0.65, root.wh * 0.5
		size: [100, root.btn_size]
<Root>:
	HomeWidget:

''')

class HomeWidget(Widget):
	ww, wh = Window.size[0], Window.size[1]
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

class Root(Screen):
	pass

class AwesomeApp(App):
	def build(self):
		Window.clearcolor = [0.8, 0.7, 0.6, 1]
		root = Root()
		return root

if __name__ == '__main__':
	AwesomeApp().run()
