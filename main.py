# This Python file uses the following encoding: utf-8
# Alle tal er i meter
# Vi definerer at "Debug Besked" forkortes DB samt bruges.
# 

antal_paller = 0
antal_produktioner = 0

class Palle():
	
	def __init__(self):
		global antal_paller			#Giver adgang til variablen "antal_paller" i dette scope/class/def
		antal_paller += 1		#Plus 1 stk palle pAA palle_antal
		self.int_palle_id = antal_paller    # !BRUGES KUN I KODEN!!! Identifikation af pallen!!!
		self.palle_id = ""                  #String til identifikation af individuelle objecter
		self.maengde = 0                    #Beholder til volumen af raavare, bruges til udregning af fordelingsfaktor	
		self.omregningsfaktor = 0           #procentdelen som denne palle indeholder ud af indholdet fra ALLE paller i ordren.
		
class Produktion():
	produktions_id = ""
	kalkuleret_antal = 0					#Det forhaands kalkulerede maengde af raavarer som skal forbruges i denne produktion
		
class fordeling():
	global antal_paller			#Giver adgang til variablen "antal_paller" i dette scope/class/def
	

	if antal_paller <= 0:   #Laver en palle hvis der ingen er.
		palle_abe = Palle()		#jeg laver en ny palle, entity navnet er en placeholder
		print("if")          #DB
		print(antal_paller)	#DB
		print(palle_abe.int_palle_id) #DB
		print(palle_abe.maengde) #DB
		raw_input()					#Holder shell aaben :P venter paa tekst input
		
	else:
		print "else"	#DB
		raw_input()					#Holder min CMD AAben :P		
		
		
		print antal_paller	#DB
		#print antal_produktioner	#DB
		#print produktions_id		#DB
		#print kalkuleret_antal		#DB
		

