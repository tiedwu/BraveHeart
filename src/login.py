
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

Builder.load_string('''
<MyGrid>:

	name: name
	email: email

	GridLayout:
		cols: 1
		size: root.width - 200, root.height - 200
		pos: 100, 100

		GridLayout:
			cols: 2

			Label:
				text: "Name: "

			TextInput:
				id: name
				multiline: False

			Label:
				text: "Email: "

			TextInput:
				id: email
				multiline: False

		Button:
			text: "Submit"
			on_press: root.btn()


''')

class MyGrid(Widget):

	#name = ObjectProperty(None)
	#email = ObjectProperty(None)

	def btn(self):
		print("Name:", self.name, self.name.text)
		print("Email", self.email, self.email.text)
		self.name.text = ""
		self.email.text = ""
 
class MyApp(App):
	def build(self):
		return MyGrid()

if __name__ == '__main__':
	MyApp().run()
