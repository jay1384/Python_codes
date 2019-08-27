import schedule
import time
import xlrd 
import os
from datetime import date
import sys
import webbrowser   
 
#urL='https://clockify.me/tracker'
urL='https://new.timecamp.com'

chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path),1)
webbrowser.get('chrome').open_new_tab(urL)

def job():
	#os.system("toggle.fullscreen")
	print ("Job and timer are executing good.")
	webbrowser.get('chrome').open_new_tab(urL)
	"""
	today = date.today()
	d3 = today.strftime("%d/%m/%y")
	print("Today's date:", d3)
	#loc = ('Desktop\Work done.xlsx')
	#wb = xlrd.open_workbook(loc) 

	#file = "C:\Users\CAGYF3W\Downloads\008_Projects\Work_done.xlsx"
	#os.startfile(file)
	
	User_input_reminder = 'r'	
	while(User_input_reminder == 'r') :
		User_input_reminder = raw_input("Press 'y' to update work-done in last hour or press 'r' to remind after 5 min : ")
		if(User_input_reminder == 'y'):
			with open(r"C:\Users\CAGYF3W\Downloads\008_Projects\Work_done.txt", "a") as myfile:
				User_input_data = raw_input("Write data as work-done in last hour : ")
				myfile.write(User_input_data)
				myfile.close()	
		if(User_input_reminder == 'r') :
			time.sleep(60*1)
				
	"""	
	return

#schedule.every(10).seconds.do(job)
#schedule.every(10).minutes.do(job)
#schedule.every().hour.do(job)
#schedule.every().day.at("10:30").do(job)	
#schedule.every().day.at("15:14").do(job)


schedule.every().day.at("08:02").do(job)
schedule.every().day.at("09:02").do(job)
schedule.every().day.at("10:02").do(job)
schedule.every().day.at("11:02").do(job)
schedule.every().day.at("12:02").do(job)
schedule.every().day.at("13:02").do(job)
schedule.every().day.at("14:02").do(job)
schedule.every().day.at("15:02").do(job)
schedule.every().day.at("16:02").do(job)
schedule.every().day.at("17:02").do(job)
schedule.every().day.at("18:02").do(job)
schedule.every().day.at("19:02").do(job)
schedule.every().day.at("20:02").do(job)
schedule.every().day.at("21:02").do(job)
schedule.every().day.at("22:02").do(job)
schedule.every().day.at("23:02").do(job)
schedule.every().day.at("00:02").do(job)



try:
	while True:
		schedule.run_pending()
except KeyboardInterrupt:
	print("Exiting - Thank you")
	pass
