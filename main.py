# This Python file uses the following encoding: utf-8
# Alle tal er i meter
# Vi definerer at "Debug Besked" forkortes DB samt bruges.
# 
ticks = 0
antal_paller = 1			#Variabel til at gemme antal generede paller
antal_produktioner = 0		#Variabel til at gemme antal generede produktioner
palledict = {}				#Dictionary til at gemme vores paller i (Dette gælder åbentbart også objects!)
palletabel = {}				#Dict til at oversætte palle-ID'er til tal (1, 2, 3, 4, 5, etc.)
produktionsdict = {}			#Dictionary til at gemme vores produktioner i


class Palle():
	
	def __init__(self):
		print "PALLE"		#DB

		self.maengde = 0                    #Beholder til volumen af raavare, bruges til udregning af fordelingsfaktor	

	
class Produktion():

	def __init__(self):
		print "PRODUKTION"			#DB

		kalkuleret_antal = 0		#Det forhaands kalkulerede maengde af raavarer som skal forbruges i denne produktion
		self.omregningsfaktor = 0   #procentdelen som denne produktion skal modtage, ud af beløbet som alle produktioner skal modtage i alt


while ticks < 100:
	if antal_paller < 4:

		palle_id = input("Indtast Palle-ID: ")		#variabel oprettes, input fra bruger (Palle-ID'et) gemmes.
		palledict[palle_id] = Palle()				#En Palle bliver spawned i vores dictionary, Palle-ID'et er dens navn :D
		print str(palledict[palle_id]) + " Oprettet"	#DB
	
		palledict[palle_id].maengde = input("Indtast maengde: ")		#Pallens maengde tilgåes via dictionary, og ændres afhængig af bruger inputtet
		print str(palledict[palle_id].maengde) + " Tilfoejet til pallen"	#DB
		
		palletabel[antal_paller] = palle_id		#Tilføjer pallen til vores tabel, så vi kan henvise til den via simple tal i stedet for et indviklet palle-id
		print palletabel[antal_paller]		#DB
		antal_paller += 1		#Plus 1 stk palle pAA palle_antal
	
		#testpalle = Palle()		#DB
	

	elif antal_produktioner < 3:

		produktions_id = input("Indtast Produktions nummer: ") #Bruger input, produktionsnummer
		produktionsdict[produktions_id] = Produktion()			#Produktion spawnes
		print str(produktionsdict[produktions_id]) + " Oprettet" #DB
	
		produktionsdict[produktions_id].kalkuleret_antal = input("Indtast det kalkulerede antal: ") #Bruger input, kalkuleret antal
		print str(produktionsdict[produktions_id].kalkuleret_antal)
		antal_produktioner += 1	
		
	ticks += 1
#raw_input()					#Holder min CMD AAben :P