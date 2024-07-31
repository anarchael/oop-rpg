class Entity:

	def __init__(self, name, max_hp):
		self.name = name
		self.max_hp = max_hp
	
	def reduce_hp(self, amount=1): #Réduit les pv de l'entité
		self.hp -= amount
		print(f"{self.name} a perdu {amount} points de vie. (PV actuels: {self.hp}/{self.max_hp})")

	def heal_hp(self, amount=1):  # Soigne les pv de l'entité
		if self.hp+amount > self.max_hp:
			amount = self.max_hp-self.hp
		self.hp += amount
		print(f"{self.name} a été soigné de {amount} points de vie ! (PV actuels: {self.hp}/{self.max_hp})")

	def is_dead(self): # Vérifie si l'entité est morte
		return self.hp <= 0