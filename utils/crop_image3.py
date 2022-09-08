from PIL import Image

def crop(image_path, coords, saved_location):
	image_obj = Image.open(image_path)

	size = (80, 80)
	n = 1
	for rect in coords:
		cropped_image = image_obj.crop(rect)
		resized = cropped_image.resize(size, Image.Resampling.LANCZOS)
		resized.save(f'{saved_location}/{n}.jpg')
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

def crop3(image_path, coord, dist):
	image = Image.open(image_path)
	cropped = image.crop(coord)
	cropped.show() 


if __name__ == '__main__':
	image = 'source.jpg'

	rects = []

	# pt1
	x1, y1 = 150, 1499
	x2, y2 = x1+170, y1+170
	rect1 = (x1, y1, x2, y2)
	#rects.append(rect1)

	# pt2
	x1, y1 = 390, 1499
	x2, y2 = x1+170, y1+170
	rect2 = (x1, y1, x2, y2)
	#rects.append(rect2)

	# pt3
	x1, y1 = 635, 1499
	x2, y2 = x1+170, y1+170
	rect3 = (x1, y1, x2, y2)
	#rects.append(rect3)

	# pt4
	x1, y1 = 880, 1499
	x2, y2 = x1+170, y1+170
	rect4 = (x1, y1, x2, y2)
	#rects.append(rect4)

	# pt5
	x1, y1 = 1125, 1499
	x2, y2 = x1+170, y1+170
	rect5 = (x1, y1, x2, y2)
	#rects.append(rect5)

	# pt
	x1, y1 = 452, 1267
	x2, y2 = x1+125,y1+125
	pt = (x1, y1, x2, y2)
	#rects.append(pt)

	# pt1
	x1, y1 = 452, 1604
	x2, y2 = x1 + 125, y1+125
	pt1 = (x1, y1, x2, y2)
	#rects.append(pt1)

	# pt2
	x1, y1 = 452, 1940
	x2, y2 = x1+125, y1+125
	pt2 = (x1, y1, x2, y2)
	#rects.append(pt2) 

	# ct1
	x1, y1 = 452, 1042
	x2, y2 = x1+125, y1+125
	ct1 = (x1, y1, x2, y2)
	#rects.append(ct1)

	# ct2
	x1, y1 = 452, 1379
	x2, y2 = x1+125, y1+125
	ct2 = (x1, y1, x2, y2)
	#rects.append(ct2)

	# ct3
	x1, y1 = 452, 1715
	x2, y2 = x1+125, y1+125
	ct3 = (x1, y1, x2, y2)
	#rects.append(ct3)

	# ct4
	x1, y1 = 452, 2052
	x2, y2 = x1+125, y1+125
	ct4 = (x1, y1, x2, y2)
	#rects.append(ct4)

	# dt1
	x1, y1 = 452, 1062
	x2, y2 = x1+125, y1+125
	dt1 = (x1, y1, x2, y2)
	rects.append(dt1)

	x1, y1 = 452, 1399
	x2, y2 = x1+125, y1+125
	dt2 = (x1, y1, x2, y2)
	rects.append(dt2)

	x1, y1 = 452, 1735
	x2, y2 = x1+125, y1+125
	dt3 = (x1, y1, x2, y2)
	rects.append(dt3)

	x1, y1 = 452, 2071
	x2, y2 = x1+125, y1+125
	dt4 = (x1, y1, x2, y2)
	rects.append(dt4)

	crop(image, rects, 'out')


