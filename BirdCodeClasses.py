# ---------------------------------  Aves class creation -----------------------------------
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


class Aves():

	def __init__(self):

		self.vertebralColumn = True
		self.homeothermy = True
		self.forelimbs = 'wings'
		self.integumentarySystem = 'feathers'
		self.mouthType = 'beak'
		self.teeth = False
		self.animalReproduction = 'oviparous'
		self.temporalRange_ma = 72
		self.specialty = 'Ornithology'
		self.digestiveSystem = 'crop and gizzard'
		self.sexChromosome = 'Z, W'
		self.femaleChromosome = '(ZW)'
		self.maleChromosome = '(ZZ)'
		self.sweatGland = False
		self.flight = True
		self.flying = False

	def takeOff(self, letsFly):
		
		self.flying = letsFly

		if self.flying:
			return "Mulsant 1 is flying"

		else:
			return "Mulsant 1 is stopped"


	def state(self):

		print("The integumentary system of Mulsant 1 is: ", self.integumentarySystem)
		print("The forelimbs of Mulsant 1 are: " , self.forelimbs)
		print("The mouth type of Mulsant 1 is: ", self.mouthType)


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
Coruscans1.state()
print()







