import random
from PIL import Image
from tkinter import*

Locations = ["Airport Maintenace", "Arklov Peak Military Base", "Atlas Superstore", "BCH TV Station", "Barakett Promenade East",
"Barakett Promenade West", "Bloc 14", "Bloc 15", "Bloc 16", "Bloc 18", "Bloc 6", "City of Verdansk Port", "Crash Site",
"Downtown Tavorsk District", "Gora Bridge", "Gora Dam", "Gorengard Lumber Yard", "Jarvdinsk Spomenik", "Junkyard",
"Karst River Quarry", "Kart Racing Track", "Krovnik Farmland", "Lozoff Pass", "Novi Grazna Hills", "Riverside",
"Storage Town", "Styor Spomenik", "Tavorsk Park", "Tavorsk Park", "Torsk Bloc", "Verdansk Graveyard",
"Verdansk International Airport", "Verdansk Stadium", "Verdansk Train Station", "WHP Camp", "Zhokov Boneyard",
"Zordaya Prison Complex", "Zozsni Spomenik", "Nick's Neghborhood", "Shay's Bunker"]

random_loc = random.choice(Locations)
im = Image.open("Verdansk-Map.jpg")
window = Tk()
window.title('WHAT IS GOING ON YOU GUYS')
label = label(window, text = "The BOIZ are dropping at " + random_loc, im.show())

#print("\nThe BOIZ are dropping at " + random_loc)

im.show()
