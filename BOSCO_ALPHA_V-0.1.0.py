from datetime import datetime
import time
import tkinter as tk

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
                     bg="black", # Background color
                     fg="white") # Foreground (text) color

changed = False

def update_cur_datetime():
    #time values
    global updatedlol
    global label5
    global current_datetime
    global cur_year
    global cur_month
    global cur_day
    global cur_hour
    global cur_min
    atime = current_datetime.today()
    global time_remaining
    atime = datetime.now()
    #print(current_datetime)

    if current_datetime.date().weekday() == 2:
            target_timeB1 = datetime(cur_year, cur_month, cur_day, hour=9, minute=25)
            target_timeB3 = datetime(cur_year, cur_month, cur_day, hour=11, minute=10)
            target_timeB4 = datetime(cur_year, cur_month, cur_day, hour=12, minute=00)
            target_timeBL = datetime(cur_year, cur_month, cur_day, hour=12, minute=45)
            target_timeB5 = datetime(cur_year, cur_month, cur_day, hour=13, minute=30)
            target_timeB6 = datetime(cur_year, cur_month, cur_day, hour=14, minute=20)
            target_timeB7 = datetime(cur_year, cur_month, cur_day, hour=15, minute=7)


            if atime < target_timeB1:
                time_remaining = target_timeB1 - atime
            if atime > target_timeB1:
                time_remaining = target_timeB3 - atime
            if atime > target_timeB3:
                time_remaining = target_timeB4 - atime
            if atime > target_timeB4:
                time_remaining = target_timeBL - atime
            if atime > target_timeBL:
                time_remaining = target_timeB5 - atime
            if atime > target_timeB5:
                time_remaining = target_timeB6 - atime
            if atime > target_timeB6:
                time_remaining = target_timeB7 - atime
            if atime > target_timeB7:
                time_remaining = "SCHOOLS OUT"
    else:
            target_timeA1 = datetime(cur_year, cur_month, cur_day, hour=9, minute=25)
            target_timeA3 = datetime(cur_year, cur_month, cur_day, hour=10, minute=45)
            target_timeA4 = datetime(cur_year, cur_month, cur_day, hour=11, minute=41)
            target_timeAL = datetime(cur_year, cur_month, cur_day, hour=12, minute=21)
            target_timeA5 = datetime(cur_year, cur_month, cur_day, hour=13, minute=13)
            target_timeA6 = datetime(cur_year, cur_month, cur_day, hour=14, minute=10)
            target_timeA7 = datetime(cur_year, cur_month, cur_day, hour=15, minute=7)


            if atime < target_timeA1:
               time_remaining = target_timeA1 - atime
            if atime > target_timeA1:
               time_remaining = target_timeA3 - atime
            if atime > target_timeA3:
               time_remaining = target_timeA4 - atime
            if atime > target_timeA4:
               time_remaining = target_timeAL - atime
            if atime > target_timeAL:
               time_remaining = target_timeA5 - atime
            if atime > target_timeA5:
               time_remaining = target_timeA6 - atime
            if atime > target_timeA6:
               time_remaining = target_timeA7 - atime
            if atime > target_timeA7:
               time_remaining = "SCHOOLS OUT"

    # Pack the label into the window
    if updatedlol == False:
        label5 = tk.Label(root, text=f"YOUR CURRENT CLASS ENDS IN {time_remaining}", 
                     font=("Red October", 12), 
                     padx=10, pady=0, 
                     bg="black", # Background color
                     fg="white") # Foreground (text) color
        label5.pack(padx=20, pady=0)
        updatedlol = True
    else:
        label5.destroy()
        updatedlol = False

    print(f"Updater Cycled and Packed = {updatedlol}")

def create_text_box_app():
    root.overrideredirect(True)  # Remove default title bar

    # Custom title bar frame
    title_bar = tk.Frame(root, bg="darkgreen", relief="raised", bd=2)
    title_bar.pack(expand=True, fill="x")

    # Title label
    title_label = tk.Label(title_bar, text="BOSCO ALPHA V0.1.0", bg="darkgreen", fg="black", font=("Red October", 12))
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
        
        #root.after(1000, update)

            # Create a label widget to display the text
    label = tk.Label(root, text="HELLO SIR.", 
                     font=("Red October", 12), 
                     padx=10, pady=0, 
                     bg="black", # Background color
                     fg="white") # Foreground (text) color

    label1 = tk.Label(root, text=f"THE TIME IS {time}", 
                     font=("Red October", 12), 
                     padx=10, pady=0, 
                     bg="black", # Background color
                     fg="white") # Foreground (text) color

    label2 = tk.Label(root, text=f"THE DATE IS {date}, IN Y M D FORMAT,", 
                     font=("Red October", 12), 
                     padx=10, pady=0, 
                     bg="black", # Background color
                     fg="white") # Foreground (text) color
    label3 = tk.Label(root, text="YOUR BELL SCHEDULE IS", 
                     font=("Red October", 12), 
                     padx=10, pady=0, 
                     bg="black", # Background color
                     fg="white") # Foreground (text) color


    label4A = tk.Label(root, text="""1  9:25AM
3  10:44AM
4  11:41AM
L  12:21AM
5  1:13PM
6  2:10PM
7  3:07PM
""", 
                     font=("Red October", 12), 
                     padx=10, pady=0, 
                     bg="black", # Background color
                     fg="white") # Foreground (text) color

    label4B = tk.Label(root, text="""1  9:25AM
3  11:10AM
4  12:00AM
L  12:45AM
5  1:30PM
6  2:20PM
7  3:07PM
""", 
                     font=("Red October", 12), 
                     padx=10, pady=0, 
                     bg="black", # Background color
                     fg="white") # Foreground (text) color

    label4C = tk.Label(root, text="NO SCHEDULE TODAY, YOUR WEEKEND HATH ARRIVED.",
                     font=("Red October", 12), 
                     padx=10, pady=0, 
                     bg="black", # Background color
                     fg="white")

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
    create_text_box_app()
