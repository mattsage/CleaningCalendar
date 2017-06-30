import datetime
import calendar

daynumber = datetime.datetime.now().day
weeknumber = (daynumber - 1) // 7 + 1
weekday = datetime.date.today().strftime("%A")
month = datetime.date.today().strftime("%B")
print daynumber
print weeknumber
print weekday
print month

if month=="January ":
		chore = "Wipe inside of Kitchen Cabinets and Drawers"
        print chore
elif month=="February":
		chore = "Organise Cupboards and Pantry"
        print chore
elif month=="March":
        chore = "Wipe inside of Bathroom Cabinets and Drawers"
		print ""
elif month=="April":
        chore = "Garage"
		print chore
elif month=="May":
        chore = "Outside of the House"
		print chore
elif month=="June":
        chore = "Wash Walls, Mouldings and Doors"
		print chore
elif month=="July":
        chore = "Shampoo Carpets"
		print chore
elif month=="August":
        chore = "Windows/Window Sills"
		print chore
elif month=="September":
        chore = "Blinds and Window Treatments"
		print chore
elif month=="October":
        chore = "Garage"
		print chore
elif month=="November":
        chore = "Move Fridge/Oven"
		print chore
elif month=="December":
        chore = "Wash Walls, Mouldings and Doors"
		print chore		
else:
        print "Date not recognised"
