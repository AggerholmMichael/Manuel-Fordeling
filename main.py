# This Python file uses the following encoding: utf-8
# Alle tal er i meter
# Vi definerer at "Debug Besked" forkortes DB samt bruges.
# 

antal_paller = 1			#Variabel til at gemme antal generede paller
antal_produktioner = 0		#Variabel til at gemme antal generede produktioner
palledict = {}				#Dictionary til at gemme vores paller i (Dette gælder åbentbart også objects!)
class Palle():
	
	def __init__(self):
		print "PALLE"		#DB
		global antal_paller			#Giver adgang til variablen "antal_paller" i dette scope/class/def
		antal_paller += 1		#Plus 1 stk palle pAA palle_antal
		self.maengde = 0                    #Beholder til volumen af raavare, bruges til udregning af fordelingsfaktor	
		self.omregningsfaktor = 0           #procentdelen som denne palle indeholder ud af indholdet fra ALLE paller i ordren.
		
class Produktion():
	print "PRODUKTION"			#DB
	produktions_id = ""			#Container til produktions-ID
	kalkuleret_antal = 0					#Det forhaands kalkulerede maengde af raavarer som skal forbruges i denne produktion

while antal_paller < 2:

	palle_id = input("Indtast Palle-ID: ")		#variabel oprettes, input fra bruger (Palle-ID'et) gemmes.
	palledict[palle_id] = Palle()				#En Palle bliver spawned i vores dictionary, Palle-ID'et er dens navn :D
	print str(palledict[palle_id]) + " Oprettet"	#DB
	
	palledict[palle_id].maengde = input("Indtast maengde: ")		#Pallens maengde tilgåes via dictionary, og ændres afhængig af bruger inputtet
	print str(palledict[palle_id].maengde) + " Tilfoejet til pallen"	#DB
	
	#testpalle = Palle()		#DB

raw_input()					#Holder min CMD AAben :P