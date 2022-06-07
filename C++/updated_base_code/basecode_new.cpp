// base code file
#include "./hfiles/poole.h"

///////////////////////////////////////////////////////////////////////

main(){
	srand(time(NULL));
	// write code here
	gotoxy(10,10);
	cout<<"This works!";
	framedbox(12,12,5,8,'&');
	drawbox(2,2,4,8,'^');
	drawline(10,3,10,'$');

}
