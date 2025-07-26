import pyodbc

server = 'LAPTOP-USGBCF7K'  
database = 'UVAS_VetClinicDB'
       
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    f'SERVER={server};'
    f'DATABASE={database};'
    'Trusted_Connection=yes;'     
)

def menu():
        print("""What you want to do?
              1- Fetch data.
              2- Enter data.
              3- Update data.
              4- Delete data.""")

def fetch_menu():
        print("""Which Data you want to fetch?
              1- Pets.
              2- Treatments.
              3- Appointments.
              4- Medicines.
              5- Bills.
              6- Vaccinations.""")
        
def input_menu():
        print("""Which data you want to Enter?
              1- Pets.
              2- Treatments.
              3- Appointments.
              4- Medicines.
              5- Bills.
              6- Vaccinations.""")
        
def update_menu():
        print("""Which data you want to Update?
              1- Pets.
              2- Treatments.
              3- Appointments.
              4- Medicines.
              5- Bills.
              6- Vaccinations.""")
        
def delete_menu():
        print("""Which data you want to Delete?
              1- Pets.
              2- Treatments.
              3- Appointments.
              4- Medicines.
              5- Bills.
              6- Vaccinations.""")
        


cur = conn.cursor()

menu()
option = input("Enter option = ")

if option == '1':
        fetch_menu()
        fetch = input("Enter option = ")
        if fetch== '1':
                print("Pets info")
        elif fetch=='2':
                print("Treatment info")
        elif fetch == '3':
                print("Appointment info")
        elif fetch == '4':
                print("Meddicine info")
        elif fetch == '5':
                print("Bills")
        elif fetch == '6':
                print("Vaccination info")
        else:
                print("Invalid input")

elif option == '2':
        input_menu()
        inpt = input("Enter option = ")
        if inpt== '1':
                print("Pets info")
        elif inpt=='2':
                print("Treatment info")
        elif inpt == '3':
                print("Appointment info")
        elif inpt == '4':
                print("Meddicine info")
        elif inpt == '5':
                print("Bills")
        elif inpt == '6':
                print("Vaccination info")
        else:
                print("Invalid input")

elif option == '3':
        update_menu()
        upd = input("Enter option = ")
        if upd== '1':
                print("Pets info")
        elif upd=='2':
                print("Treatment info")
        elif upd == '3':
                print("Appointment info")
        elif upd == '4':
                print("Meddicine info")
        elif upd == '5':
                print("Bills")
        elif upd == '6':
                print("Vaccination info")
        else:
                print("Invalid input")

elif option == '4':
        dele = input("Enter option = ")
        if dele== '1':
                print("Pets info")
        elif dele=='2':
                print("Treatment info")
        elif dele == '3':
                print("Appointment info")
        elif dele == '4':
                print("Meddicine info")
        elif dele == '5':
                print("Bills")
        elif dele == '6':
                print("Vaccination info")
        else:
                print("Invalid input")

        

conn.close()

