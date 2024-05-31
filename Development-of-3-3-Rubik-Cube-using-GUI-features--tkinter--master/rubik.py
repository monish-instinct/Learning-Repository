
import tkinter
from tkinter import Button

colors={1:'red',2:'green',3:'blue',4:'white',5:'yellow',6:'orange'}
class rbface:
	def __init__(self,a1):
		self.a=self.b=self.c=[a1,a1,a1]
	def flipX(self):
		temp=self.a
		self.a=self.c
		self.c=temp
	def flipY(self):
		self.a.reverse()
		self.b.reverse()
		self.c.reverse()
	def exchange_rowa(self,a1):
		temp =self.a
		self.a=a1
		return temp
	def exchange_rowc(self,c1):
		temp =self.c
		self.c=c1
		return temp
	def exchange_col1(self,a1):
		temp=[]
		temp.append(self.a[0])
		temp.append(self.b[0])
		temp.append(self.c[0])
		self.a[0]=a1[0]
		self.b[0]=a1[1]
		self.c[0]=a1[2]
		return temp
	def exchange_col3(self,a1):
		temp=[]
		temp.append(self.a[2])
		temp.append(self.b[2])
		temp.append(self.c[2])
		self.a[2]=a1[0]
		self.b[2]=a1[1]
		self.c[2]=a1[2]
		return temp
	def spin_right(self):
		a=self.a
		b=self.b
		c=self.c
		self.a=[c[2],b[2],a[2]]
		self.b=[c[1],b[1],a[1]]
		self.c=[c[0],b[0],a[0]]
	def spin_left(self):
		a=self.a
		b=self.b
		c=self.c
		self.a=[c[0],b[0],a[0]]
		self.b=[c[1],b[1],a[1]]
		self.c=[c[2],b[2],a[2]]

class rbcube:		
	def __init__(self):
		self.frontf=rbface(1)
		self.rightf=rbface(2)
		self.backf=rbface(3)
		self.leftf=rbface(4)
		self.bottomf=rbface(5)
		self.topf=rbface(6)
	def swap(self,a,b):
		temp=a
		a=b
		b=temp
	def move_right_A(self):
		a=self.frontf.exchange_rowa(self.leftf.a)
		a=self.rightf.exchange_rowa(a)
		a=self.backf.exchange_rowa(a)
		a=self.leftf.exchange_rowa(a)
		self.topf.spin_right()
		return True
	def move_right_C(self):
		c=self.frontf.exchange_rowc(self.leftf.c)
		c=self.rightf.exchange_rowc(c)
		c=self.backf.exchange_rowc(c)
		c=self.leftf.exchange_rowc(c)
		self.bottomf.spin_left()
		return True
	def move_left_A(self):
		a=self.frontf.exchange_rowa(self.rightf.a)
		a=self.leftf.exchange_rowa(a)
		a=self.backf.exchange_rowa(a)
		a=self.rightf.exchange_rowa(a)
		self.topf.spin_left()
		return True
	def move_left_C(self):
		c=self.frontf.exchange_rowc(self.rightf.c)
		c=self.leftf.exchange_rowc(c)
		c=self.backf.exchange_rowc(c)
		c=self.rightf.exchange_rowc(c)
		self.bottomf.spin_right()
		return True
	def move_up1(self):
		temp=[]
		temp.append(self.frontf.a[0])
		temp.append(self.frontf.b[0])
		temp.append(self.frontf.c[0])
		temp = self.topf.exchange_col1(temp)
		temp.reverse()
		temp = self.backf.exchange_col3(temp)
		temp.reverse()
		temp = self.bottomf.exchange_col1(temp)
		temp = self.frontf.exchange_col1(temp)
		self.leftf.spin_right()
		return True
	def move_up3(self):
		temp=[]
		temp.append(self.frontf.a[2])
		temp.append(self.frontf.b[2])
		temp.append(self.frontf.c[2])
		temp = self.topf.exchange_col3(temp)
		temp.reverse()
		temp = self.backf.exchange_col1(temp)
		temp.reverse()
		temp = self.bottomf.exchange_col3(temp)
		temp = self.frontf.exchange_col3(temp)
		self.rightf.spin_left()
		return True
	def move_down1(self):
		temp=[]
		temp.append(self.frontf.a[0])
		temp.append(self.frontf.b[0])
		temp.append(self.frontf.c[0])
		temp.reverse()
		temp = self.bottomf.exchange_col1(temp)
		temp.reverse()
		temp = self.backf.exchange_col3(temp)
		temp.reverse()
		temp = self.topf.exchange_col1(temp)
		temp = self.frontf.exchange_col1(temp)
		self.leftf.spin_left()
		return True
	def move_down3(self):
		temp=[]
		temp.append(self.frontf.a[2])
		temp.append(self.frontf.b[2])
		temp.append(self.frontf.c[2])
		temp = self.bottomf.exchange_col3(temp)
		temp.reverse()
		temp = self.backf.exchange_col1(temp)
		temp.reverse()
		temp = self.topf.exchange_col3(temp)
		temp = self.frontf.exchange_col3(temp)
		self.rightf.spin_right()
		return True
	def go_left(self):
		temp=self.frontf
		self.frontf=self.leftf
		self.leftf=self.backf
		self.backf=self.rightf
		self.rightf=temp
		self.topf.spin_right()
		self.bottomf.spin_left()
		return True
	def go_right(self):
		temp=self.frontf
		self.frontf=self.rightf
		self.rightf=self.backf
		self.backf=self.leftf
		self.leftf=temp
		self.topf.spin_left()
		self.bottomf.spin_right()
		return True
	def go_down(self):
		temp=self.frontf
		self.bottomf.flipX()
		self.frontf=self.bottomf
		self.bottomf=self.backf
		self.topf.flipX()
		self.backf=self.topf
		self.topf=temp
		self.leftf.spin_right()
		self.rightf.spin_left()
		return True
	def go_up(self):
		temp=self.frontf
		self.frontf=self.topf
		self.backf.flipX()
		self.topf=self.backf
		self.bottomf.flipX()
		self.backf=self.bottomf
		self.bottomf=temp
		self.leftf.spin_left()
		self.rightf.spin_right()
		return True

def update():
	button = Button(mwindow, text ="",height=3,width=3,bg=colors[cube.frontf.a[0]]).grid(row=1,column=1)
	button = Button(mwindow, text ="",height=3,width=3,bg=colors[cube.frontf.a[1]]).grid(row=1,column=2)
	button = Button(mwindow, text ="",height=3,width=3,bg=colors[cube.frontf.a[2]]).grid(row=1,column=3)

	button = Button(mwindow, text ="",height=3,width=3,bg=colors[cube.frontf.b[0]]).grid(row=2,column=1)
	button = Button(mwindow, text ="",height=3,width=3,bg=colors[cube.frontf.b[1]]).grid(row=2,column=2)
	button = Button(mwindow, text ="",height=3,width=3,bg=colors[cube.frontf.b[2]]).grid(row=2,column=3)

	button = Button(mwindow, text ="",height=3,width=3,bg=colors[cube.frontf.c[0]]).grid(row=3,column=1)
	button = Button(mwindow, text ="",height=3,width=3,bg=colors[cube.frontf.c[1]]).grid(row=3,column=2)
	button = Button(mwindow, text ="",height=3,width=3,bg=colors[cube.frontf.c[2]]).grid(row=3,column=3)
	return True

cube=rbcube()
mwindow = tkinter.Tk()
button = Button(mwindow, text ="^", command = lambda:cube.move_up1()&update() ).grid(row=0,column=1)
button = Button(mwindow, text ="up", command = lambda:cube.go_up()&update() ).grid(row=0,column=2)
button = Button(mwindow, text ="^", command = lambda:cube.move_up3()&update() ).grid(row=0,column=3)
button = Button(mwindow, text ="<", command = lambda:cube.move_left_A()&update() ).grid(row=1,column=0)
button = Button(mwindow, text =">", command = lambda:cube.move_right_A()&update() ).grid(row=1,column=4)
button = Button(mwindow, text ="left", command = lambda:cube.go_left()&update() ).grid(row=2,column=0)
button = Button(mwindow, text ="right", command = lambda:cube.go_right()&update() ).grid(row=2,column=4)
button = Button(mwindow, text ="<", command = lambda:cube.move_left_C()&update() ).grid(row=3,column=0)
button = Button(mwindow, text =">", command = lambda:cube.move_right_C()&update() ).grid(row=3,column=4)
button = Button(mwindow, text ="v", command = lambda:cube.move_down1()&update() ).grid(row=4,column=1)
button = Button(mwindow, text ="down", command = lambda:cube.go_down()&update() ).grid(row=4,column=2)
button = Button(mwindow, text ="v", command = lambda:cube.move_down3()&update() ).grid(row=4,column=3)
update()
mwindow.mainloop()
		

