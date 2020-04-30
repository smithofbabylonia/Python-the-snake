from pieces import *


class Grid:

	def __init__(self,game,size, ttl):
		vt=int(size/2)
		self.pen=ttl
		self.game=game
		self.origin =[-290,295]
		self.grid=[]
		self.outOfbounds=[]
		self.flag=False
		self.size=size
		self.area=585/size
		self.level=0
		self.head=None
		for s in range(size):
			e = []
			for t in range(size):
				e.append(Empty([s,t],self))
			self.grid.append(e)
		self.draw()
		if game.gameMode!=4:
			self.heading([vt,vt])
			self.putPalet()

	def putPalet(self):
		x= self.position()
		self.palet=Palet(x,self)
		self.circle(self.grid[x[1]][x[0]])
 
	def heading(self, pos):
		if self.grid[pos[1]][pos[0]].id==11: # dont put head on palet
			print("crash")
			pos[0]+=1
		self.head=Head(pos,self,True)
		self.head.grow()

	def insert(self,obj):
		x=obj.pos
		self.grid[x[1]][x[0]]=obj

	def eat(self):
		if self.flag:
			self.head.grow()
			x= self.position()
			self.palet=Palet(x,self)
			self.circle(self.grid[x[1]][x[0]])
			self.flag=False
			return 1
		return 0

	def move(self,chng):
		pos=[]
		pos.append(self.head.pos[0])
		pos.append(self.head.pos[1])
		self.grid[pos[1]][pos[0]]=Empty(pos,self)
		pos[0]+=chng[0]
		pos[1]+=chng[1]
		if self.toDie(pos):
			print("You died MF")
			self.game.loseLife()
			self.game.startGame(self.game.stage)
			return
		self.head.moveUp(pos)
		if type(self.grid[pos[1]][pos[0]])==Palet:
			self.flag=True
		self.grid[pos[1]][pos[0]]=self.head

	def toDie(self,uh):
		if uh[0]<0 or uh[1]<0 or uh[0]==self.size or uh[1]==self.size:
			return True
		if self.grid[uh[1]][uh[0]] in self.outOfbounds:
			return True
		x = self.head.snaking([])
		for y in x: # self biting
			if (uh[0]==y[0] and uh[1]==y[1]) :
				return True
		return False

	def position(self):
		x=[[-1,-1]]
		if self.head!=None:
			x = self.head.snaking([])
		why = True
		a=0
		b=0
		while why:
			a= randint(0,self.size-1)
			b= randint(0,self.size-1)
			for y in x:
				if a==y[0] and b==y[1]:
					break # to rand
			if a==y[0] and b==y[1]:
				why=True
			elif self.grid[b][a] in self.outOfbounds:
				why=True
			else:
				why=False
		return [a,b]

	def black(self,obj):
		self.pen.pencolor(obj.color)
		self.pen.fillcolor(obj.color)
		rad = self.area-4
		x=self.origin[0]+obj.pos[0]*self.area
		y=self.origin[1]-obj.pos[1]*self.area
		self.pen.pu()
		self.pen.goto(x+2,y-1)
		self.pen.pd()
		self.pen.begin_fill()
		for m in range(4):
			self.pen.fd(rad)
			self.pen.rt(90)
		self.pen.pu()
		self.pen.end_fill()

	def clean(self,obj):
		self.pen.pencolor("White")
		self.pen.fillcolor("White")
		rad = self.area-4
		x=self.origin[0]+obj.pos[0]*self.area
		y=self.origin[1]-obj.pos[1]*self.area
		self.pen.pu()
		self.pen.goto(x+2,y-1)
		self.pen.pd()
		self.pen.begin_fill()
		for m in range(4):
			self.pen.fd(rad)
			self.pen.rt(90)
		self.pen.pu()
		self.pen.end_fill()

	def blank(self):
		self.pen.pencolor("White")
		self.pen.fillcolor("White")
		rad = 587
		x=self.origin[0]+1
		y=self.origin[1]-1
		self.pen.pu()
		self.pen.goto(x+2,y-1)
		self.pen.pd()
		self.pen.begin_fill()
		for m in range(4):
			self.pen.fd(rad)
			self.pen.rt(90)
		self.pen.pu()
		self.pen.end_fill()

	def circle(self,obj):
		self.pen.fillcolor("Red")
		rad = self.area/2 -2
		circumf = 2*3.14159265359*rad
		segment = circumf/360
		x=self.origin[0]+obj.pos[0]*self.area
		y=self.origin[1]-obj.pos[1]*self.area
		self.pen.pu()
		self.pen.goto(x+2,y-2)
		self.pen.fd(rad)
		self.pen.pd()
		self.pen.begin_fill()
		for m in range(360):
			self.pen.fd(segment)
			self.pen.rt(1)
		self.pen.pu()
		self.pen.end_fill()
					

	def draw(self):
		self.blank()
		self.pen.pencolor("Black")
		size=self.size
		self.pen.pu()
		self.pen.goto(self.origin[0],self.origin[1])
		self.pen.pd()
		for row in range(size):
			for col in range(size):
				for cnr in range(4):
					self.pen.fd(self.area)
					self.pen.rt(90)
				self.pen.fd(self.area)
			self.pen.bk(self.area*size)
			self.pen.rt(90)
			self.pen.fd(self.area)
			self.pen.lt(90)

