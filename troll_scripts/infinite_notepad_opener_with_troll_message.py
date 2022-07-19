#pip install pynput

import pynput, os
from pynput.keyboard import Key, Listener
import subprocess as sp
keys = []
with open('readme.txt', 'w') as various:			#creating a text file before going through the loop
    various.write('yeet, you got trolled')
def press(enteredkey):
	keys.append(enteredkey)			
def release(key):
	progname = "Notepad.exe"
	textfile_name = "readme.txt"
	sp.Popen([progname, textfile_name])
	#print(key)										#remove hashtag before print(key) to get the key which is pressed
	if key == Key.esc:
		return False
with Listener(on_press = press, on_release = release) as x:					
	x.join()
