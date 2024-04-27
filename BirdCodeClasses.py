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

	def takeOff(self):
		self.flying = True


	def state(self):
		if self.flying:
			return "Mulsant 1 is flying"

		else:
			return "Mulsant 1 is stopped"



Mulsant1 = Aves()

print("The integumentary system of Mulsant 1 is: " , Mulsant1.integumentarySystem)
print("The forelimbs of Mulsant 1 are: " , Mulsant1.forelimbs)
print("The mouth type of Mulsant 1 is: ", Mulsant1.mouthType)
print("Mulsant 1 is flying? ", Mulsant1.flying)
Mulsant1.takeOff()
print(Mulsant1.state())





