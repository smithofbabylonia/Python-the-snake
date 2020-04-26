class Empty:

	def __init__(self,pos,grid):
		self.pos=pos
		self.grid=grid

class Obstacle:

	def __init__(self,pos, grid):
		grid.grid[pos[1]][pos[0]]=self
		grid.outOfbounds.append(self)
		self.pos=pos
		self.grid=grid
		self.color="Black"
		grid.black(self)

class Head:
	def __init__(self,pos,grid,lead):
		self.pos=pos
		self.grid=grid
		self.snake=None
		self.lead=lead
		self.color="Green"
		if lead:
			grid.black(self)


	def __str__(self):
		return "head at {0} in Lead: {1}.".format(self.pos,self.lead)


	def moveUp(self,po):
		#print(type(self.snake))
		if self.snake==None:
			self.grid.clean(self)
			self.pos=po
			#print("ened")
			return
		if self.lead:
			#print("headed")
			self.snake.moveUp(self.pos)
			self.pos=po
			self.grid.black(self)
			return
		#print("middle body")
		self.snake.moveUp(self.pos)
		self.pos=po

	def snaking(self, oni):
		oni.append(self.pos)
		if self.snake==None:
			return oni
		return self.snake.snaking(oni)

	def grow(self):
		if self.snake==None:
			self.snake=Head(self.pos,self.grid,False)
		else:
			self.snake.grow()

class Palet(Empty):
	pass
