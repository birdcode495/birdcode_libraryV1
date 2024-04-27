print()
print()
print(" ------------------------------------------------------------------------------------")
print()
print()
print("                             BirdCode version 1: The Library of Life                  ")
print()
print()
print(" -------------------------------------------------------------------------------------")
print()
print()


# ---------------------------------  Creation of the class Aves -----------------------------------


class Aves():

	def __init__(self):

		self.__class_scientificName = 'Aves'
		self.__class_englishName = 'Birds'
		self.__class_spanishName = 'Aves'
		self.__class_frenchname = ''
		self.__class_germanName = ''
		self.__class_chineseName = '鸟类'
		self.__class_speciesNumber_gbif = 14825
		self.__vertebralColumn = True
		self.__homeothermy = True
		self.__forelimbs = 'wings'
		self.__integumentarySystem = 'feathers'
		self.__mouthType = 'beak'
		self.__teeth = False
		self.__animalReproduction = 'oviparous'
		self.__temporalRange_ma = 72
		self.__speciality = 'Ornithology'
		self.__digestiveSystem = 'crop and gizzard'
		self.__sexChromosome = 'Z, W'
		self.__femaleChromosome = '(ZW)'
		self.__maleChromosome = '(ZZ)'
		self.__sweatGland = False
		self.__flight = True
		self.__flying = False

	

	def takeOff(self, letsFly):
		
		self.__flying = letsFly

		if self.__flying:
			return "Mulsant 1 is flying"

		else:
			return "Mulsant 1 is stopped"


	def state(self):

		print("The integumentary system of Mulsant 1 is: ", self.__integumentarySystem)
		print("The forelimbs of Mulsant 1 are: " , self.__forelimbs)
		print("The mouth type of Mulsant 1 is: ", self.__mouthType)




# --------------------------------------- Creation of the class Apodiformes ----------------------------------


class Apodiformes(Aves):

	self.__order_scientificName = 'Apodiformes'
	self.__englishName = ''
	self.__spanishName = ''
	self.__frenchName = ''
	self.__germanName = ''
	self.__chineseName = ''
	self.__order_speciesNumber_gbif = 541







# ------------------------------------- Creation of the class Trochilidae ------------------------------------








# ------------------------------------------- Object creation -----------------------------------------------
		


print("--------------------------------------- First object creation ----------------------------------")

print()
Mulsant1 = Aves()
print(Mulsant1.takeOff(True))
print()
Mulsant1.state()
print()

print("------------------------------------- second object creation --------------------------------------")

print()
Coruscans1 = Aves()
print(Mulsant1.takeOff(False))
print()
Coruscans1.__integumentarySystem = 'fear'
Coruscans1.state()
print()






# ----------------------------------------- Creation of the class T
