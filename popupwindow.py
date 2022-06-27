from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

Builder.load_string('''
#:import Factory kivy.factory.Factory
<Dungeon@Popup>:
	size_hint: None, None
	size: 500, 400
	title: ''
	separator_height: 0
	BoxLayout:
		orientation: 'vertical'
		Image:
			source: 'dungeon.png'
			size_hint: None, None
			allow_scretch: True
			size: 473, 224
			pos_hint: {'center_x': 0.5}
		Button:
			text: 'press me'
			on_press: root.dismiss()

<MainPage>:
	Button:
		id: main_btn
		text: 'show up'
		size_hint: None, None
		center_x: self.parent.center_x
		y: 0
		#on_release:
			#print('show up')
			#Factory.Dungeon().open()
			#root.switch_screen(name='dungeonpage')

<DungeonPage>:
	BoxLayout:
		orientation: 'vertical'
		Image:
			source: 'dungeon.png'
		Button:
			id: dun_btn
			text: 'second'

<Main>:
	ScreenManager:
		id: sm
		MainPage:
			id: mainpage
			name: 'mainpage'
		DungeonPage:
			id: dungeonpage
			name: 'dungeonpage'


''')

class MainPage(Screen):
	pass

class DungeonPage(Screen):
	pass

class Main(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.ids.mainpage.ids.main_btn.bind(on_release=self.switch_dungeon)
		self.ids.dungeonpage.ids.dun_btn.bind(on_release=self.switch_main)
		print(self.ids.sm.ids)

	def switch_dungeon(self, instance):
		self.ids.sm.current = 'dungeonpage'

	def switch_main(self, instance):
		self.ids.sm.current = 'mainpage'

class MainApp(App):
	def build(self):
		return Main()

if __name__ == '__main__':
	MainApp().run()
