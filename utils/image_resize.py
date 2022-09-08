from PIL import Image
import sys
import os

#print(sys.argv[1])
ratio = 3
#resize = (1440//ratio, 2911//ratio)
#resize = (1440//ratio, 1440//ratio)
#resize = (225 // ratio, 225 // ratio)
resize = (80, 80)

file = sys.argv[1]
base = os.path.basename(file)
target = os.path.splitext(base)[0] + '-resized.jpg'

img = Image.open(file)
img_resized = img.resize(resize, Image.Resampling.LANCZOS)

# if some png occurs can not write 'P' as 'JPEG'
# try to convert to RGB
img_converted = img_resized.convert('RGB')


#img_resized.show()
#img_resized.save('xx.jpg')

img_converted.save(target)



#print("Image(%s) size: %d, %d" % (file, img.width, img.height))
