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
              4- Delete data.
              """)

def fetch_menu():
        print("""Which Data you want to fetch?
              1- Pets.
              2- Treatments.
              3- Appointments.
              4- Medicines.
              5- Bills.
              6- Vaccinations.
              7- Owner.""")
        
def input_menu():
        print("""Which data you want to Enter?
              1- Pets.
              2- Treatments.
              3- Appointments.
              4- Medicines.
              5- Bills.
              6- Vaccinations.
              7- Owner.""")
        
def update_menu():
        print("""Which data you want to Update?
              1- Pets.
              2- Treatments.
              3- Appointments.
              4- Medicines.
              5- Bills.
              6- Vaccinations.
              7- Owner.""")
        
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
                cur.execute('''SELECT * FROM Pets''')
                for row in cur.fetchall():
                        print(row)
        elif fetch=='2':
                print("Treatment info")
                cur.execute('''SELECT * FROM Treatments''')
                for row in cur.fetchall():
                        print(row)
        elif fetch == '3':
                print("Appointment info")
                cur.execute('''SELECT * FROM Appointments''')
                for row in cur.fetchall():
                        print(row)
        elif fetch == '4':
                print("Meddicine info")
                cur.execute('''SELECT * FROM Medicines''')
                for row in cur.fetchall():
                        print(row)
        elif fetch == '5':
                print("Bills")
                cur.execute('''SELECT * FROM Bills''')
                for row in cur.fetchall():
                        print(row)
        elif fetch == '6':
                print("Vaccination info")
                cur.execute('''SELECT * FROM Vaccinations''')
                for row in cur.fetchall():
                        print(row)
        elif fetch =='7':
                print("Owner info")
                print("Vaccination info")
                cur.execute('''SELECT * FROM Owner''')
                for row in cur.fetchall():
                        print(row)
        else:
                print("Invalid input")

elif option == '2':
        input_menu()
        inpt = input("Enter option = ")
        if inpt== '1':
                print("For entering a new pet, Owner details must antered first!")
                name = input("Enter pet name = ")
                specie = input("Enter pet specie = ")
                breed = input("Enter Breed = ")
                age = int(input("Enter age = "))
                gender = input("Enter pet gender = ")
                owner = input("Enter Owner ID (same as Owner table) = ")
                cur.execute('''INSERT INTO Pets(petName,species,breed,age,gender,ownerID)
                            VALUES(?,?,?,?,?,?)''',(name,specie,breed,age,gender,owner))
                conn.commit()
        elif inpt=='2':
                appID = int(input("Enter appointment ID = "))
                diagnos = input("Enter diagnpsis result = ")
                med = input("Enter Medicine = ")
                dos = input("Enter dosage of medicine = ")
                advice = input("Enter Vet's Advice = ")
                cur.execute('''INSERT INTO Treatments(appointmentID,diagnosis,medicines,dosage,advice)
                           VALUES(?,?,?,?,?) ''',(appID,diagnos,med,dos,advice))
                conn.commit()

        elif inpt == '3':
                print("Appointment info")
                pet = input("Enter pet ID = ")
                vet = input("Enter Vet ID = ")
                time = input("Enter time = ")
                cause = input("Enter disease = ")
                cur.execute('''INSERT INTO Appointment(petID,vetID,Time,cause)
                            VALUES(?,?,?,?)''',(pet,vet,time,cause))
                conn.commit()

        elif inpt == '4':
                print("Meddicine info")
                name = input("Enter Medicine name = ")
                man = input("Enter manufacturer = ")
                dose = input("Enter dosage = ")
                unit = input("Enter unit = ")
                descrip = input("Enter Description = ")
                cur.execute('''INSERT INTO Medicines(medicineName,manufacture,dose,unit,description)
                            VALUES(?,?,?,?,?)''',(name,man,dose,unit,descrip))
                conn.commit()
        elif inpt == '5':
                print("Bills")
                treatID = input('''Enter Treatment ID''')
                date = input('''Enter bill date = ''')
                amount = int(input('''Enter bill amount = '''))
                paystatus = input('''Enter payment status = ''')
                paymethod = input('''Enter payment method = ''')
                cur.execute('''INSERT INTO Bills(treatmentID,billDate,amount,paymentstatus,paymentmethod)
                            VALUES(?,?,?,?,?)''',(treatID,date,amount,paystatus,paymethod))
                conn.commit()
        elif inpt == '6':
                print("Vaccination info")
        elif input == '7':
                print("Enter Owner's data")

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

