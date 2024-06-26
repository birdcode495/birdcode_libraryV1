

# ----------------------------------------------------- BirdCode: The Library of Life ---------------------------------------------------

from BirdCode_SuperClass import Eukaryota












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


# ---------------------------------  Creation of the Superclass Aves -----------------------------------


class Aves(Eukaryota):

	def __init__(self):

		super().__init__()

		self.__class_scientificName = 'Aves'
		self.__class_englishName = 'Birds'
		self.__class_spanishName = 'Aves'
		self.__class_frenchname = 'Oiseaux'
		self.__class_germanName = 'Vögel'
		self.__class_chineseName = '鸟类'
		self.__class_speciesRichness_gbif = 14825
		self.__vertebralColumn = True
		self.__homeothermy = True
		self.forelimbs = 'wings'
		self.integumentarySystem = 'feathers'
		self.mouthType = 'beak'
		self.__teeth = False
		self.__animalReproduction = 'oviparous'
		self.__class_temporalRange_ma = 72
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

		print("The integumentary system of Mulsant 1 is: ", self.integumentarySystem)
		print("The forelimbs of Mulsant 1 are: " , self.forelimbs)
		print("The mouth type of Mulsant 1 is: ", self.mouthType)




## --------------------------------------- Creation of the subclass Apodiformes ----------------------------------


class Apodiformes(Aves):

	def __init__(self):

		super().__init__()

		self.order_scientificName = 'Apodiformes'
		self.order_englishName = 'swifts, treeswifts and hummingbirds'
		self.spanishName = 'vencejos, salaganas, vencejos arborícolas y colibríes'
		self.frenchName = ''
		self.germanName = ''
		self.chineseName = ''
		self.order_speciesNumber_gbif = 541







### ------------------------------------- Creation of the subclass Trochilidae ------------------------------------


class Trochilidae(Apodiformes):

	def __init__(self):

		super().__init__()

		self.__family_scientificName = 'Trochilidae'
		self.__englishName = 'Hummingbirds'
		self.__spanishName = 'Colibríes'
		self.__frenchName = ''
		self.__germanName = ''
		self.__chineseName = ''
		self.__family_speciesNumber_gbif = 387
		self.__family_endemism = 'America'
		self.__family_temporalRange_ma = 30







#### ------------------------------------- Creation of the subclasses of the Trochilidae subfamilies ----------------------------------------


class Florisuginae(Trochilidae):

	def __init__(self):

		super().__init__()

		self.__subfamily_scientificName = 'Florisuginae'
		self.__subfamily_speciesNumber = 4
		self.__englishName = 'topazes'


class Phaethornithinae(Trochilidae):

	def __init__(self):

		super().__init__()

		self.__subfamily_scientificName = 'Phaethornithinae'
		self.__subfamily_speciesNumber = 37
		self.__englishName = 'hermits'


class Polytminae(Trochilidae):

	def __init__(self):

		super().__init__()

		self.__subfamily_scientificName = 'Polytminae'
		self.__subfamily_speciesNumber = 29
		self.__englishName = 'mangoes'


class Lesbiinae(Trochilidae):

	def __init__(self):

		super().__init__()

		self.__subfamily_scientificName = 'Lesbiinae'
		self.__subfamily_speciesNumber = 30
		self.__englishName = 'brilliants and coquettes'


class Patagoninae(Trochilidae):

	def __init__(self):

		super().__init__()

		self.__subfamily_scientificName = 'Patagoninae'
		self.__subfamily_speciesNumber = 1
		self.__englishName = 'giant hummingbird'


class Trochilinae(Trochilidae):

	def __init__(self):

		super().__init__()

		self.__subfamily_scientificName = 'Trochilinae'
		self.__subfamily_speciesNumber = 170
		self.__englishName = 'mountain gems, bees and emeralds'





##### ------------------------------------ Creation of the subclasses of the Trochilidae family genuses ------------------

#### & ----------------------------------- Subfamily Florisuginae --------------


class Topaza(Florisuginae):

	def __init__(self):

		super().__init__()

		self.genus_scientificName = 'Topaza'


class Florisuga(Florisuginae):

	def __init__(self):

		super().__init__()

		self.__genus_scientificName = 'Florisuga'







# ------------------------------------------- Object creation -----------------------------------------------
		


print("--------------------------------------- First object creation ----------------------------------")

print()
Mulsant1 = Topaza()
print(Mulsant1.takeOff(True))
print()
Mulsant1.state()
print()
print("The scientific name of Mulsant1 is: ", Mulsant1.__genus_scientificName)

print("------------------------------------- second object creation --------------------------------------")

print()
Coruscans1 = Florisuga()
print(Mulsant1.takeOff(False))
print()
Coruscans1.__integumentarySystem = 'fear'
Coruscans1.state()
print()







