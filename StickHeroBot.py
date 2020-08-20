from ppadb.client import Client
from PIL import Image
from numpy import array, uint8
from time import sleep

adb = Client(host='127.0.0.1', port=5037)
devices = adb.devices()

if len(devices) == 0:
	print('no device attached')
	quit()

device = devices[0]

# device.shell('input touchscreen swipe 534 1464 534 1464 350')
while True:
	image = device.screencap()

	with open('screen.png', 'wb') as f:
		f.write(image)

	image = Image.open('screen.png')
	image = array(image, dtype=uint8)

	failsafe = [list(i[:3]) for i in image[1820]][0]
	for i, pixel in enumerate(failsafe):
		r, g, b = [int(i) for i in pixel]
		print(r,g,b)
		if r + g + b < 10:
			print('You Lost!')
			raise SystemExit
		else:
			continue
	quit()
	# 1,440x3,168 pixels

	# 220 just under ninja

	row = [list(i[:3]) for i in image[1820]]

	transitions = []
	ignore = True
	black = True
	cherry = False
	tap = False

	for i, pixel in enumerate(row):
		r, g, b = [int(i) for i in pixel]
		# print(r, g, b)
		if ignore and (r + g + b) != 0:
			continue

		ignore = False

		# Hasn't found cherry yet and then it does find one
		if not cherry and r == 225 and g == 13 and b == 13:
			# Tap screen to make ninja
			# go down and hit cherry
			# need to tap again to
			# put it right way up again
			tap = True
			cherry = True

		if black and (r + g + b) != 0:
			black = not black
			transitions.append(i)
			continue

		if not black and (r + g + b) == 0:
			black = not black
			transitions.append(i)
			continue
	# End of first pillar, start of second and end of second
	# print(transitions)

	start, t1, t2 = transitions

	gap = t1 - start

	t = t2 - t1

	distance = (gap + t / 2) * .98
	print(round(distance))


	# fails 381.71
	if cherry and distance > int(419):
		device.shell(f'input touchscreen swipe 534 1464 534 1464 {round(distance) - 100}')
		device.shell("sleep 0.46; input tap 534 1464; input tap 534 1464")

	else:
		device.shell(f'input touchscreen swipe 534 1464 534 1464 {int(distance)}')

	sleep(3)




