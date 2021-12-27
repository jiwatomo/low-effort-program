import tkinter as tk
def update_text(fr, to):
	print("ok")
	
def change_modes(val1, val2):
	val1["text"] = "Enjoy!"	
	if val2["text"] == "win10":
		app_mode = 2
		val2["text"] = "win7"
	else:
		app_mode = 1
		val2["text"] = "win10"
		
def rightside_changer(val1, val2):
	btext = val1["text"]
	val1.pack_forget()
	nentry = tk.Entry(master=val2)
	nentry.pack(fill=tk.X, side=tk.LEFT)
	nbtn = tk.Button(master=val2, text=btext, command=lambda: rightside_handler(nentry, val1, nentry, nbtn))
	nbtn.pack(fill=tk.X, side=tk.LEFT)
	
def rightside_handler(val1, val2, val3, val4):
	hand = val1.get()
	
	
	
	val3.pack_forget()
	val4.pack_forget()
	val2.pack(fill=tk.X)
	
def mid_button_handler(val1):
	if val1 == "test1":
		print("Done")
	elif val1 == "test2":
		print("Done")
	elif val1 == "test3":
		print("Done")
	elif val1 == "test4":
		print("Done")
	elif val1 == "test5":
		print("Done")
	elif val1 == "test6":
		print("Done")
	elif val1 == "test7":
		print("Done")
	elif val1 == "test8":
		print("Done")
	elif val1 == "test9":
		print("Done")
