from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.uix.widget import Widget

Window.clearcolor = [1, 1, 1, 1]
Window.size = [1440, 2911]

Builder.load_string('''
#:set ms 180
#:set bs 160
#:set ps 160
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
		#dungeon_y: root.wh * 0.3
		canvas.before:
			Color:
				rgba: 1, 1, 1, 1
			Rectangle:
				pos: root.ww * 0.05, root.dungeon_y
				size: root.dw, root.dh
				source: 'images/dungeon.png'

		Mob:
			pos: root.ww * 0.05 + (root.dw * 1 / 6), root.mob_y
		Mob:
			pos: root.ww * 0.05 + (root.dw * 2 / 6), root.mob_y
		Mob:
			pos: root.ww * 0.05 + (root.dw * 2 / 6), root.mob_y
		Mob:
			pos: root.ww * 0.05 + (root.dw * 3 / 6), root.mob_y
		Mob:
			pos: root.ww * 0.05 + (root.dw * 4 / 6), root.mob_y
		Boss:
			pos: root.ww * 0.05 + (root.dw * 5 / 6), root.dungeon_y + (bs * 0.5)

		Hero:
			pos: root.ww * 0.05, root.dungeon_y + (ps * 0.55)
''')

class Hero(Widget):
	pass

class Boss(Widget):
	pass

class Mob(Widget):
	pass

class Dungeon(Widget):
	ww, wh = Window.size[0], Window.size[1]
	dw, dh = ww * 0.9, wh * 0.15
	dungeon_y = wh * 0.4

	# mob size
	mob_size = 180
	mob_y = dungeon_y + ((mob_size / 3) * 1)

	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		print('screen size: ', self.ww, self.wh)
		print('map size: ', self.dw, self.dh)

class AwesomeApp(App):
	def build(self):
		return Dungeon()

if __name__ == '__main__':
	AwesomeApp().run()
