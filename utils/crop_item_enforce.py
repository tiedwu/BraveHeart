from PIL import Image

def crop_resize(image_path, coords, saved_location):
	image_obj = Image.open(image_path)

	size = (80, 80)
	n = 1
	for rect in coords:
		cropped_image = image_obj.crop(rect)
		resized = cropped_image.resize(size, Image.Resampling.LANCZOS)
		resized.save(f'{saved_location}/{n}.jpg')
		n += 1

def crop(image_path, coords, saved_location):
	image_obj = Image.open(image_path)

	n = 1
	for rect in coords:
		cropped_image = image_obj.crop(rect)
		#resized = cropped_image.resize(size, Image.Resampling.LANCZOS)
		cropped_image.save(f'{saved_location}/{n}.jpg')
		n += 1

def crop2(image_path, coords, dist):
	image = Image.open(image_path)

	size = (80, 80)
	n = 1
	for rect in coords:
		cropped_image = image.crop(rect)
		resized = cropped_image.resize(size, Image.Resampling.LANCZOS)
		resized.save(f'{dist}/{n}.jpg')
		n += 1

def crop_show(image_path, coord, dist):
	image = Image.open(image_path)
	cropped = image.crop(coord)
	cropped.show() 


if __name__ == '__main__':
	image = 'source.jpg'
	#image = 's2.jpg'
	top_y = 2911
	rects = []

	x1, y1 = 110, 304
	x2, y2 = x1 + 1225, y1 + 150
	gy = (x1, y1, x2, y2)
	# item_enforce_widget_endy = top_y - y1
	# 2911 - 304 = 2607
	# from alpha bar 2607 + 5 = 2612

	# check title height 150
	# item_enforce_widget_width = 1225(include alpha bar)
	# set alpha = 5
	# title width = widget_width - 2 * 5

	# word y: 454, 634
	# image
	x1, y1 = 110, 629
	x2, y2 = x1 + 1225, y1 + 125
	im = (x1, y1, x2, y2)

	# harrow, varrow
	x1, y1 = 110, 900
	x2, y2 = x1 + 1225, y1 + 45
	ar = (x1, y1, x2, y2)

	# harrow
	x1, y1 = 685, 900
	x2, y2 = x1 + 45, y1 + 45
	ar1 = (x1, y1, x2, y2)

	# varrow
	x1, y1 = 946, 900
	x2, y2 = x1 + 45, y1 + 45
	ar2 = (x1, y1, x2, y2)

	# btn
	x1, y1 = 870, 1083
	x2, y2 = x1 + 275, y1 + 95
	btn = (x1, y1, x2, y2)

	# ticket
	x1, y1 = 240, 1340
	x2, y2 = x1 + 85, y1 + 80
	tk = (x1, y1, x2, y2)
	#rects.append(tk)

	# check box s1
	x1, y1 = 906, 1361
	x2, y2 = x1 + 48, y1 + 48
	cb = (x1, y1, x2, y2)
	rects.append(cb)

	# check box s2
	x1, y1 = 906, 1389
	x2, y2 = x1 + 48, y1 + 48
	cb2 = (x1, y1, x2, y2)
	#rects.append(cb2)


	#rects.append(ar2)
	# show
	#crop_show(image, cb, 'out')

	#rects.append(st)
	# save
	#crop_resize(image, eq_rects, 'out')
	crop(image, rects, 'out')
	
