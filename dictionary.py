# import mouse as m ,keyboard as k
from keyboard import is_pressed
from pyperclip import paste
from PyDictionary import PyDictionary
from Tkinter import *
from pyautogui import size,center,hotkey

screenSize =size()
center_x , center_y =center((0,0,screenSize[0],screenSize[1]))

dictionary = PyDictionary()
last_query = ""
cur_query = ""
i = 1
jio = "600x250+"+str(center_x - 300)+"+"+ str(center_y -125)

print("Ready To Search Internet......")

while(1):
		if is_pressed('ctrl+e'):
			hotkey('ctrl', 'c')

			cur_query = paste()
		
			if last_query != cur_query :

				last_query = cur_query
				
				print( str(i) + " : " + cur_query)
				i += 1

				try :
					meaning = dictionary.meaning(cur_query)
				
					if "Error" in meaning.keys() or meaning =={}:
						meaning["Error"] = ["check InterNet connection \n ??? connection failure !!!"]
				except :
					meaning = dict()
					meaning["Error"] = ["Check Internet connection  ??? \n   Connection failure !!!"]
				
				 
				output = ""
				
				for key in meaning:
					output += key + " : \n " + '\n'.join(meaning[key]) + '\n'

				root = Tk()
				S = Scrollbar(root)
				T = Text(root, height=4, width=100)
				S.pack(side=RIGHT, fill=Y)
				T.pack(side=LEFT, fill=Y)
				S.config(command=T.yview)
				T.config(yscrollcommand=S.set ,font=10 ,background="#D3D3D3" )
				T.insert(END, output)
				T.config(state=DISABLED)
				root.title(cur_query)
				root.geometry(jio)

				root.mainloop()