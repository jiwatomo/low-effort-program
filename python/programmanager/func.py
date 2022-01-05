import tkinter as tk
import webbrowser
from subprocess import Popen
from tkinter import filedialog
app_mode = [0]

def update_text(fr, tos):
	fr["text"] = tos

# """ def initial():

#	cmdlist = ["""set PATH="%cd%\Scripts" """, "python --version", """set PATH="%cd%\path" """]
#	for i in cmdlist:
#		Popen(i, shell=True)
# """
def change_modes(val1, val2):
	val1["text"] = "Enjoy!"	
	if val2["text"] == "win10":
		app_mode[0] = 1
		val2["text"] = "win7"
	else:
		app_mode[0] = 2
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

def filewirting():
	ready = []
	blist = open("appbanlist.txt", "r")
	handler = blist.readlines()
	for j in handler:
		ready.append(j.strip())
	blist.close()
	if app_mode[0] == 1:
		hand = open("win7perf.bat", "w")
		for i in ready:
			hand.write(f"tskill {i}.exe\n")
		hand.close()
		
	elif app_mode[0] == 2:
		hand = open("win10perf.bat", "w")
		for i in ready:
			hand.write(f"taskkill /F /IM {i}.exe\n")
		hand.close()
		

def execs_perform(log):
	if app_mode[0] == 1:
		filewirting()
		p = Popen("win7perf.bat")
		stdout, stderr = p.communicate()

		log["text"] = "Performance Done"
		Popen("del win7perf.bat", shell=True)
	elif app_mode[0] == 2:
		filewirting()
		p = Popen("win10perf.bat")
		stdout, stderr = p.communicate()

		log["text"] = "Performance Done"
		Popen("del win10perf.bat", shell=True)
	else:
		log["text"] = "select mode first!"
	
def explorer_mode(log, md):

	if md["text"] == "ExplorerOFF":
		print("ok")
		if app_mode[0] == 1:
			Popen("tskill explorer.exe", shell=True)
			log["text"] = "Turn off explrer done" 
		elif app_mode[0] == 2:
			Popen("taskkill /F /IM explorer.exe", shell=True)
			log["text"] = "Turn off explrer done" 
	elif md["text"] == "ExplorerON":
		Popen("start explorer.exe", shell=True)
		log["text"] = "Turn on explrer done" 



def mid_button_handler(val1):
	if val1 == "test1":
		print(app_mode)
	elif val1 == "test2":
		Popen("echo %cd%", shell=True)
	elif val1 == "test3":
		print("Done")
	elif val1 == "test4":
		print("Done")
	elif val1 == "test5":
		print("Done")
	elif val1 == "test6":
		print("Done")
	elif val1 == "test7":
		status_read = open("status.txt", "x")
		
		status_read.close()
	elif val1 == "test8":
		print("Done")
	elif val1 == "test9":
		print("Done")

def close_button(windw):
	windw.destroy()