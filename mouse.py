class Pointer(object):#it runs constructer function first
	def __init__(self,x,y):#self refers to your object
		self.x=x
		self.y=y

# >>> from Pointer import Pointer
# >>> mypointer=Pointer(10,20)
# >>> from mouse import Pointer
# >>> mypointer=Pointer(10,20)
# >>> mypointer.__class__
# <class 'mouse.Pointer'>
# >>> mypointer.x
# 10
# >>> mypointer.y
# 20
# >>>
	def moveUp(self):
		self.y=self.y + 1
	def moveDown(self):
		self.y=self.y-1
	def checkpos(self):
		x=self.x
		y=self.y
		print("{} ,{}".format(x,y))