from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen
from kivy.graphics import Color, RoundedRectangle, Line, Rectangle
from kivy.uix.label import Label
from kivy.uix.behaviors import ButtonBehavior, ToggleButtonBehavior
from kivy.uix.image import Image
from kivy.uix.togglebutton import ToggleButton
from kivy.graphics.instructions import Canvas

from common.widgets import ImageButton, AL_Label, GC_Label, SlotToggleButton, BH_Button

Builder.load_string('''
<Root>:

''')

#class ImageButton(ButtonBehavior, Image):
#	def __init__(self, **kwargs):
#		super().__init__(**kwargs)

class BBLabel(Label):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		if 'font_size' in list(kwargs.keys()):
			self.font_size = kwargs['font_size']
		self.font_name = 'fonts/DroidSansFallback.ttf'
		self.color = [193 / 255, 170 / 255, 154 / 255, 1]
		self.size_hint = None, None

class BBAlignLabel(Label):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.font_name = 'fonts/DroidSansFallback.ttf'
		self.size_hint = None, None
		self.text_size = self.size
		self.halign = "left"
		self.valign = "middle"

class BeadWidget(Widget):
	def __init__(self, screen_width, screen_height, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.width = screen_width * 0.9
		self.height = screen_height * 0.60
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
		bg_startx = title_startx
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

		# title
		lbl_title = BBLabel(text='精气珠', pos=[title_startx, title_starty], \
							width=title_width, height=title_height)
		self.add_widget(lbl_title)

		btn_exit_width, btn_exit_height = 74, 74
		# exit button
		btn_tips_pad_x = 20
		title_endx = title_startx + title_width
		btn_exit_endx = title_endx - btn_tips_pad_x
		btn_exit_x = btn_exit_endx - btn_exit_width
		btn_exit_y = title_starty + (title_height - btn_exit_height) / 2
		btn_exit = ImageButton(size_hint=[None, None], size=[btn_exit_width, btn_exit_height], \
						  pos=[btn_exit_x, btn_exit_y], source='icons/exit.jpg')
		self.add_widget(btn_exit)

		# tips button
		btn_tips_padx = 20
		btn_tips_endx = btn_exit_x - btn_tips_pad_x
		btn_tips_width, btn_tips_height = 74, 74
		btn_tips_x = btn_tips_endx - btn_tips_width
		btn_tips_y = title_starty + (title_height - btn_tips_height) / 2
		btn_tips = ImageButton(size_hint=[None, None], size=[btn_tips_width, btn_tips_height], \
						  pos=[btn_tips_x, btn_tips_y], source='icons/tips.jpg')
		self.add_widget(btn_tips)

		# Label_slot
		lbl_slot_pad_x = 50
		lbl_slot_pad_y = 30
		lbl_slot_width = 500
		lbl_slot_height = 60
		lbl_slot_x = title_startx + lbl_slot_pad_x
		lbl_slot_y = title_starty - lbl_slot_pad_y - lbl_slot_height
		lbl_slot = AL_Label(text='精气珠装备槽', pos=[lbl_slot_x, lbl_slot_y], \
							size=[lbl_slot_width, lbl_slot_height], halign="left")
		self.add_widget(lbl_slot)

		# Label_qulity
		lbl_qulity_pad_x = 100
		lbl_qulity_pad_y = 30
		lbl_qulity_width = 500
		lbl_qulity_height = 60
		lbl_qulity_endx = title_startx + title_width - lbl_qulity_pad_x
		lbl_qulity_x = lbl_qulity_endx - lbl_qulity_width
		lbl_qulity_y = title_starty - lbl_qulity_pad_y - lbl_qulity_height
		total_bead_level = 8700
		text = f'总品质等级: {total_bead_level}'
		lbl_qulity = AL_Label(text=text, pos=[lbl_qulity_x, lbl_qulity_y], \
							size=[lbl_qulity_width, lbl_qulity_height], halign='right')
		self.add_widget(lbl_qulity)

		# slot * 4, destiny_bead * 1
		slot_space_x = 15
		slot_width, slot_height = 149, 149
		total_slot_width = 5 * slot_width + 4 * slot_space_x
		slot_pad_x = (title_width - total_slot_width) / 2
		slot_1st_x = title_startx + slot_pad_x
		slot_space_y = 50
		slot_1st_y = lbl_slot_y - slot_space_y - slot_height
		slot_2nd_x = slot_1st_x + slot_width + slot_space_x
		slot_3rd_x = slot_2nd_x + slot_width + slot_space_x
		slot_4th_x = slot_3rd_x + slot_width + slot_space_x
		slot_5th_x = slot_4th_x + slot_width + slot_space_x
		with self.canvas.before:
			Color(1, 1, 1, 1)
			Line(rectangle=[slot_1st_x, slot_1st_y, slot_width, slot_height], width=2)
			Line(rectangle=[slot_2nd_x, slot_1st_y, slot_width, slot_height], width=2)
			Line(rectangle=[slot_3rd_x, slot_1st_y, slot_width, slot_height], width=2)
			Line(rectangle=[slot_4th_x, slot_1st_y, slot_width, slot_height], width=2)
			Line(rectangle=[slot_5th_x, slot_1st_y, slot_width, slot_height], width=2)
			
		lbl_setting_space_y = 50
		lbl_setting_width = 100
		lbl_setting_height = 60
		lbl_setting_center_x = title_startx + title_width / 2
		lbl_setting_center_y = slot_1st_y - lbl_setting_space_y - lbl_setting_height / 2
		print(f'[bead_box.py] __init__(lbl_setting_center_y={lbl_setting_center_y})')
		lbl_setting_y = slot_1st_y - lbl_setting_space_y - lbl_setting_height
		#lbl_setting_center_x = 500
		lbl_setting = GC_Label(text='精气珠槽切换: ', center_x=lbl_setting_center_x, y=lbl_setting_y, \
							   size=[lbl_setting_width, lbl_setting_height])
		self.add_widget(lbl_setting)

		tgbtn_slot_width, tgbtn_slot_height = 50, 50
		tgbtn_slot_down_width, tgbtn_slot_down_height = 60, 60
		tgbtn_slot_3rd_pad_center_x = 100
		tgbtn_slot_space_center_x = 100
		tgbtn_slot_3rd_center_x = title_startx + title_width - tgbtn_slot_3rd_pad_center_x
		tgbtn_slot_2nd_center_x = tgbtn_slot_3rd_center_x - tgbtn_slot_space_center_x
		tgbtn_slot_1st_center_x = tgbtn_slot_2nd_center_x - tgbtn_slot_space_center_x
		tgbtn_slot_center_y = lbl_setting_center_y
		print(f'[bead_box.py] __init__(lbl_setting_center_y={lbl_setting_center_y})')
		normal_size = [tgbtn_slot_width, tgbtn_slot_height]
		down_size = [tgbtn_slot_down_width, tgbtn_slot_down_height]
		tgbtn_slot_1st = SlotToggleButton(text="1", group='slot_select', state="normal")
		tgbtn_slot_1st.pos = [tgbtn_slot_1st_center_x -  tgbtn_slot_width / 2, \
							  tgbtn_slot_center_y - tgbtn_slot_height / 2]
		tgbtn_slot_1st.size = [tgbtn_slot_width, tgbtn_slot_height]
		tgbtn_slot_1st.bind(state=self.on_tgbtn_slot_state)
		self.add_widget(tgbtn_slot_1st)

		tgbtn_slot_2nd = SlotToggleButton(text="2", group='slot_select', state="normal")
		tgbtn_slot_2nd.pos = [tgbtn_slot_2nd_center_x - tgbtn_slot_width / 2, \
							  tgbtn_slot_center_y - tgbtn_slot_height / 2]
		tgbtn_slot_2nd.size = [tgbtn_slot_width, tgbtn_slot_height]
		tgbtn_slot_2nd.bind(state=self.on_tgbtn_slot_state)
		self.add_widget(tgbtn_slot_2nd)

		tgbtn_slot_3rd = SlotToggleButton(text="3", group='slot_select', state="normal")
		tgbtn_slot_3rd.pos = [tgbtn_slot_3rd_center_x - tgbtn_slot_width / 2, \
							  tgbtn_slot_center_y - tgbtn_slot_height / 2]
		tgbtn_slot_3rd.size = [tgbtn_slot_width, tgbtn_slot_height]
		tgbtn_slot_3rd.bind(state=self.on_tgbtn_slot_state)
		self.add_widget(tgbtn_slot_3rd)
		tgbtn_slot_1st.state = 'down'

		tgbtn_slot_lowest_y = tgbtn_slot_center_y - tgbtn_slot_down_height / 2
		text = '合成精气珠'
		lbl_bead_combine_pad_x = 50
		lbl_bead_combine_pad_y = 30
		lbl_bead_combine_width = 300
		lbl_bead_combine_height = 60
		lbl_bead_combine_x = title_startx + lbl_bead_combine_pad_x
		lbl_bead_combine_y = tgbtn_slot_lowest_y - lbl_bead_combine_pad_y - lbl_bead_combine_height
		lbl_bead_combine = AL_Label(text=text, pos=[lbl_bead_combine_x, lbl_bead_combine_y], \
									size=[lbl_bead_combine_width, lbl_bead_combine_height], halign='left')
		self.add_widget(lbl_bead_combine)

		bead_chip_image_src = 'icons/bead_chip.jpg'
		bead_chip_image_width, bead_chip_image_height = 100, 100
		bead_chip_image_pad_y = 20
		bead_chip_image_y = lbl_bead_combine_y - bead_chip_image_pad_y - bead_chip_image_height
		bead_chip_image_x = lbl_bead_combine_x
		bead_chip_image = Image(pos=[bead_chip_image_x, bead_chip_image_y], size_hint=[None, None],\
								  size=[bead_chip_image_width, bead_chip_image_height], \
								  source=bead_chip_image_src)
		self.add_widget(bead_chip_image)

		bead_chip_amount = 8635
		lbl_chip_amount_pad_x = 10
		lbl_chip_amount_width, lbl_chip_amount_height = 300, 100
		lbl_chip_amount_x = bead_chip_image_x + bead_chip_image_width + lbl_chip_amount_pad_x
		lbl_chip_amount_y = bead_chip_image_y
		lbl_chip_amount = AL_Label(text=f'{bead_chip_amount}', pos=[lbl_chip_amount_x, lbl_chip_amount_y], \
								   size=[lbl_chip_amount_width, lbl_chip_amount_height], halign='left')
		self.add_widget(lbl_chip_amount)

		# 3 buttons: store, combination 10 times, combination once
		btn_combine_once_padx = lbl_bead_combine_pad_x
		btn_combine_once_width, btn_combine_once_height = 200, 100
		btn_combine_once_x = title_startx + title_width - btn_combine_once_padx - btn_combine_once_width
		btn_combine_once_y = lbl_chip_amount_y
		btn_combine_once = BH_Button(text='合成', pos=[btn_combine_once_x, btn_combine_once_y], \
									 size=[btn_combine_once_width, btn_combine_once_height])
		self.add_widget(btn_combine_once)

		btn_combine_ten_padx = 50
		btn_combine_ten_width, btn_combine_ten_height = 200, 100
		btn_combine_ten_x = btn_combine_once_x  - btn_combine_ten_padx - btn_combine_ten_width
		btn_combine_ten_y = lbl_chip_amount_y
		btn_combine_ten = BH_Button(text='十连合成', pos=[btn_combine_ten_x, btn_combine_ten_y], \
									 size=[btn_combine_ten_width, btn_combine_ten_height])
		self.add_widget(btn_combine_ten)

		btn_chipstore_padx = 50
		btn_chipstore_width, btn_chipstore_height = 200, 100
		btn_chipstore_x = btn_combine_ten_x - btn_chipstore_padx - btn_chipstore_width
		btn_chipstore_y = lbl_chip_amount_y
		btn_chipstore = BH_Button(text='精粹商店', pos=[btn_chipstore_x, btn_chipstore_y], \
								  size=[btn_chipstore_width, btn_chipstore_height])
		self.add_widget(btn_chipstore)

		# storage grids
		#grid_pad_x = lbl_bead_combine_pad_x
		separate_line_width = 2
		column_number = 8
		row_number = 5
		#grid_width = (title_width - 2 * grid_pad_x - 7 * separate_line_width) / row_number
		#grid_height = grid_width
		grid_width, grid_height = 150, 150
		grid_pad_x = (title_width - (column_number * grid_width + (column_number + 1) * separate_line_width)) / 2
		row_1st_pad_y = 50
		row_1st_x = title_startx + grid_pad_x
		row_1st_width = title_width - 2 * grid_pad_x
		row_1st_y = btn_chipstore_y - row_1st_pad_y - separate_line_width
		row_last_y = row_1st_y - row_number * grid_height - row_number * separate_line_width
		total_grid_width = (column_number + 1) * separate_line_width + column_number * grid_width
		total_grid_height = (row_number + 1) * separate_line_width + row_number * grid_height

		with self.canvas.before:
			Color(32/255, 27/255, 21/255, 1)
			Rectangle(pos=[row_1st_x, row_last_y], size=[total_grid_width, total_grid_height])

			row_y = row_1st_y
			Color(119 / 255, 102 / 255, 74 / 255, 1)
			for i in range(row_number+1):
				#Color(119 / 255, 102 / 255, 74 / 255, 1)
				Line(points=[row_1st_x, row_y, row_1st_x + row_1st_width, row_y], width=separate_line_width)
				row_y = row_y - grid_height - separate_line_width
			row_x = row_1st_x
			for j in range(column_number+1):
				#Color(119 / 255, 102 / 255, 74 / 255, 1)
				Line(points=[row_x, row_1st_y, row_x, row_last_y], width=separate_line_width)
				row_x = row_x + separate_line_width + grid_width

		# bead_amount
		bead_amount = 5
		bead_amount_max = 40
		lbl_bead_amount_pad_y = 50
		lbl_bead_amount_width, lbl_bead_amount_height = 100, 100
		lbl_bead_amount_x = bead_chip_image_x
		lbl_bead_amount_y = row_last_y - lbl_bead_amount_pad_y - lbl_bead_amount_height
		lbl_bead_amount = AL_Label(text=f'{bead_amount}/{bead_amount_max}', \
								   pos=[lbl_bead_amount_x, lbl_bead_amount_y], \
								   size=[lbl_bead_amount_width, lbl_bead_amount_height], halign='left')
		canvas = Canvas()
		canvas.add(Color(0, 0, 1, 1))
		canvas.add(Rectangle(pos=[lbl_bead_amount_x, lbl_bead_amount_y], \
							 size=[lbl_bead_amount_width, lbl_bead_amount_height]))
		lbl_bead_amount.canvas.before.add(canvas)
		self.add_widget(lbl_bead_amount)

		# 2 buttons: collating all, decompose all
		btn_decompose_all_padx = lbl_bead_combine_pad_x
		btn_decompose_all_width, btn_decompose_all_height = 200, 100
		btn_decompose_all_x = title_startx + title_width - btn_decompose_all_padx - btn_decompose_all_width
		btn_decompose_all_y = lbl_bead_amount_y
		btn_decompose_all = BH_Button(text='一键分解', pos=[btn_decompose_all_x, btn_decompose_all_y], \
									 size=[btn_decompose_all_width, btn_decompose_all_height])
		self.add_widget(btn_decompose_all)

		btn_collating_all_pad_x = 50
		btn_collating_all_width, btn_collating_all_height = 200, 100
		btn_collating_all_x = btn_decompose_all_x - btn_collating_all_pad_x - btn_collating_all_width
		btn_collating_all_y = lbl_bead_amount_y
		btn_collating_all = BH_Button(text='一键整理', pos=[btn_collating_all_x, btn_collating_all_y], \
									  size=[btn_collating_all_width, btn_collating_all_height])
		self.add_widget(btn_collating_all)

		# setting image button
		btn_setting_pad_x = 50
		btn_setting_width, btn_setting_height = 62, 60
		btn_setting_x = btn_collating_all_x - btn_setting_pad_x - btn_setting_width
		btn_setting_y = btn_collating_all_y + (btn_collating_all_height - btn_setting_height) / 2
		btn_setting = ImageButton(size_hint=[None, None], size=[btn_setting_width, btn_setting_height], \
								  pos=[btn_setting_x, btn_setting_y], source='icons/misc/setting.jpg')
		self.add_widget(btn_setting)

		# auto decompose setting
		lbl_decompose_setting_pad_x = 20
		lbl_decompose_setting_width, lbl_decompose_setting_height = 250, 100
		lbl_decompose_setting_x = btn_setting_x - lbl_decompose_setting_pad_x - lbl_decompose_setting_width
		lbl_decompose_setting_y = btn_collating_all_y
		lbl_decompose_setting = AL_Label(text=f'自动分解设置', \
								   pos=[lbl_decompose_setting_x, lbl_decompose_setting_y], \
								   size=[lbl_decompose_setting_width, lbl_decompose_setting_height], halign='center')
		canvas = Canvas()
		canvas.add(Color(0, 0, 1, 1))
		canvas.add(Rectangle(pos=[lbl_decompose_setting_x, lbl_decompose_setting_y], \
							 size=[lbl_decompose_setting_width, lbl_decompose_setting_height]))
		lbl_decompose_setting.canvas.before.add(canvas)
		self.add_widget(lbl_decompose_setting)

	def on_tgbtn_slot_state(self, obj, value):
		tgbtn_slot_width, tgbtn_slot_height = 50, 50
		tgbtn_slot_down_width, tgbtn_slot_down_height = 60, 60
		obj_center = obj.center
		DOWN_RIM_COLOR = Color(244/255, 204/255, 82/255, 1)
		NORMAL_RIM_COLOR = Color(0, 0, 0, 0)
		DOWN_TEXT_COLOR = (244/255, 204/255, 82/255, 1)
		NORMAL_TEXT_COLOR = (108/255, 247/255, 244/255, 1)
		print(f'center {obj_center}')
		if obj.state == 'down':
			#obj.text = "D"
			obj_size = [tgbtn_slot_down_height, tgbtn_slot_down_height]
			rim_color = DOWN_RIM_COLOR
			text_color = DOWN_TEXT_COLOR
		elif obj.state == "normal":
			#obj.text = "N"
			obj_size = [tgbtn_slot_width, tgbtn_slot_height]
			rim_color = NORMAL_RIM_COLOR
			text_color = NORMAL_TEXT_COLOR
		obj.pos = [obj_center[0] - obj_size[0] / 2, obj_center[1] - obj_size[1] / 2]
		obj.size = [obj_size[0], obj_size[1]]
		obj.color = text_color
		print(f'update_pos {obj.pos}')
		obj.canvas.after.clear()
		canvas = Canvas()
		canvas.add(rim_color)
		canvas.add(Line(rounded_rectangle=[obj.pos[0], obj.pos[1], obj.size[0], obj.size[1], 2], width=2))
		canvas.opacity = 1.0
		obj.canvas.after.add(canvas)

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
