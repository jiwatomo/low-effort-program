import tkinter as tk
from subprocess import Popen
from tkinter import filedialog
import wmi
import json
app_mode = [2]

def update_text(fr, tos):
	fr["text"] = tos

# """ def initial():

#	cmdlist = ["""set PATH="%cd%\Scripts" """, "python --version", """set PATH="%cd%\path" """]
#	for i in cmdlist:
#		Popen(i, shell=True)
# """
		
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
	try:
		Popen("del win10perf.bat", shell=True)
	except Exception as e:
		print(e)
	ready = []
	blist = open("appbanlist.txt", "r")
	handler = blist.readlines()
	for j in handler:
		ready.append(j.strip())
	blist.close()
	
	hand = open("win10perf.txt", "wt")
	hand.write(f"@echo off\n")
	for i in ready:
		hand.write(f"taskkill /F /IM {i}.exe >NUL\n")
	hand.write(f"exit\n")
	Popen("move win10perf.txt win10perf.bat >NUL", shell=True)
	hand.close()
	Popen("move win10perf.txt win10perf.bat", shell=True)
	print("Debug: filewriting exe")
		

def execs_perform(log):
	p = Popen("start win10perf.bat", shell=True)
	log["text"] = "Performance Done"
	
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



def mid_button_handler(val1, log, windw):
	if val1 == "Browser":
		csm = Popen("explorer https://google.com", shell=True)
		csm.wait()
		log['text'] = "Browser opened"
	elif val1 == "Banlist":
		print("Don't forget to saving before closing!")
		notepad_open = Popen("notepad appbanlist.txt", shell=True)
		notepad_open.wait()
		filewirting()
	elif val1 == "AppCheck":
		tasks_reading = wmi.WMI()
		tasks_handler = []
		jsmv = Popen("move banlist.txt banlist.json", shell=True)
		jsmv.wait()
		the_json = open('banlist.json')
		banlist = json.load(the_json)
		banlist["banlist"].sort()
		print("Cotto Matte")
		def refreshProcess():
			for process in tasks_reading.Win32_Process():
					tasks_handler.append(f"{process.Name}")
			tasks_handler.sort()
			
		appcheckwindw = tk.Toplevel(windw)                         #APPCHECK WINDOW!
		frame_atas =tk.Frame(master=appcheckwindw)
		frame_appcheck_left = tk.Frame(master=frame_atas)
		text_before = tk.Label(master=frame_appcheck_left, text="All Opened App")
		text_before.pack()

		listbox_before = tk.Listbox(master=frame_appcheck_left)
		
		
		def refreshData():
			listbox_before.delete(0, listbox_before.size())
			listbox_after.delete(0, listbox_after.size())
			incvar = 0
			for j in tasks_handler:
				checker = j in banlist["banlist"]
				if checker == True:
					continue
				listbox_before.insert(incvar, j)
				incvar += 1
			incvarafter = 1
			for after in banlist["banlist"]:
				listbox_after.insert(incvar, after)
				incvarafter += 1
			print(incvar)
		
		listbox_before.pack(fill=tk.BOTH, expand=True)

		frame_appcheck_right = tk.Frame(master=frame_atas)
		text_after = tk.Label(master=frame_appcheck_right, text="To be killed")
		listbox_after = tk.Listbox(master=frame_appcheck_right)
	

		def getSelected():
			selected = listbox_before.curselection()
			selectedContent = listbox_before.get(selected[0])
			banlist["banlist"].append(selectedContent)
			refreshData()
			listbox_before.delete(selected[0])

		def removeSelected():
			selected = listbox_after.curselection()
			selectedContent = listbox_after.get(selected[0])
			banlist["banlist"].remove(selectedContent)
			refreshData()
			listbox_after.delete(selected[0])
		
		def onSaving():
			the_json.close()
			Popen("del banlist.json", shell=True)
			with open("banlist.txt", "a") as outfile:
				json.dump(banlist, outfile)
			jsmv = Popen("move banlist.txt banlist.json", shell=True)
			jsmv.wait()
			appcheckwindw.destroy()
			

		frame_appcheck_mid = tk.Frame(master=frame_atas)
		btn_adding = tk.Button(master=frame_appcheck_mid, text=">>>", command=getSelected)
		btn_removing = tk.Button(master=frame_appcheck_mid, text="<<<", command=removeSelected)
		btn_adding.pack(fill=tk.X, expand=True)
		btn_removing.pack(fill=tk.X, expand=True)


		
		text_after.pack()
		listbox_after.pack(fill=tk.BOTH, expand=True)

		frame_appcheck_bottom = tk.Frame(master=appcheckwindw)
		btn_comfir = tk.Button(master=frame_appcheck_bottom, text="Save", command=onSaving)
		btn_comfir.pack(side=tk.RIGHT, padx=10, ipadx=10)
		btn_refres = tk.Button(master=frame_appcheck_bottom, text="Refresh", command=refreshProcess)
		btn_refres.pack(side=tk.RIGHT, padx=10, ipadx=10)
		frame_atas.pack(fill=tk.BOTH, expand=True)
		frame_appcheck_left.pack(side=tk.LEFT,fill=tk.BOTH, expand=True)
		frame_appcheck_mid.pack(side=tk.LEFT,fill=tk.BOTH, expand=True)
		frame_appcheck_right.pack(side=tk.RIGHT,fill=tk.BOTH, expand=True)
		frame_appcheck_bottom.pack(fill=tk.BOTH, ipadx=5, ipady=5, expand=True)
		refreshProcess()
		refreshData()
		appcheckwindw.mainloop()
	elif val1 == "Cpanel":
		print("Done")
		log["text"] =" HEllo"
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