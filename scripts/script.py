import time
import os

while True:
	file = 'C:\Users\Administrator\Downloads\somefile1'

	if os.path.isfile(file):

		# open file and obtain content
		f = open(file, 'r')
		content = f.read()

		if content == "remove file x":
			print "x"
		elif content == "invoke autoit script x":
			print "y"

		# close file handle
		f.close()

		# remove file so this condition doesn't happen again
		os.remove(file)

	# optional sleep for five seconds
	time.sleep(5)

