from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window

Window.size = [800, 1000]



Builder.load_string('''
<BagItem>:
	#item_pos: 500, 500
	size_hint: None, None
	width: 80
	height: 80
	pos: self.pos
	item_image: ''
	canvas.after:
		Color:
			rgba: 1, 1, 1, 1
		Line:
			width: 1
			rectangle: self.x, self.y, self.width, self.height
	ToggleButton:
		group: 'item_select'
		text: ''
		size: self.parent.size
		pos: self.parent.pos
		on_press: print('HI')
		Image:
			size_hint: None, None
			size: self.parent.size
			source: 'icons/item/weapon/003.png'
			#source: root.item_image
			allow_stretch: True
			center_x: self.parent.center_x
			center_y: self.parent.center_y

<Bag>:
	size_hint: None, None
	#size: root.ww * 0.9, root.wh * 0.5
	width: root.mw
	height: root.mh
	pos: [root.ww * 0.05, root.wh * 0.1]
	canvas.before:
		Color:
			rgba: 61/255, 60/255, 57/255, 1
		Rectangle:
			pos: self.pos
			size: self.size

		Color:
			rgba: 1, 1, 1, 1
		Line: # grid: 80x80, 8x5 grids
			width: root.linew
			rectangle: (root.rect_startx, root.rect_starty, root.grid_width, \
				root.grid_height)
		Line:
			width: root.linew
			points: root.grid_col_x[0], root.grid_col_y[0], \
					root.grid_col_x[0], root.grid_col_y[1]
		Line:
			width: root.linew
			points: root.grid_col_x[1], root.grid_col_y[0], \
					root.grid_col_x[1], root.grid_col_y[1]
		Line:
			width: root.linew
			points: root.grid_col_x[2], root.grid_col_y[0], \
					root.grid_col_x[2], root.grid_col_y[1]
		Line:
			width: root.linew
			points: root.grid_col_x[3], root.grid_col_y[0], \
					root.grid_col_x[3], root.grid_col_y[1]
		Line:
			width: root.linew
			points: root.grid_col_x[4], root.grid_col_y[0], \
					root.grid_col_x[4], root.grid_col_y[1]
		Line:
			width: root.linew
			points: root.grid_col_x[5], root.grid_col_y[0], \
					root.grid_col_x[5], root.grid_col_y[1]
		Line:
			width: root.linew
			points: root.grid_col_x[6], root.grid_col_y[0], \
					root.grid_col_x[6], root.grid_col_y[1]
		Line:
			width: root.linew
			points: root.grid_row_x[0], root.grid_row_y[0], \
					root.grid_row_x[1], root.grid_row_y[0]
		Line:
			width: root.linew
			points: root.grid_row_x[0], root.grid_row_y[1], \
					root.grid_row_x[1], root.grid_row_y[1]
		Line:
			width: root.linew
			points: root.grid_row_x[0], root.grid_row_y[2], \
					root.grid_row_x[1], root.grid_row_y[2]
		Line:
			width: root.linew
			points: root.grid_row_x[0], root.grid_row_y[3], \
					root.grid_row_x[1], root.grid_row_y[3]

<BagWidget>:
	Bag:
		id: bag

	BoxLayout:
		size_hint_y: None
		height: 50
		size_hint_x: None
		width: root.ww * 0.9
		pos: root.ww * 0.05, root.wh * 0.65 
		Label:
			text: 'col#1'
		Label:
			text: 'col#2'
	# lines

<Root>:
	BagWidget:
		id:bag_widget
''')

class BagItem(Widget):
	def __init__(self, item_image, **kwargs):
		super().__init__(**kwargs)
		#print(**kwargs)
		self.item_image = item_image

class Bag(Widget):
	#ww, wh = app().window_size[0], app().window_size[1]
	ww, wh = Window.size[0], Window.size[1]
	mw, mh = Window.size[0] * 0.9, Window.size[1] * 0.6

	# grids
	grid_size = 80
	linew = 1
	grid_width = grid_size * 8 + linew * 9
	grid_height = grid_size * 5 + linew * 6
	y_offset = 70
	rect_startx = (mw - grid_width) / 2 + ww * 0.05
	#rect_starty = (wh * 0.4 - grid_height) / 2 + wh * 0.15 + y_offset
	rect_starty = wh * 0.15 + y_offset
	grid_col_x = [rect_startx + (grid_size + linew) * 1, \
					rect_startx + (grid_size + linew) * 2, \
					rect_startx + (grid_size + linew) * 3, \
					rect_startx + (grid_size + linew) * 4, \
					rect_startx + (grid_size + linew) * 5, \
					rect_startx + (grid_size + linew) * 6, \
					rect_startx + (grid_size + linew) * 7]
	grid_col_y = [rect_starty, rect_starty + grid_height]
	grid_row_x = [rect_startx, rect_startx + grid_width]
	grid_row_y = [rect_starty + (grid_size + linew) * 1, \
					rect_starty + (grid_size + linew) * 2, \
					rect_starty + (grid_size + linew) * 3, \
					rect_starty + (grid_size + linew) * 4]

	bag_storage = []
	def __init__(self, **kwargs):
		super(Bag, self).__init__(**kwargs)

		# define bag_storage
		n, m = 8, 5
		for i in range(m):
			for j in range(n):
				#print(i, j)
				self.bag_storage.append(\
					[self.rect_startx + j * (self.grid_size + self.linew), \
					self.rect_starty + ((m-1)-i) * (self.grid_size + self.linew)])

		# for test storage position correct or not
		#for each in self.bag_storage:
		#	print(each)
		#	self.add_item(pos=each, item='item')

		#self.next_position = 0
		# occupied: [{'position_id': 0, 'item': item}]
		self.occupied = []

	def init_bag(self, bag_data):
		# init bag by read bag json
		print("init_bag()")

		for item in bag_data:
			self.add_item(item)
			self.occupied.append(item)

	def reset_items(self):
		for item in self.occupied:
			print(item)
			self.add_item(item, insert=True)

	def add_item(self, item, insert=False):
		print("add_item() ", item)

		pos_index = len(self.occupied)
		if insert:
			pos_index -= 1

		self.add_widget(BagItem(pos=self.bag_storage[pos_index], \
						item_image='icons/item/weapon/003.png'))

		# send to server to update json in main.py

	# position means position-th instead of index
	def remove_item(self, position):
		print("remove_item()")
		#print(self.children)

		self.occupied.pop(position-1)
		#print(self.occupied)

		# clear all grids
		self.clear_widgets()

		# reset items
		self.reset_items()

	#def on_size(self, *args):
		#print("Bag(on_size): ", *args)
		#print(self.parent.height)

class BagWidget(Widget):
	ww, wh = Window.size[0], Window.size[1]
	mw, mh = Window.size[0] * 0.9, Window.size[1] * 0.6

class Root(Screen):

	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		print(self.ids)
	#def on_size(self, *args):
		#print("Root(on_size): ", *args)

class AwesomeApp(App):

	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.window_size = [800, 1000]

	def build(self):
		root = Root()

		# read items
		import json
		import item_manage
		db = 'data/item.json'

		im = item_manage.ItemManager(db=db)
		item = im.random_eq(['weapon'], 120, 1)
		#print(item)
		bag_data = []
		bag_data.append(item)

		item2 = im.random_eq(['suit'], 120, 1)
		bag_data.append(item2)

		print(bag_data)
		root.ids.bag_widget.ids.bag.init_bag(bag_data)
		#root.ids.bag_widget.ids.bag.add_item(item)

		root.ids.bag_widget.ids.bag.remove_item(1)
		return root

if __name__ == '__main__':
	Window.size = [800, 1000]
	Window.clearcolor = 1, 1, 1, 1
	AwesomeApp().run() 
