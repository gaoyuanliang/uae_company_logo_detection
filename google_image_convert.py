import re
import os
from PIL import Image

index = 1
image_dir = u"adnoc_station_files"

while True:
	try:
		f = "{}/images\({}\)".format(image_dir, index)
		im=Image.open("{}/images({})".format(image_dir, index))
		f_new = "{}/{}_{}.{}".format(image_dir, image_dir, index, im.format)
		cmd = "mv {} {}".format(f,f_new)
		cmd_result = os.system(cmd)
		index += 1
		if cmd_result != 0:
			break
	except:
		break


dirs = os.listdir( image_dir )

for files in dirs:
	try:
		print(re.search(r'^.*\.json$', files).group())
	except:
		pass
