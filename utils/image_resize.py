from PIL import Image
import sys
import os

#print(sys.argv[1])
ratio = 3
#resize = (1440//ratio, 2911//ratio)
#resize = (1440//ratio, 1440//ratio)
#resize = (225 // ratio, 225 // ratio)
resize = (100, 100)

file = sys.argv[1]
base = os.path.basename(file)
target = os.path.splitext(base)[0] + '-resized.png'

img = Image.open(file)
img_resized = img.resize(resize, Image.Resampling.LANCZOS)
img_resized.save(target) 



#print("Image(%s) size: %d, %d" % (file, img.width, img.height))
