from PIL import Image, ImageDraw

w, h = 96, 96
shape = [(0, 0), (96, 96)]

img = Image.new("RGB", (w, h))

img1 = ImageDraw.Draw(img)
img1.rectangle(shape, fill='#ffffff')

line1 = [(10, 10), (48, 86)]
img1.line(line1, fill="#ff0000", width=10)
line2 = [(48, 86), (86, 10)]
img1.line(line2, fill="#ff0000", width=10)

img.show()
img.save('myimg.png')
