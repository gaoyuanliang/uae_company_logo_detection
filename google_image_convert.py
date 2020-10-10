import re
import os

index = 1
image_dir = u"road_sign_abu_dhabi_files"

while True:
	f = "{}/images\({}\)".format(image_dir, index)
	f_new = "{}/{}_{}.jpg".format(image_dir, image_dir, index)
	cmd = "mv {} {}".format(f,f_new)
	cmd_result = os.system(cmd)
	index += 1
	if cmd_result != 0:
		break
