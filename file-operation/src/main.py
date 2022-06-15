# create the folder if the folder if it was not exist
# get the app name

from kivy.app import App
from kivy.utils import platform
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.logger import Logger
from kivy.uix.button import Button

import os

if platform == 'android':
	from android.permissions import Permission, request_permissions
	from android.permissions import check_permission
	from android.storage import app_storage_path, primary_external_storage_path
	from android.storage import secondary_external_storage_path

Builder.load_string('''

<Root>:
	BoxLayout:
		orientation: 'vertical'
		ScrollView:
			scroll_type: ['bars', 'content']
			bar_width: 10
			Label:
				id: log_label
				canvas.before:
					Color:
						rgba: (0.8, 0.2, 0.5, 1)
					RoundedRectangle:
						radius: [100]
						pos: self.pos
						size: self.size
				size_hint_y: None
				height: self.texture_size[1]
				text_size: self.width, None
				text: ''
				font_size: '30sp'
				padding: 50, 50

		ScrollView:
			GridLayout:
				cols: 1
				size_hint_y: None
				height: self.minimum_height
				id: gd
''')

#def log(msg):
#	Logger.info(msg)

def check_permissions(perms):
	for perm in perms:
		if check_permission(perm) != True:
			return False
	return True

class Root(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.create_file()

	def log(self, msg):
		Logger.info(msg)
		self.ids.log_label.text += f'{msg}\n'

	def create_file(self):

		if platform == 'android':
			perms = [Permission.WRITE_EXTERNAL_STORAGE, 
				Permission.READ_EXTERNAL_STORAGE]

			if check_permissions(perms) != True:
				request_permissions(perms)
				# app has to be restarted, permissions will be work on 2nd start
				exit()
		try:
			self.log('Got requested permissions')

			dir = 'testdir'
			if platform == 'android':
				dir = os.path.join(primary_external_storage_path(), dir)

			if not os.path.isdir(dir):
				# create directory
				os.mkdir(dir)
				self.log(f'created directory {dir}')

			# write file
			#print('123...')
			testfile = bytes([1, 2, 3, 4])

			fname = os.path.join(dir, 'testfile')
			self.log(f'writing to {fname}')

			with open(fname, 'wb') as f:
				f.write(testfile)

			self.log('Done.')

			# copy file
			import shutil
			shutil.copy('profile.json', dir)

			self.log('file copied')

		except:
			self.log('missing permissions?')

	def on_kv_post(self, obj):
		for i in range(100):
			self.ids.gd.add_widget(Button(text=str(i),size_hint_y=None,height=100))

class FileOPApp(App):
	def build(self):
		return Root()

if __name__ == '__main__':
	FileOPApp().run()

	dir = 'testdir'

	print(os.path.isdir(dir))
