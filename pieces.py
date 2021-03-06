from random  import randint

class Empty:

	def __init__(self,pos,grid):
		self.pos=pos
		self.grid=grid
		self.id=0

class Obstacle:

	def __init__(self,pos, grid):
		grid.insert(self)
		grid.outOfbounds.append(self)
		self.pos=pos
		self.grid=grid
		self.color="Black"
		self.id=1
		grid.black(self)

class Head:
	def __init__(self,pos,grid,lead):
		self.pos=pos
		self.id=10
		self.grid=grid
		grid.insert(self)
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

class Palet:
	def __init__(self,pos,grid):
		self.placesToBe = [[1,0],[0,-1],[-1,0],[0,1]]
		self.local=0
		self.pos=pos
		self.grid=grid
		grid.insert(self)
		self.id=11

	def moveUp(self):
		test=[-1,-1]
		x=self.placesToBe[self.local]
		test[0]=x[0]+self.pos[0]
		test[1]=x[1]+self.pos[1]
		if not self.grid.toDie(test):
			self.grid.clean(self)
			self.grid.insert(Empty(self.pos,self.grid))
			self.pos[0]+=x[0]
			self.pos[1]+=x[1]
			self.grid.insert(self)
			self.grid.circle(self)
			return
		self.local=randint(0,3)
