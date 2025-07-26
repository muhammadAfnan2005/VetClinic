#include<iostream>
using namespace std;

void showMenu(){
    cout<<"===== VET CLINIC ====="<<endl
    <<"1. Show Treatments."<<endl
    <<"2. Add Treatment."<<endl
    <<"3. Update Treatment."<<endl
    <<"4. Delete Treatment."<<endl
    <<"5. Show pet detalis by ID"<<endl
    <<"6. Exit"<<endl
    <<"Select your choice."<<endl;
}

int main(){
    int choice;
    do{
        showMenu();
        cin>>choice;

        switch(choice){
            case 1: cout<<"treatments"; break;
            case 2: cout<<"add treatment"; break;
            case 3: cout<<"update treatment"; break;
            case 4: cout<<"delete treatment"; break;
            case 5: cout<<"show pet"; break;
            case 6: cout<<"exiting"; break;
            default: cout<< " invalid input ";
        }
    }
    while(choice != 6);
}