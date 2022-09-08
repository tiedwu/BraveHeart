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

	#size = (80, 80)
	#n = 1
	#for rect in coords:
	cropped_image = image.crop(coord)
		#resized = cropped_image.resize(size, Image.Resampling.LANCZOS)
		#resized.save(f'{dist}/{n}.jpg')
		#n += 1
	cropped_image.show()


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

	# pt0
	x1, y1 = 452, 930
	x2, y2 = x1+125,y1+125
	pt0 = (x1, y1, x2, y2)
	rects.append(pt0)

	# pt
	x1, y1 = 452, 1267
	x2, y2 = x1+125,y1+125
	pt = (x1, y1, x2, y2)
	rects.append(pt)

	# pt1
	x1, y1 = 452, 1604
	x2, y2 = x1 + 125, y1+125
	pt1 = (x1, y1, x2, y2)
	rects.append(pt1)

	# pt2
	x1, y1 = 452, 1940
	x2, y2 = x1+125, y1+125
	pt2 = (x1, y1, x2, y2)
	rects.append(pt2) 

	#crop3(image, pt0, 'out')
	crop2(image, rects, 'out')


