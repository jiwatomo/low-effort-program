// some declaration using indonesian language
// thanks for coming ^_^

//including
#include <iostream>
#include <string>
#include <fstream>
using namespace std;

//some code
string output,cache;
int jumlahData = -1;
void inserting(string thenama, string thenomor, string theemail);
void getting();
void deleting();
void reset();

//main function
int main() {
	
	//mainloop
	while (true) {
		
		//declaration
		int masukkan;
		char masukkan2;
		
		//main menu
		cout<<"Database client\n"
			<<"1.Insert data\n"
			<<"2.Get data\n"
			<<"3.Delete data\n"
			<<"4.Reset data\n"
			<<"0.keluar program"<<endl;
		cin>>masukkan;
		
		//input checker
		if (masukkan == 1) {
			
			//for 1 - Inserting
			string get_nama,get_nomor,get_email;
			cout<<"Nama: ";
			cin>>ws;
			getline(cin, get_nama);
			cout<<"Nomor: ";
			cin>>ws;
			getline(cin, get_nomor);
			cout<<"Email: ";
			cin>>ws;
			getline(cin, get_email);
			inserting(get_nama,get_nomor,get_email);
		} else if (masukkan == 2) {
			//for 2 - Get the data
			getting();
		} else if (masukkan == 3) {
			//for 3 (WIP)
			cout<<"Work in process";
		} else if (masukkan == 4) {
			//for 4 - Reset the data
			cout<<"Are you sure?(y/n): ";
			cin>>masukkan2;
			if (masukkan2 == 'y') {
				reset();
				cout<<"succesfully reseting"<<endl;
				continue;
			} else if (masukkan2 == 'n') {
				cout<<"task cancelled"<<endl;
			} else {
				cout<<"Wrong input"<<endl;
			}
		} else {
			break;
		}
	}
	return 0;
}

//function
void inserting(string thenama, string thenomor, string theemail) {
	ifstream theFile;
	ofstream theReadfile;
	string temp;
	theReadfile.open("dataKontak.txt", ios::app);
	theFile.open("dataKontak.txt", ios::app);
	while(getline(theFile, temp)) {
		++jumlahData;	
	}
	theReadfile<<"\n"<<jumlahData
				<<" "
				<<thenama<<" "
				<<thenomor<<" "
				<<theemail<<" "
				<<"\n";
	theReadfile.close();
	theFile.close();
}
void getting() {
	ifstream theFile;
	ofstream theReadfile;
	string temp;
	theReadfile.open("dataKontak.txt", ios::app);
	theFile.open("dataKontak.txt", ios::app);
	while(getline(theFile, temp)) {
		cout<<temp<<endl;
	}
	cout<<"--------------"<<endl;
	theFile.close();
	theReadfile.close();
	
}
void deleting() {
}
void reset() {
	ofstream theResetfile;
	theResetfile.open("dataKontak.txt", ios::trunc);
	theResetfile<<"--------------\n"<<"nomor/nama/nomorhp/email";
	theResetfile.close();
}
