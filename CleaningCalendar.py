import datetime
import calendar
#Based on https://homesteadwifey.files.wordpress.com/2014/03/c850a-cleaningpic.png?w=640

daynumber = datetime.datetime.now().day
weeknumber = (daynumber - 1) // 7 + 1
weekday = datetime.date.today().strftime("%A")
month = datetime.date.today().strftime("%B")

#print daynumber
#print weeknumber
#print weekday
#print month

dailychore = "De-Clutter Living Spaces, Wash up & Wipe Kitchen surfaces"

if weekday=="Monday":
	chore = "Hoover Main Spaces"
if weekday=="Tuesday":
	chore = "WOMChore"
if weekday=="Wednesday":
	chore = "Dust"
if weekday=="Thursday":
	chore = "Clean Bathrooms"
if weekday=="Friday":
	chore = "Washing"
if weekday=="Saturday":
	chore = "Catch-up"
if weekday=="Sunday":
	chore = "Clear out Fridge"	
	
if chore == "WOMChore":
	if weeknumber == 1:
		chore = "Clean Appliances"
	elif weeknumber == 2:
		chore = "Clean Furniture/Cabinets"
	elif weeknumber == 3:
		chore = "Wash Rugs etc"
	elif weeknumber == 4:
		chore = "MOYChore"
	else:
		chore = "Day Off!"

if chore == "MOYChore":
	if month=="January ":
		chore = "Wipe inside of Kitchen Cabinets and Drawers"
	elif month=="February":
		chore = "Organise Cupboards and Pantry"
	elif month=="March":
		chore = "Wipe inside of Bathroom Cabinets and Drawers"
	elif month=="April":
		chore = "Garage"
	elif month=="May":
		chore = "Outside of the House"
	elif month=="June":
		chore = "Wash Walls, Mouldings and Doors"
	elif month=="July":
		chore = "Shampoo Carpets"
	elif month=="August":
		chore = "Windows/Window Sills"
	elif month=="September":
		chore = "Blinds and Window Treatments"
	elif month=="October":
		chore = "Garage"
	elif month=="November":
		chore = "Move Fridge/Oven"
	elif month=="December":
		chore = "Wash Walls, Mouldings and Doors"	
	else:
		print "Date not recognised"
	
print dailychore
print chore
