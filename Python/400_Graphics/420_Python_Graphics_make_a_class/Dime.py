from graphics import *;
class Dime:
	coinColor = color_rgb(83,83,87);
	def __init__(self,point):
		self.point = point;
		self.coin = Circle(point,20);
		self.coin.setFill(self.coinColor);
		self.val = Text(point,"10c");
		self.val.setFill("white");
	def draw(self,canvas):
		self.coin.draw(canvas);
		self.val.draw(canvas);
		