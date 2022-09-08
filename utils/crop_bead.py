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

def crop_show(image_path, coord, dist):
	image = Image.open(image_path)
	cropped = image.crop(coord)
	cropped.show() 


if __name__ == '__main__':
	image = 'b1.jpg'
	#image = 's2.jpg'
	top_y = 2911
	rects = []

	x1, y1 = 1117, 631
	x2, y2 = x1 + 74, y1 + 74
	qu = (x1, y1, x2, y2)
	#rects.append(qu)

	x1, y1 = 1035, 921
	x2, y2 = x1 + 149, y1 + 149
	slot = (x1, y1, x2, y2)

	# bead_amount image
	x1, y1 = 130, 1350
	x2, y2 = x1+100, y1+100
	ba = (x1, y1, x2, y2)
	#rects.append(ba)

	# grid 150, 150
	x1, y1 = 132, 1550
	x2, y2 = x1 + 150, y1 + 500
	g = (x1, y1, x2, y2)

	# rank 5
	x1, y1 = 426, 1519
	x2, y2 = x1 + 140, y1 + 140
	r5 = (x1, y1, x2, y2)

	# rank 4
	x1, y1 = 1151, 1519
	x2, y2 = x1 + 140, y1 + 140
	r4 = (x1, y1, x2, y2)

	# rank 3
	x1, y1 = 136, 1667
	x2, y2 = x1 + 140, y1 + 140
	r3 = (x1, y1, x2, y2)

	# rank 2
	x1, y1 = 426, 1667
	x2, y2 = x1 + 140, y1 + 140
	r2 = (x1, y1, x2, y2)

	# rank 1
	x1, y1 = 281, 1667
	x2, y2 = x1 + 140, y1 + 140
	r1 = (x1, y1, x2, y2)

	rects.append(r1)
	rects.append(r2)
	rects.append(r3)
	rects.append(r4)
	rects.append(r5)

	# show
	#crop_show(image, r4, 'out')

	#rects.append(st)
	# save
	#crop_resize(image, eq_rects, 'out')
	crop(image, rects, 'out')

