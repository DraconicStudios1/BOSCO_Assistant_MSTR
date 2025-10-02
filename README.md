BOSCO Assistant ALPHA

Currently BOSCO doesn't stand for anything, and only contains basic functions to tell your local time, date and the time until a set of specified hours/minutes

IF you change the time until timeset, you MUST use 24 hour timestamps. Nothing else works with the math.

You CANNOT use datetime.datetime.strftime string sets for the math. Trust me, I tried.

BOSCO is built using the Tkinter Python application backbone, and as such, looks like a Windows 95 application. If anyone knows how to fix that and actually use images for stuff, please contact me at: bluecolt08@gmail.com, Discord: dracstudios.

Currently BOSCO has been developed and tested STRICTLY on Windows 11 devices, I have no clue if it works on any forms of Linux, earlier Windows versions, or MacOS. You are welcome to branch this repo and try to convert it if you so please.

BE CAREFUL, AND FOR THE LOVE OF GOD DONT USE MY CODE TO LEARN PYTHON. I JUST STARTED THIS SHIT.

# DEVLOG 1

I have been trying to make the time_remaining value constantly update each second, but datetime.now() only runs once each time I run the application, and I have no clue why.
I will be trying to make a seperate function to run the time and gather the current date and time outside of the existing function, but I have no way of making sure that this will work. Alpha V0.1.0 is under way.

# DEVLOG 2

IT WORKS! I GOT THE TIME UPDATING TO WORK! THAT TOOK ME SO LONG OH MY GOD!
I will get it to update every second now.

# CHANGELOG

You can find version changes below.

# ALPHA V0.0.2

-Added ability to drag window

-Added Weekend/Day Off message

# ALPHA V0.0.3

-Fixed issue where weekend message showed on weekdays

-Added Format Example in ExampleScheduleChart.txt for 24hr clock

-Renamed PythonApp1.py to BOSCO_ALPHA_V-0-0-3.py

# ALPHA V0.1.0 *MAJOR UPDATE*

-Added ability to update the time_remaining value

-Fixed issue where old debug prints were still active, the current one is active purposely

-Fixed issue where time calculations were not different on the defined day with a different schedule
