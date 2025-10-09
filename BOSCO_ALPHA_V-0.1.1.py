from datetime import datetime
import tkinter as tk
import json

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

    #print(current_datetime)
    if current_datetime.date().weekday() == 2:
            if instanceNum < MaxArrayWed:
                for int in WedTimesH:
                    target_timeB = datetime(cur_year, cur_month, cur_day, hour=WedTimesH[instanceNum], minute=WedTimesM[instanceNum])
                    print(instanceNum)
                    if atime <= target_timeA:
                        time_remaining = target_timeA - atime
                    if atime >= target_timeA:
                        instanceNum += 1
                        time_remaining = target_timeA - atime
                    print(time_remaining)
                    break

                
    else:
            if instanceNum < MaxArrayMTTF:
                for int in MTTF_TimesH:
                    target_timeA = datetime(cur_year, cur_month, cur_day, hour=MTTF_TimesH[instanceNum], minute=MTTF_TimesM[instanceNum])
                    print(instanceNum)
                    if atime <= target_timeA:
                        time_remaining = target_timeA - atime
                    if atime >= target_timeA:
                        instanceNum += 1
                        time_remaining = target_timeA - atime
                    print(time_remaining)
                    break

    # Pack the label into the window
    if updatedlol == False:
        labelERRIND = tk.Label(root, text="(KEEP CYCLING UNTIL IT DOESN'T THROW A NEGATIVE DAY)",
                     font=("Red October", 12), 
                     padx=10, pady=0, 
                     bg="black", # Background color
                     fg="darkgreen")
        label5 = tk.Label(root, text=f"YOUR CURRENT CLASS ENDS IN {time_remaining}", 
                     font=("Red October", 12), 
                     padx=10, pady=0, 
                     bg="black", # Background color
                     fg="darkgreen") # Foreground (text) color
        if atime >= target_timeA:
            labelERRIND.pack(padx=20, pady=5)
        label5.pack(padx=20, pady=0)
        updatedlol = True
    else:
        label5.destroy()
        labelERRIND.destroy()
        updatedlol = False
    print(f"Updater Cycled and Packed = {updatedlol}")

def create_app():

    global WedSchedule
    global MTTF_Schedule

    root.overrideredirect(True)  # Remove default title bar
    # Custom title bar frame
    title_bar = tk.Frame(root, bg="darkgreen", relief="raised", bd=2)
    title_bar.pack(expand=True, fill="x")
    # Title label
    title_label = tk.Label(title_bar, text="BOSCO ALPHA V0.1.1", bg="darkgreen", fg="black", font=("Red October", 12))
    title_label.pack(side="left", padx=5)
    root.configure(bg='black')
    # Close Button
    def close_app():
        root.destroy()
    close_button = tk.Button(title_bar, text="X", bg='darkgreen', fg='black', command=close_app)
    close_button.pack(side="right", padx=5)
    global current_datetime
    date = current_datetime.strftime("%A, %Y/%m/%d")
    time = current_datetime.strftime("%I:%M%p")
    # Create a label widget to display the text
    label = tk.Label(root, text="HELLO SIR.", 
                     font=("Red October", 12), 
                     padx=10, pady=0, 
                     bg="black", # Background color
                     fg="darkgreen") # Foreground (text) color
    label1 = tk.Label(root, text=f"THE TIME IS {time}", 
                     font=("Red October", 12), 
                     padx=10, pady=0, 
                     bg="black", # Background color
                     fg="darkgreen") # Foreground (text) color
    label2 = tk.Label(root, text=f"THE DATE IS {date}, IN Y M D FORMAT,", 
                     font=("Red October", 12), 
                     padx=10, pady=0, 
                     bg="black", # Background color
                     fg="darkgreen") # Foreground (text) color
    label3 = tk.Label(root, text="YOUR BELL SCHEDULE IS", 
                     font=("Red October", 12), 
                     padx=10, pady=0, 
                     bg="black", # Background color
                     fg="darkgreen") # Foreground (text) color
    label4A = tk.Label(root, text=MTTF_Schedule
, 
                     font=("Red October", 12), 
                     padx=10, pady=0, 
                     bg="black", # Background color
                     fg="darkgreen") # Foreground (text) color
    label4B = tk.Label(root, text=WedSchedule, 
                     font=("Red October", 12), 
                     padx=10, pady=0, 
                     bg="black", # Background color
                     fg="darkgreen") # Foreground (text) color
    label4C = tk.Label(root, text="NO SCHEDULE TODAY, YOUR WEEKEND HATH ARRIVED.",
                     font=("Red October", 12), 
                     padx=10, pady=0, 
                     bg="black", # Background color
                     fg="darkgreen")
    label.pack(padx=20, pady=0)
    label1.pack(padx=20, pady=0)
    label2.pack(padx=20, pady=0)
    label3.pack(padx=20, pady=0)
    if current_datetime.date().weekday() == 4 or current_datetime.date().weekday() == 5:
        label4C.pack(padx=20, pady=0)
    else:
        if current_datetime.date().weekday() == 2:
            label4B.pack(padx=20, pady=0)
        else:
            label4A.pack(padx=20, pady=0)
    updooter = tk.Button(root, text="UPDATE",
                         font=("Red October", 12),
                         padx=10, pady=0,
                         bg="darkgreen", # Background color
                         fg="black",
                         command=update_cur_datetime)
    updooter.pack(padx=20, pady=0) 
    x_axis = None
    y_axis = None
    # bind title bar motion to the move window function
    xwin = root.winfo_x()
    ywin = root.winfo_y()
    def get_pos(event):
        global xwin
        global ywin
        xwin = xwin - event.x
        ywin = ywin - event.y
    def move_window(event):
        root.geometry(f'+{event.x_root - xwin}+{event.y_root - ywin}')
    def change_on_hovering(event):
        close_button['bg'] = 'red'
    def change_on_hovering1(event):
        updooter['bg'] = 'green'
    def return_to_normal_state(event):
       close_button['bg'] = 'darkgreen'
    def return_to_normal_state1(event):
       updooter['bg'] = 'darkgreen'
    def change_text_on_button(event):
        global changed
        if changed == False:
            updooter['text'] = "RESET"
            changed = True
        else:
            updooter['text'] = "UPDATE"
            changed = False
    title_bar.bind("<B1-Motion>", move_window)
    title_bar.bind("<Button-1>", get_pos)
    title_label.bind("<B1-Motion>", move_window)
    title_label.bind("<Button-1>", get_pos)
    close_button.bind('<Enter>', change_on_hovering)
    close_button.bind('<Leave>', return_to_normal_state)
    updooter.bind('<Enter>', change_on_hovering1)
    updooter.bind('<Leave>', return_to_normal_state1)
    updooter.bind('<Button-1>', change_text_on_button)
    # Start the Tkinter event loop
    root.mainloop()
if __name__ == "__main__":
    create_app()
