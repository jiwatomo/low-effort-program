from functools import partial
from func import *
# should_init_2 = open("banlist.json", "a")
# should_init_2.close()
filewirting()


def main():
	windw = tk.Tk()
	windw.title("Program Manager")
	windw.iconbitmap("favicon.ico")
	# Top
	top_area = tk.Frame()
	top_area.pack()
	dlabel = tk.Label(master=top_area, text="Welcome!")
	dlabel.pack(side=tk.LEFT)
	frame_kosong = tk.Frame(master=top_area, width=270, height=1)
	frame_kosong.pack()
	dlabel_mode = tk.Label(master=top_area, text="Made By Jtm")
	dlabel_mode.pack(side=tk.RIGHT)


	
	
	# Mid
	mid_area = tk.Frame(relief=tk.SUNKEN, borderwidth=4)
	mid_area.pack()
	#  dlabel_mid = tk.Label(master=mid_area, text="Mid Area")
	#  dlabel_mid.pack()
	
	# Side left
	left_side =tk.Frame(master=mid_area, borderwidth=3)
	left_side.pack(fill=tk.Y, side=tk.LEFT)
	
	btn_perform = tk.Button(master=left_side, text="Performance", command=lambda:execs_perform(dlabel_log))
	btn_perform.pack(fill=tk.X)
	btn_ExplorerON = tk.Button(master=left_side, text="ExplorerON", command=lambda:explorer_mode(dlabel_log, btn_ExplorerON))
	btn_ExplorerON.pack(fill=tk.X)
	btn_ExplorerOFF = tk.Button(master=left_side, text="ExplorerOFF", command=lambda:explorer_mode(dlabel_log, btn_ExplorerOFF))
	btn_ExplorerOFF.pack(fill=tk.X)
	
	frame_kosong_config = {
		"widtha": 15,
		"heighta": 1
	}
	
	frame_kosong = tk.Frame(master=mid_area, width=frame_kosong_config["widtha"], height=frame_kosong_config["heighta"])
	frame_kosong.pack(side=tk.LEFT,fill=tk.X)
	bottom_area = tk.Frame()
	dlabel_log = tk.Label(master=bottom_area, text="Log started")
	# Center
	center_side = tk.Frame(master=mid_area, borderwidth=3)
	center_side.pack(fill=tk.Y, side=tk.LEFT)
	
	btn_list_row1 = ["Browser", "Banlist", "AppCheck"]
	btn_list_row2 = ["Note", "Cpanel", "Sadvanced"]
	btn_list_row3 = ["Dmanager", "test8", "test9"]
	for i in range(3):
		btnframe = tk.Frame(master=center_side, relief=tk.RAISED, borderwidth=1)
		if i == 0:
			inc = 0
			btnframe.grid(row=i, column=inc)
			for j in btn_list_row1:
				btn_mid = tk.Button(master=btnframe, text=j, command=partial(mid_button_handler, j, dlabel_log, windw))
				btn_mid.pack(fill=tk.X,side=tk.LEFT)
				inc += 1
		elif i == 1:
			inc = 0
			btnframe.grid(row=i, column=inc)
			for j in btn_list_row2:
				btn_mid = tk.Button(master=btnframe, text=j, command=partial(mid_button_handler, j, dlabel_log, windw))
				btn_mid.pack(fill=tk.X,side=tk.LEFT)
				inc += 1
		elif i == 2:
			inc = 0
			btnframe.grid(row=i, column=inc)
			for j in btn_list_row3:
				btn_mid = tk.Button(master=btnframe, text=j, command=partial(mid_button_handler, j, dlabel_log, windw))
				btn_mid.pack(fill=tk.X,side=tk.LEFT)
				inc += 1
		
	frame_kosong = tk.Frame(master=mid_area, width=frame_kosong_config["widtha"], height=frame_kosong_config["heighta"])
	frame_kosong.pack(side=tk.LEFT,fill=tk.X)
	
	


	# Side right
	rigth_side = tk.Frame(master=mid_area, borderwidth=3)
	rigth_side.pack(fill=tk.Y, side=tk.RIGHT)
	
	frm_command =tk.Frame(master=rigth_side)
	frm_command.pack(fill=tk.X)
	btn_command = tk.Button(master=frm_command, text="cmd", command=lambda: rightside_changer(btn_command, frm_command))
	btn_command.pack(fill=tk.X)
	
	frm_kill =tk.Frame(master=rigth_side)
	frm_kill.pack(fill=tk.X)
	btn_kill = tk.Button(master=frm_kill, text="Kill", command=lambda: rightside_changer(btn_kill, frm_kill))
	btn_kill.pack(fill=tk.X)
	
	frm_exit =tk.Frame(master=rigth_side)
	frm_exit.pack(fill=tk.X)
	btn_exit = tk.Button(master=frm_exit, text="Exit", command=lambda: close_button(windw))
	btn_exit.pack(fill=tk.X)
	
	
	
	# Bottom
	bottom_area.pack()
	dlabel_log.pack()
	
	windw.mainloop()
	
	
	
	
if __name__ == "__main__":
	main()
	
