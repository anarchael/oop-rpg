from classes import Player, Enemy
from random import randint

# Fonction pour valider les choix du joueur



# Fonctions gérant les salles
def generate_room(player, probabilities=[25, 25, 25]):
	print("")
	room_chance = randint(0,100)
	probs = define_probs(probabilities)
	if room_chance < probs[0]:
		enemy = Enemy("Squelette")
		print(f"{player.name} tombe nez à nez avec un {enemy.name.lower()} !!")
		enter_enemy_room(player, enemy)
	elif room_chance < probs[1]:
		print(f"{player.name} trouve un coffre !!")
		enter_treasure_room(player)
	elif room_chance < probs[2]:
		print(f"{player.name} trouve une potion non identifiée")
		enter_potion_room(player)
	else:
		input("La salle est vide... (Appuyez sur entrée pour continuer)")
		generate_room(player, probabilities)

# Gestion des salles
def define_probs(probabilities):
	probs = []
	prob = 0
	for i in probabilities:
		prob+=i
		probs.append(prob)
	return probs

def enter_enemy_room(player, enemy, probabilities=[10, 30, 30]):
	action = 0
	while enemy.hp > 0 and player.hp > 0:
		action = player.fight(enemy)
		if action == 2:
			break
	if not player.is_dead():
		if action != 2:
			player.add_score(5, f"{player.name} a vaincu {enemy.name}")
		generate_room(player, probabilities)
	else:
		player.dead()

def enter_treasure_room(player, probabilities=[30, 10, 30]):
	player.collect()
	if not player.is_dead():
		generate_room(player, probabilities)
	else:
		player.dead()

def enter_potion_room(player, probabilities=[30,30,10]):
	player.drinks_potion()
	if not player.is_dead():
		generate_room(player, probabilities)
	else:
		player.dead()