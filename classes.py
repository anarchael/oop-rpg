from random import randint
from dependencies import validate_int

# Super-classe Entity
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

# Classe Player héritant de Entity	
class Player(Entity):
	def __init__(self, name=None):
		super(Player, self).__init__(name, 20)
		self.hp = self.max_hp
		self.hit_chance = 60
		self.is_alive = True
		self.score = 0

		if name == None:
			self.name = input("Choisissez un nom pour votre héro : ")
		else:
			self.name = name

	def dead(self):
		print(f"{self.name} mange les pissenlits par la racine.")

	#Fonctions qui renvoient un booléen correspondant à des probabilités pseudo-aléatoires
	def hits_enemy(self):
		return randint(0,100) < self.hit_chance

	def flee(self):
		return randint(0,100) < 20

	def add_score(self, amount, specification):
		self.score += amount
		print(f"{specification} Son score augmente de {amount}. \n(Score actuel: {self.score})")
	
	#fonctions spécifiques des salles
	def fight(self, enemy): #Résouds le choix du joueur pour le combat
		user_input = validate_int("Que voulez vous faire ?\n1 - Combattre\n2 - Fuir\n", ["1", "2"])
		if user_input == 1:
			if self.hits_enemy():
				enemy.reduce_hp()
			else:
				self.reduce_hp()
			return 1

		elif user_input == 2:
			if self.flee():
				print(f"{self.name} s'enfuit.")
				return 2
			else:
				print(f"{self.name} ne parvient pas à s'enfuir")
				self.reduce_hp()
				return 1

	def collect(self): #Résouds le choix du joueur pour les trésors
		user_input = validate_int("Voulez-vous l'ouvrir ?\n1 - Oui\n2 - Non", ["1", "2"])
		if user_input == 1:
			if is_mimic():
				print("C'était un mimic !!")
				self.reduce_hp()
			else:
				self.add_score(2, f"{self.name} ramasse le trésor.")
		elif user_input == 2:
			input(f"{self.name} passe son chemin... (Appuyez sur Entrée pour continuer)")

	def drinks_potion(self): #Résouds le choix du joueur pour la potion 
		user_input = validate_int("Voulez-vous la boire?\n1 - Oui\n2 - Non", ["1", "2"])
		if user_input == 1:
			if is_poison():
				print("C'était du poison !!")
				self.reduce_hp(5)
			else:
				self.heal_hp(5)
		elif user_input == 2:
			input(f"{self.name} passe son chemin... (Appuyez sur Entrée pour continuer)")

# Classe Enemy héritant de Entity
class Enemy(Entity):

	def __init__(self, name):
		super(Enemy, self).__init__(name, randint(5,10))
		self.name = name
		self.hp = self.max_hp

# Valeurs booléenes non liées à des entités
def is_mimic():
	return randint(0,100) < 15

def is_poison():
	return randint(0,100) < 5
