import tkinter as tk
from func import *

# Global Variable
app_mode = 0


def main():
	windw = tk.Tk()
	windw.title("Menu")
	
	# Top
	top_area = tk.Frame()
	top_area.pack()
	dlabel = tk.Label(master=top_area, text="Welcome!, select the mode first")
	dlabel.pack(side=tk.LEFT)
	tfr = tk.Frame(master=top_area, width="200")
	tfr.pack(side=tk.LEFT, fill=tk.X)
	btn_mode = tk.Button(master=top_area, text="Change mode")
	btn_mode.pack(side=tk.RIGHT)
	
	
	# Mid
	mid_area = tk.Frame(relief=tk.SUNKEN)
	mid_area.pack()
	#  dlabel_mid = tk.Label(master=mid_area, text="Mid Area")
	#  dlabel_mid.pack()
	# Side left
	left_side =tk.Frame(master=mid_area)
	left_side.pack(fill=tk.Y, side=tk.LEFT)
	btn_perform = tk.Button(master=left_side, text="Performance")
	btn_perform.pack(fill=tk.X)
	btn_ExplorerON = tk.Button(master=left_side, text="ExplorerON")
	btn_ExplorerON.pack(fill=tk.X)
	btn_ExplorerOFF = tk.Button(master=left_side, text="ExplorerOFF")
	btn_ExplorerOFF.pack(fill=tk.X)
	
	tfr1 = tk.Frame(master=mid_area, width=200)
	tfr1.pack(fill=tk.Y, side=tk.LEFT)
	
	# Center
	center_side = tk.Frame(master=mid_area)
	center_side.pack(fill=tk.Y, side=tk.LEFT)
	
	btn_list_row1 = ["test1", "test2", "test3"]
	btn_list_row2 = ["test4", "test5", "test6"]
	btn_list_row3 = ["test7", "test8", "test9"]
	for i in range(3):
		if i == 0:
			inc = 0
			for j in btn_list_row1:
				btnframe = tk.Frame(master=center_side, relief=tk.RAISED, borderwidth=1)
				btnframe.grid(row=i, column=inc)
				btn_mid = tk.Button(master=btnframe, text=j, command=lambda: mid_button_handler(j))
				btn_mid.pack()
				inc += 1
		elif i == 1:
			inc = 0
			for j in btn_list_row2:
				btnframe = tk.Frame(master=center_side, borderwidth=1)
				btnframe.grid(row=i, column=inc)
				btn_mid = tk.Button(master=btnframe, text=j, command=lambda: mid_button_handler(j))
				btn_mid.pack()
				inc += 1
		elif i == 2:
			inc = 0
			for j in btn_list_row3:
				btnframe = tk.Frame(master=center_side, borderwidth=1)
				btnframe.grid(row=i, column=inc)
				btn_mid = tk.Button(master=btnframe, text=j, command=lambda: mid_button_handler(j))
				btn_mid.pack()
				inc += 1
				
	# Side right
	right_side = tk.Frame(master=mid_area)
	right_side.pack(fill=tk.Y, side=tk.LEFT)
	
	
	# Bottom
	bottom_area = tk.Frame()
	bottom_area.pack()
	dlabel_bottom = tk.Label(master=bottom_area, text="Bottom Area")
	dlabel_bottom.pack()
	
	
	windw.mainloop()
	
	
	
	
if __name__ == "__main__":
	main()
	
