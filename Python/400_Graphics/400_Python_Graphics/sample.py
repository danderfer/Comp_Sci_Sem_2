# sample graphics program
#
# imports graphics library
#
from graphics import *;


# constructs a window
window = GraphWin("Window", 500,500);

# constructs a Rectangle object
circle = Circle(Point(50,50),10);

# draws the circle in the constructed window
circle.draw(window);

# waits for the user to click the mouse in the window
window.getMouse();

# closes the window
window.close();

