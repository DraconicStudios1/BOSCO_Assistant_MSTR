from datetime import datetime
import tkinter as tk
import json
from PIL import Image, ImageTk

with open('ScheduleData.json', 'r') as f:
	values = json.load(f)
WedTimesH = values["WedTimesH"]
WedTimesM = values["WedTimesM"]
MTTF_TimesH = values["MTTF-TimesH"]
MTTF_TimesM = values["MTTF-TimesM"]
MaxArrayWed = len(values["WedTimesH"])
MaxArrayMTTF = len(values["MTTF-TimesH"])
WedSchedule = values["WedSchedule"]
MTTF_Schedule = values["MTTF-Schedule"]
lasttimestamp = ""
instanceNum = 0
root = tk.Tk()
updatedlol = False
current_datetime = datetime.now()
cur_year = current_datetime.year
cur_month = current_datetime.month
cur_day = current_datetime.day
cur_hour = current_datetime.hour
cur_min = current_datetime.minute
time_remaining = datetime(cur_year, cur_month, cur_day, cur_hour, cur_min)
label5 = tk.Label(root, text=f"YOUR CURRENT CLASS ENDS IN {time_remaining}", 
					 font=("Red October", 12), 
					 padx=10, pady=0, 
					 bg="black",
					 fg="white")
labelERRIND = tk.Label(root, text=f"YOUR CURRENT CLASS ENDS IN {time_remaining}", 
					 font=("Red October", 12), 
					 padx=10, pady=0, 
					 bg="black",
					 fg="white")
changed = False
target_timeB = datetime(cur_year, cur_month, cur_day, hour=WedTimesH[instanceNum], minute=WedTimesM[instanceNum])
target_timeA = datetime(cur_year, cur_month, cur_day, hour=MTTF_TimesH[instanceNum], minute=MTTF_TimesM[instanceNum])

def update_cur_datetime():
	#time values
	global updatedlol
	global label5
	global labelERRIND
	global current_datetime
	global cur_year
	global cur_month
	global cur_day
	global cur_hour
	global cur_min
	global time_remaining
	atime = datetime.now()
	global WedTimesH
	global WedTimesM
	global MTTF_TimesH
	global MTTF_TimesM
	global lasttimestamp
	global MaxArrayWed
	global MaxArrayMTTF
	global instanceNum
	target_timeB = datetime(cur_year, cur_month, cur_day, hour=WedTimesH[instanceNum], minute=WedTimesM[instanceNum])
	target_timeA = datetime(cur_year, cur_month, cur_day, hour=MTTF_TimesH[instanceNum], minute=MTTF_TimesM[instanceNum])
	if current_datetime.date().weekday() == 2:
			if instanceNum < MaxArrayWed:
				for int in WedTimesH:
					print(instanceNum)
					if atime <= target_timeB:
						time_remaining = target_timeB - atime
					if atime >= target_timeB:
						instanceNum += 1
						time_remaining = target_timeB - atime
					print(time_remaining)
					break	
	else:
			if instanceNum < MaxArrayMTTF:
				for int in MTTF_TimesH:
					print(instanceNum)
					if atime <= target_timeA:
						time_remaining = target_timeA - atime
					if atime >= target_timeA:
						instanceNum += 1
						time_remaining = target_timeA - atime
					print(time_remaining)
					break
	if updatedlol == False:
		labelERRIND = tk.Label(root, text="(KEEP CYCLING UNTIL IT DOESN'T THROW A NEGATIVE DAY)",
					 font=("Red October", 12), 
					 padx=10, pady=0, 
					 bg="black",
					 fg="darkgreen")
		label5 = tk.Label(root, text=f"YOUR CURRENT CLASS ENDS IN {time_remaining}", 
					 font=("Red October", 12), 
					 padx=10, pady=0, 
					 bg="black",
					 fg="darkgreen")
		if atime >= target_timeA:
			labelERRIND.grid(column=0, row=9)
		label5.grid(column=0, row=10)
		updatedlol = True
	else:
		label5.destroy()
		labelERRIND.destroy()
		updatedlol = False
	print(f"Updater Cycled and Packed = {updatedlol}")

def create_app():
	global WedSchedule
	global MTTF_Schedule
	tk_image = ImageTk.PhotoImage(Image.open("AppBG.png"))
	tk_image1 = ImageTk.PhotoImage(Image.open("CloseButton.png"))
	tk_image2A = ImageTk.PhotoImage(Image.open("UpdateButton.png"))
	tk_image2B = ImageTk.PhotoImage(Image.open("ResetButton.png"))
	tk_image3 = ImageTk.PhotoImage(Image.open("BackgroundImage.png"))
	background_label = tk.Label(root, image=tk_image3, bg='black')
	background_label.place(x=0, y=40)
	root.overrideredirect(True)
	title_bar = tk.Frame(root, bg="black", relief="flat")
	title_bar.grid(column=0, row=0, padx=0, pady=0)
	title_label = tk.Label(title_bar, bg="black", fg="darkgreen", image=tk_image)
	title_label.grid(column=0, row=0)
	root.configure(bg='black', width=720, height=480)
	def close_app():
		root.destroy()
	close_button = tk.Button(title_bar, image=tk_image1, bg='black', command=close_app, relief="flat")
	close_button.place(x=690, y=10, width=20, height=20)
	global current_datetime
	date = current_datetime.strftime("%A, %Y/%m/%d")
	time = current_datetime.strftime("%I:%M %p")
	label = tk.Label(root, text="HELLO SIR.", 
					 font=("Red October", 12), 
					 padx=10, pady=0, 
					 bg="black", 
					 fg="darkgreen") 
	label1 = tk.Label(root, text=f"THE TIME IS {time}", 
					 font=("Red October", 12), 
					 padx=10, pady=0, 
					 bg="black", 
					 fg="darkgreen") 
	label2 = tk.Label(root, text=f"THE DATE IS {date}, IN Y M D FORMAT,", 
					 font=("Red October", 12), 
					 padx=10, pady=0, 
					 bg="black", 
					 fg="darkgreen") 
	label3 = tk.Label(root, text="YOUR BELL SCHEDULE IS", 
					 font=("Red October", 12), 
					 padx=10, pady=0, 
					 bg="black", 
					 fg="darkgreen") 
	label4A = tk.Label(root, text=MTTF_Schedule
, 					 font=("Red October", 12), 
					 padx=10, pady=0, 
					 bg="black", 
					 fg="darkgreen") 
	label4B = tk.Label(root, text=WedSchedule, 
					 font=("Red October", 12), 
					 padx=10, pady=0, 
					 bg="black", 
					 fg="darkgreen") 
	label4C = tk.Label(root, text="NO SCHEDULE TODAY, YOUR WEEKEND HATH ARRIVED.",
					 font=("Red October", 12), 
					 padx=10, pady=0, 
					 bg="black", 
					 fg="darkgreen")
	label.grid(column=0, row=2)
	label1.grid(column=0, row=3)
	label2.grid(column=0, row=4)
	label3.grid(column=0, row=5)
	if current_datetime.date().weekday() == 5 or current_datetime.date().weekday() == 6:
		label4C.grid(column=0, row=6)
	else:
		if current_datetime.date().weekday() == 2:
			label4B.grid(column=0, row=6)
		else:
			label4A.grid(column=0, row=6)
	gapper = tk.Label(root, text="""
	
	
	
	
	
	

	
	""", bg='black', fg='black')
	gapper.grid(column=0, row=7)
	updooter = tk.Button(root, image=tk_image2A,
						 padx=10, pady=0,
						 bg="black",
						 fg="black",
						 relief="flat",
						 command=update_cur_datetime)
	updooter.grid(column=0, row=8)
	x_axis = None
	y_axis = None
	xwin = root.winfo_x()
	ywin = root.winfo_y()
	def get_pos(event):
		global xwin
		global ywin
		xwin = xwin - event.x
		ywin = ywin - event.y
	def move_window(event):
		root.geometry(f'+{event.x_root - xwin}+{event.y_root - ywin}')
	def change_text_on_button(event):
		global changed
		if changed == False:
			updooter['image'] = tk_image2B
			changed = True
		else:
			updooter['image'] = tk_image2A
			changed = False
	title_bar.bind("<B1-Motion>", move_window)
	title_bar.bind("<Button-1>", get_pos)
	title_label.bind("<B1-Motion>", move_window)
	title_label.bind("<Button-1>", get_pos)
	updooter.bind('<Button-1>', change_text_on_button)
	root.mainloop()
if __name__ == "__main__":
	create_app()
