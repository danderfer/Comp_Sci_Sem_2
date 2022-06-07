from graphics import *;
from random import *;
class Waldo:
	skinColor = color_rgb( 255, 194, 166 );
	brownColor = color_rgb( 128, 64, 0 );
	def __init__(self,point):
		self.point = point;
		x = point.getX();
		y = point.getY();
		self.head = Rectangle(point,Point(x+15,y+15));
		self.head.setFill(self.skinColor);
		hatP = [Point(x,y), Point(x+6,y-12), Point(x+9,y-12), Point(x+15,y)];
		self.hat = Polygon(hatP);
		self.hat.setFill("red");
		self.poof = Circle(Point(x+7, y-15), 6);
		self.poof.setFill("white");
		self.Eyes = Rectangle( Point(x+2, y+3), Point(x+13, y+7));
		self.Eyes.setFill("white");
		self.PupilOne = Rectangle(Point(x+4, y+4), Point(x+6, y+6));
		self.PupilTwo = Rectangle(Point(x+9, y+4), Point(x+11, y+6));
		self.thing1 = Rectangle(Point(x, y+3), Point(x+2, y+5));
		self.thing2 = Rectangle(Point(x+13, y+3), Point(x+15, y+5));
		self.mouth1 = Line(Point(x+4, y+13), Point(x+9, y+13));
		self.mouth2 = Line(Point(x+9, y+13), Point(x+12, y+12));
		###########################################################
	def draw(self,canvas):
		self.hat.draw(canvas);
		self.head.draw(canvas);
		self.poof.draw(canvas);
		self.Eyes.draw(canvas);
		self.PupilOne.draw(canvas);
		self.PupilTwo.draw(canvas);
		self.thing1.draw(canvas);
		self.thing2.draw(canvas);
		self.mouth1.draw(canvas);
		self.mouth2.draw(canvas);
	def setFill(self,color):
		self.hat.setFill(color);
	def move(self,dx,dy):
		self.point.x = self.point.x + dx;
		self.point.y = self.point.y + dy;
		self.hat.move(dx,dy);
		self.head.move(dx,dy);
		self.poof.move(dx,dy);
		self.Eyes.move(dx,dy);
		self.PupilOne.move(dx,dy);
		self.PupilTwo.move(dx,dy);
		self.thing1.move(dx,dy);
		self.thing2.move(dx,dy);
		self.mouth1.move(dx,dy);
		self.mouth2.move(dx,dy);
	def moveTo(self,x,y):
		self.undraw();
		self.__init__(Point(x,y));
	def undraw(self):
		self.hat.undraw();
		self.head.undraw();
		self.poof.undraw();
		self.Eyes.undraw();
		self.PupilOne.undraw();
		self.PupilTwo.undraw();
		self.thing1.undraw();
		self.thing2.undraw();
		self.mouth1.undraw();
		self.mouth2.undraw();
	def getX(self):
		return self.point.x;
	def getY(self):
		return self.point.y;
	def contains(self,p):
		leftBound = self.point.x;
		rightBound = self.point.x + 15;
		upBound = self.point.y - 21;
		lowBound = self.point.y + 15;
		if(p.x >= leftBound and p.x <= rightBound and p.y >= upBound and p.y <= lowBound):
			return True;
		else:
			return False;
