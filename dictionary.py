## program for online dictionary
from keyboard import is_pressed

from pyperclip import paste
from PyDictionary import PyDictionary
from Tkinter import *
from pyautogui import size,center,hotkey
import sys

# To igonre warnings
import warnings
if not sys.warnoptions:
    warnings.simplefilter("ignore")

## calculating center location for current screenSize
## used for output window location
screenSize =size()
center_x , center_y =center((0,0,screenSize[0],screenSize[1]))


dictionary = PyDictionary()
last_query = ""
current_query = ""
query_count = 0

window_location = "600x250+"+str(center_x - 300)+"+"+ str(center_y -125)

print("Ready To Search Internet......")

try :
	meaning = dictionary.meaning("apple")
except :
	print("internet error")

def show_window(current_query , output ):
	
	root = Tk()
	S = Scrollbar(root)
	T = Text(root, height=4, width=100)
	S.pack(side=RIGHT, fill=Y)
	T.pack(side=LEFT, fill=Y)
	S.config(command=T.yview)
	T.config(yscrollcommand=S.set ,font=10 ,background="#D3D3D3" )
	T.insert(END, output)
	T.config(state=DISABLED)
	root.title(current_query)
	root.geometry(window_location)

	root.mainloop()




try :
	while(1):
		if is_pressed('ctrl+e'):
			hotkey('ctrl', 'c')

			current_query = paste()
		
			if last_query != current_query :

				last_query = current_query
				query_count += 1
				# printing search keyword to terminal
				print( str(query_count) + " : " + current_query)

				try :
					meaning = dictionary.meaning(current_query)
				
					if "Error" in meaning.keys() or meaning =={}:
						meaning["Error"] = ["check InterNet connection \n ??? connection failure !!!"]
				except :
					meaning = dict()
					meaning["Error"] = ["Check Internet connection  ??? \n   Connection failure !!!"]
				
				 
				output = ""
				# formating Output Content
				for key in meaning:
					output += key + " : \n " + '\n'.join(meaning[key]) + '\n'
				
				show_window(current_query ,output)
					
except:
	print("\n\nBye Bye !!!\nHope You Got Enough Knowledge Today :) \n\n")
	print("Written By Vishal Chaudhary & Parth Patel.\n\n")
	