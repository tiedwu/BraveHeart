from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.uix.widget import Widget

from kivy.properties import StringProperty, NumericProperty, ObjectProperty
from kivy.properties import ReferenceListProperty

from kivy.vector import Vector

Window.clearcolor = [1, 1, 1, 1]
Window.size = [1440, 2911]
#Window.size = [800, 1000]

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
		#source: 'gif/hero.gif'
		source: root.hero_img
		anim_delay: 0.12
		pos: root.pos
		size: ps, ps

<DungeonButton@Button>:
	font_name: 'fonts/DroidSansFallback.ttf'
	background_color: 230/255, 162/255, 73/255, 1
	size: 220, 150

<Dungeon>:
	mob1: mob1
	mob2: mob2
	mob3: mob3
	mob4: mob4
	mob5: mob5
	boss: boss
	hero: hero

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
			id: mob1
			pos: root.ww * 0.05 + (root.dw * 1 / 6), root.mob_y
		Mob:
			id: mob2
			pos: root.ww * 0.05 + (root.dw * 2 / 6), root.mob_y
		Mob:
			id: mob3
			pos: root.ww * 0.05 + (root.dw * 2 / 6), root.mob_y
		Mob:
			id: mob4
			pos: root.ww * 0.05 + (root.dw * 3 / 6), root.mob_y
		Mob:
			id: mob5
			pos: root.ww * 0.05 + (root.dw * 4 / 6), root.mob_y
		Boss:
			id: boss
			pos: root.ww * 0.05 + (root.dw * 5 / 6), root.dungeon_y + (bs * 0.5)

		Hero:
			id: hero
			pos: root.ww * 0.05, root.dungeon_y + (ps * 0.55)
	DungeonButton:
		id: dungeon_exit
		pos: root.ww * 0.05 + (root.dw * 5 / 6), root.dungeon_y - 170
		text: '结束挑战'

''')

class Hero(Widget):
	hero_img = StringProperty('gif/hero.gif')

	velocity_x = NumericProperty(0)
	velocity_y = NumericProperty(0)
	velocity = ReferenceListProperty(velocity_x, velocity_y)

	ww, wh = Window.size[0], Window.size[1]
	dw, dh = ww * 0.9, wh * 0.15

	bs = 160
	ps = 160
	hero_y = wh * 0.4 + (ps * 0.55)
	turnover = False

	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.velocity = [1, 0]
		self.run_once = False

	def set_run_once():
		self.run_once = True

	def unset_run_once():
		self.run_once = False

	def start(self):
		self.pos = self.ww * 0.05, self.hero_y

	def move(self):
		#print('moving')
		bound = self.ww * 0.05 + self.dw - (self.bs * 0.9)
		if self.pos[0] >= bound:
			self.pos = self.ww * 0.05, self.hero_y
			self.turnover = True
			#if self.run_once:
			#	self.opacity = 0
			#	self.disable = False
		else:
			self.pos = Vector(*self.velocity) + self.pos
			#self.turnover = False

		# mark for next game in the future
		if self.velocity == [0, 1]:
			self.hero_img = 'gif/hero.gif'
		elif self.velocity == [0, -1]:
			self.hero_img = 'gif/hero.gif'
		elif self.velocity == [-1, 0]:
			self.hero_img = 'gif/hero.gif'
		elif self.velocity == [1, 0]:
			self.hero_img = 'gif/hero.gif' 

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
		#print('screen size: ', self.ww, self.wh)
		#print('map size: ', self.dw, self.dh)
		self.enemies = [self.mob1, self.mob2, self.mob3, self.mob4, 
				self.mob5, self.boss]

		self.run_once = True

	def start(self):
		self.hero.start()
		self.reset_enemies()

	def check_collision(self):

		if self.hero.turnover:

			if self.run_once:
				self.opacity = 0
				self.disable = True

				self.parent.home.opacity = 1
				self.parent.home.disable = False
			else:
				self.reset_enemies()
			self.hero.turnover = False

		for e in self.enemies:
			if self.hero.pos >= e.pos:
				e.opacity = 0
				e.disabled = True

	def enemy_die(self, enemy_id):
		self.enemies[enemy_id].opacity = 0
		self.enemies[enemy_id].disable = True

	def reset_enemies(self):
		for e in self.enemies:
			e.opacity = 1
			e.disable = False

class AwesomeApp(App):
	def build(self):
		return Dungeon()

if __name__ == '__main__':
	AwesomeApp().run()
