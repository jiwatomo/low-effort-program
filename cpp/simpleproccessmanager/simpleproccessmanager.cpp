#include <iostream>
#include <string>
#include <conio.h>
using namespace std;

int main() {
	while (1) {
		string mainmenu = "Proccess Manager\n1.See all proccess\n2.Kill specific proccess\ntype any to exit";
		cout<<mainmenu<<endl;
		char getmain = _getch();
		if (getmain == '1') {
			system("tasklist");
		} else if (getmain == '2') {
			int pidhandler;
			cin>>pidhandler;
			// string commandtemp = pidhandler;
			cout<<pidhandler<<endl;
		} else {
			break;
		}
	}
	cout<<"Bye"<<endl;
	return 0;
}
