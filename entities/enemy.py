class Enemy(Entity):

	def __init__(self, name):
		super(Enemy, self).__init__(name, randint(5,10))
		self.name = name
		self.hp = self.max_hp