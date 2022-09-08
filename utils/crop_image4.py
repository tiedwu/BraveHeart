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
	image = 's2.jpg'

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
	#rects.append(dt1)

	x1, y1 = 452, 1399
	x2, y2 = x1+125, y1+125
	dt2 = (x1, y1, x2, y2)
	#rects.append(dt2)

	x1, y1 = 452, 1735
	x2, y2 = x1+125, y1+125
	dt3 = (x1, y1, x2, y2)
	#rects.append(dt3)

	x1, y1 = 452, 2071
	x2, y2 = x1+125, y1+125
	dt4 = (x1, y1, x2, y2)
	#rects.append(dt4)

	x1, y1 = 452, 1485
	x2, y2 = x1+125, y1+125
	et = (x1, y1, x2, y2)
	#rects.append(et)

	# bag grid rect
	x1, y1 = 425, 1385
	x2, y2 = x1+147, y1+147
	ct = (x1, y1, x2, y2)

	# bag exit button
	x1, y1 = 1224, 951
	x2, y2 = x1+74, y1+74
	ft = (x1, y1, x2, y2)

	# ticket
	x1, y1 = 497, 1847
	x2, y2 = x1 + 94, y1 + 74
	tg = (x1, y1, x2, y2)

	# stone
	x1, y1 = 987, 1854
	x2, y2 = x1 + 75, y1 + 75
	sg = (x1, y1, x2, y2)

	# setting
	x1, y1 = 665, 1981
	x2, y2 = x1 + 62, y1 + 60
	st = (x1, y1, x2, y2)

	# item info display window
	x1, y1 = 375, 1030
	x2, y2 = x1 + 690, y1 + 1250
	id = (x1, y1, x2, y2)

	# item info: item image
	x1, y1 = 427, 1090
	x2, y2 = x1 + 142, y1 + 142
	im = (x1, y1, x2, y2)

	#crop_show(image, im, 'out')

	# item info button window
	x1, y1 = 1092, 1270
	x2, y2 = x1 + 255, y1 + 815
	ib = (x1, y1, x2, y2)

	# 1st separate line
	x1, y1 = 427, 1264
	x2, y2 = x1 + 50, y1 + 4
	sl1 = (x1, y1, x2, y2)

	# rank
	x1, y1 = 450, 1305
	x2, y2 = x1 + 120, y1 + 50
	rk = (x1, y1, x2, y2)

	# lv
	x1, y1 = 700, 1395
	x2, y2 = x1 + 400, y1 + 50
	lv = (x1, y1, x2, y2)

	# attrs
	x1, y1 = 440, 1450
	x2, y2 = x1 + 600, y1 + 400
	attrs = (x1, y1, x2, y2)

	# 1st
	x1, y1 = 440, 1450
	x2, y2 = x1 + 500, y1 + 60
	a1 = (x1, y1, x2, y2)

	# 2nd
	x1, y1 = 440, 1515
	x2, y2 = x1 + 500, y1 + 60
	a2 = (x1, y1, x2, y2)

	# 3rd
	x1, y1 = 440, 1580
	x2, y2 = x1 + 500, y1 + 60
	a3 = (x1, y1, x2, y2)

	# 2nd separate line
	x1, y1 = 440, 1682
	x2, y2 = x1 + 500, y1 + 60
	sp2 = (x1, y1, x2, y2)

	# equipped
	eq_rects = []
	x1, y1 = 61, 960
	x2, y2 = x1 + 125, y1 + 125
	ew = (x1, y1, x2, y2)
	eq_rects.append(ew)

	x1, y1 = 61, 1139
	x2, y2 = x1 + 125, y1 + 125
	es = (x1, y1, x2, y2)
	eq_rects.append(es)

	x1, y1 = 61, 1317
	x2, y2 = x1 + 125, y1 + 125
	en = (x1, y1, x2, y2)
	eq_rects.append(en)

	x1, y1 = 61, 1496
	x2, y2 = x1 + 125, y1 + 125
	er = (x1, y1, x2, y2)
	eq_rects.append(er)

	# exit compare
	x1, y1 = 604, 851
	x2, y2 = x1 + 267, y1 + 104
	ec = (x1, y1, x2, y2)

	# lock
	x1, y1 = 1200, 1387
	x2, y2 = x1 + 85, y1 + 85
	ls = (x1, y1, x2, y2)

	# show
	crop_show(image, ls, 'out')

	#rects.append(st)
	# save
	#crop_resize(image, eq_rects, 'out')

	a_hash = [{'a': 99}, {'c': 22}]

	for h in a_hash:
		print(list(h.keys())[0])
		print(list(h.values())[0])
