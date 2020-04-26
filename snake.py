# Snake
import turtle as t
from random  import randint
import time as sec
from grid import Grid
from grid import Obstacle
sc=t.Screen()
sc.title("Python the Snake v.2.1")
sc.tracer(0,0)
ot=t.Turtle()
oc=t.Turtle()
ot.ht()
oc.ht()



class Game:

	def __init__(self,x,y):
		self.level=[9,12,12,12,15,15,15,18,18,18,20,20,20]
		self.nowplaying=False
		self.direcion=[1,0]# going to the right
		self.waiting=False
		self.rate = x
		self.total=0
		if y==5:
			y=randint(1,4)
		self.gameMode=y
		self.grid=Grid(2,oc)# put a proper start screen
		sc.onscreenclick(self.play)
		sc.onkey(self.left, "Left")
		sc.onkey(self.up, "Up")
		sc.onkey(self.right, "Right")
		sc.onkey(self.down, "Down")
		sc.listen()
		sc.update()

	def roudy(self,ting):
		Obstacle(ting,self.grid)

	def newloop(self):
		for i in range(300):
		#while True:
			sc.update()
			print("{0} moves".format(300-i))
			sec.sleep(0.5/self.rate)
			self.grid.move(self.direcion)
			self.waiting=False
			self.total+=self.grid.eat()
			sec.sleep(0.5/self.rate)
			if self.gameMode==1:
				if self.total==10:
					return

	def getObstacle(self,lvl):
		fname="obstacles{0}.ofg".format(lvl)
		rex = open(fname,"r")
		fl = rex.read()
		fl= fl.split("\n")
		fl.pop(-1) # last string is empty
		print(fl)
		for les in fl:
			les=les.split(",")
			enn = []
			enn.append(int(les[0]))
			enn.append(int(les[1]))
			self.roudy(enn)
		rex.close()

	def blank(self):
		oc.pencolor("White")
		oc.fillcolor("White")
		rad = 587
		x=-290
		y=295
		oc.pu()
		oc.goto(x+2,y-1)
		oc.pd()
		oc.begin_fill()
		for m in range(4):
			oc.fd(rad)
			oc.rt(90)
		oc.pu()
		oc.end_fill()

	def play(self,x,y):
		plr = self.rate
		print([x,y])
		self.nowplaying=True
		for games in range(plr):
			self.startGame(games)
			self.rate=games+1
			self.newloop()

	def startGame(self,mode):
		self.direcion=[1,0]
		self.grid=Grid(self.level[mode],ot)
		if self.gameMode==4:
			self.getObstacle(mode)

	def left(self):
		print("left")
		if self.direcion[1]==0 or self.waiting: # you cant go this direction if already or its opposite
			return
		self.direcion=[-1,0]
		self.waiting=True

	def right(self):
		if self.direcion[1]==0 or self.waiting:
			return
		self.direcion=[1,0]
		self.waiting=True

	def up(self):
		if self.direcion[0]==0 or self.waiting:
			return
		self.direcion=[0,-1]
		self.waiting=True

	def down(self):
		if self.direcion[0]==0 or self.waiting:
			return
		self.direcion=[0,1]
		self.waiting=True

print("1. Ten to go\n2. Scales of time\n3. Mouse chase\n4. Mamba maze\n5. Dealers choice")
x=input("choose a game type : ")
tdud= Game(11,int(x))
def find(x,y):
	area=585/18
	pa=int((x+290)/area)
	pb=17-int((y+295)/area)
	print([pa,pb])
	tdud.roudy([pa,pb])
	rex.write("{0},{1}\n".format(pa,pb))



#sc.onscreenclick(find)
sc.mainloop()
#tdud.newloop()



