from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.uix.widget import Widget

Window.clearcolor = [1, 1, 1, 1]
Window.size = [800, 1000]

Builder.load_string('''
#:set ms 83
#:set bs 83
#:set ps 83
<Mob>:
	Image:
		source: 'gif/mob.gif'
		pos: root.pos
		size: ms, ms

<Boss>:
	Image:
		source: 'gif/boss.gif'
		pos: root.pos
		size: bs, bs

<Hero>:
	Image:
		source: 'gif/hero.gif'
		pos: root.pos
		size: ps, ps

<Dungeon>:
	Widget:
		size: root.dw, root.dh
		canvas.before:
			Color:
				rgba: 1, 1, 1, 1
			Rectangle:
				pos: root.ww * 0.05, root.wh * 0.5
				size: root.dw, root.dh
				source: 'images/dungeon.png'

		Mob:
			pos: root.ww * 0.05 + (root.dw * 1 / 6), root.wh * 0.5 + ms * 0.5

		Mob:
			pos: root.ww * 0.05 + (root.dw * 2 / 6), root.wh * 0.5 + ms * 0.5
		Mob:
			pos: root.ww * 0.05 + (root.dw * 2 / 6), root.wh * 0.5 + ms * 0.5

		Mob:
			pos: root.ww * 0.05 + (root.dw * 3 / 6), root.wh * 0.5 + ms * 0.5

		Mob:
			pos: root.ww * 0.05 + (root.dw * 4 / 6), root.wh * 0.5 + ms * 0.5

		Boss:
			pos: root.ww * 0.05 + (root.dw * 5 / 6), root.wh * 0.5 + bs * 0.5


		Hero:
			pos: root.ww * 0.05, root.wh * 0.5 + ps * 0.55
''')

class Hero(Widget):
	pass

class Boss(Widget):
	pass

class Mob(Widget):
	pass

class Dungeon(Widget):
	ww, wh = Window.size[0], Window.size[1]
	dw, dh = ww * 0.9, wh * 0.25
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		print('screen size: ', self.ww, self.wh)
		print('map size: ', self.dw, self.dh)

class AwesomeApp(App):
	def build(self):
		return Dungeon()

if __name__ == '__main__':
	AwesomeApp().run()
