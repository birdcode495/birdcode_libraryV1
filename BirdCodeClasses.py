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

	vertebralColumn = True
	homeothermy = True
	forelimbs = 'wings'
	integumentarySystem = 'feathers'
	mouthType = 'beak'
	teeth = False
	animalReproduction = 'oviparous'
	temporalRange_ma = 72
	specialty = 'Ornithology'
	digestiveSystem = 'crop and gizzard'
	sexChromosome = 'Z, W'
	femalesChromosome = '(ZW)'
	maleChromosome = '(ZZ)'
	sweatGland = False
	flight = True
	flying = False

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
		


print("--------------------------------------- First object creation ----------------------------------")

print()
Mulsant1 = Aves()
print(Mulsant1.takeOff(True))
Mulsant1.state()
print()

print("------------------------------------- second object creation --------------------------------------")

print()
Coruscans1 = Aves()
print(Mulsant1.takeOff(False))
Coruscans1.state()
print()







