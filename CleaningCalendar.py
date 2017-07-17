import datetime
from pushbullet import Pushbullet

#import calendar
#Based on https://homesteadwifey.files.wordpress.com/2014/03/c850a-cleaningpic.png?w=640

api_key = open('/home/pi/Pushbulletkey.config', 'r').read()
print api_key
pb = Pushbullet(api_key) 

daynumber = datetime.datetime.now().day #Day Number of Month
weeknumber = (daynumber - 1) // 7 + 1 #Week number of the Month 1-5
weekday = datetime.date.today().strftime("%A") #Weekday e.g.Tuesday
month = datetime.date.today().strftime("%B") #Month e.g. June

##Debugging purposes##
#print daynumber
#print weeknumber
#print weekday
#print month

#Daily Chore to do everyday
dailychore = "De-Clutter Living Spaces, Wash up & Wipe Kitchen surfaces"

if weekday=="Monday":
	chore = "Hoover main areas"
if weekday=="Tuesday":
	chore = "Washing"
if weekday=="Wednesday":
	chore = "Dust"
if weekday=="Thursday":
	chore = "Clean Bathrooms"
if weekday=="Friday":
	chore = "Clear out Fridge"
if weekday=="Saturday":
	chore = "Catch-up"
if weekday=="Sunday":
	chore = "WOMChore" #Week of the month chore
	
if chore == "WOMChore": #Looks at week number for the Monthly Chore
	if weeknumber == 1:
		chore = "Clean Appliances"
	elif weeknumber == 2:
		chore = "Clean Furniture/Cabinets"
	elif weeknumber == 3:
		chore = "Wash Rugs etc"
	elif weeknumber == 4:
		chore = "MOYChore" #Month of the year Chore - Once per year
	else:
		chore = "Day Off!" #Last Sunday of the month off

if chore == "MOYChore": #Looks at the Month
	if month=="January":
		chore = "Wipe inside of Kitchen Cabinets and Drawers"
	elif month=="February":
		chore = "Organise Cupboards and Pantry"
	elif month=="March":
		chore = "Wipe inside of Bathroom Cabinets and Drawers"
	elif month=="April":
		chore = "Clear Garage"
	elif month=="May":
		chore = "Outside of the House"
	elif month=="June":
		chore = "Wash Walls, Mouldings and Doors"
	elif month=="July":
		chore = "Clean/Vax Carpets"
	elif month=="August":
		chore = "Garden"
	elif month=="September":
		chore = "Windows/Window Sills"
	elif month=="October":
		chore = "Clear Garage"
	elif month=="November":
		chore = "Move Fridge/Oven"
	elif month=="December":
		chore = "Wash Walls, Mouldings and Doors"	
	
print dailychore
print chore
push = pb.push_note("This is the title", "This is the body")
