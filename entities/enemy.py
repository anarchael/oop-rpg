from random import randint

class Enemy(Entity):

	def __init__(self, name):
		super(Enemy, self).__init__(name, 10)
		self.name = name
		self.hp = self.max_hp

	def set_max_hp(player):
		self.max_hp = randint(5+(player.level*2), 10+(player.level*2))
		self.hp = self.max_hp