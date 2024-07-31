from random import randint
from math import ceil
from entity import Entity

class Player(Entity):
	def __init__(self, name=None):
		super(Player, self).__init__(name, 20)
		self.hp = self.max_hp
		self.xp = 0
		self.level = 1
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
				enemy.reduce_hp(self.level)
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

	def required_xp_to_next_level():
		return ceil((self.level*25)*0.8)

	def earn_xp(amount):
		self.xp += amount
		print(f"{self.name} gagne {amount} points d'expérience.")
		if self.xp >= required_xp_to_next_level():
			leftover = self.xp - required_xp_to_next_level()
			self.xp = 0+leftover
			level_up()
		print(f"Point d'expérience requis pour passer au niveau supérieur: {required_xp_to_next_level()}")



	def level_up():
		self.max_hp+=5
		self.hp = max_hp
		self.level+=1
		print(f"{self.name} a gagné en niveau !!\nVous gagnez 5 pvs supplémentaires et votre vie est restaurée !!")

def is_mimic():
	return randint(0,100) < 15

def is_poison():
	return randint(0,100) < 5