import webbrowser
import pyautogui as py
import time
from datetime import datetime
meetid=input("What's the meeting id?  ")
when=input("Enter the date and time in the format : 'month/day/year:hour:min:sec' eg- 06/18/20:19:30  ")
print("waiting to join")
while True:
	now=datetime.now()
	current_time = now.strftime("%D:%H:%M")       
	if current_time==when:
		webbrowser.open("https://zoom.us/wc/join/"+meetid)
		time.sleep(3)
		py.moveTo(1054,575) #modify this line if your screen isn't big(or if the code doesn't work)
		time.sleep(2)
		py.click()
		print("Joined the meeting")
		break

