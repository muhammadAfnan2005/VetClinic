import pyodbc           #add connector
import os               #import os for clear screen before menu

#Get server and database name
server = 'LAPTOP-USGBCF7K'  
database = 'UVAS_VetClinicDB'
       
       #connect database
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    f'SERVER={server};'
    f'DATABASE={database};'
    'Trusted_Connection=yes;'     
)

def menu():                     #main menu
        os.system('cls')
        print("""What you want to do?
              1- Fetch data.
              2- Enter data.
              3- Update data.
              4- Delete data.
              Enter 'exit' to quit the program.
              """)

def fetch_menu():               
        os.system('cls')
        print("""Which Data you want to fetch?
              1- Pets.
              2- Treatments.
              3- Appointments.
              4- Medicines.
              5- Bills.
              6- Vaccinations.
              7- Owner.""")
        
def input_menu():
        os.system('cls')
        print("""Which data you want to Enter?
              1- Pets.
              2- Treatments.
              3- Appointments.
              4- Medicines.
              5- Bills.
              6- Vaccinations.
              7- Owner.""")
        
def update_menu():
        os.system('cls')
        print("""Which data you want to Update?
              1- Pets.
              2- Appointment's Time.
              3- Medicines.
              4- Bills.
              5- Vaccination date.
              6- Owner.""")
        
def delete_menu():
        os.system('cls')
        print("""Which data you want to Delete?
              1- Pets.
              2- Treatments.
              3- Appointments.
              4- Medicines.
              5- Bills.
              6- Vaccinations.""")
        


cur = conn.cursor()

while True:
        menu()

        option = input("Enter option = ")
        if option == 'exit':
                break

        #========================================== Fetch data from database===========================

        elif option == '1':
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
                        cur.execute('''SELECT * FROM Owner''')
                        for row in cur.fetchall():
                                print(row)
                else:
                        print("Invalid input")

        #===================================================Enter data in database=======================

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
                        diagnos = input("Enter diagnosis result = ")
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
                        cur.execute('''INSERT INTO Appointments(petID,vetID,Time,cause)
                                    VALUES(?,?,?,?)''',(pet,vet,time,cause))
                        conn.commit()

                elif inpt == '4':
                        print("Medicine info")
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
                        petID = input("Enter Pet ID = ")
                        name = input("Enter Vaccine name = ")
                        date = input("Enter vaccine name = ")
                        dueDate = input("Enter Next Due Date = ")
                        vetID = input("Enter Vet ID = ")
                        cur.execute('''INSERT INTO Vaccinations(petID,VaccineName,vaccinationDate,nextDueDate,vetID)
                                    VALUES(?,?,?,?,?)''',(petID,name,date,dueDate,vetID))
                        conn.commit()
                elif input == '7':
                        print("Enter Owner's data")
                        ID = input("Enter Owner ID = ")
                        name = input("Enter Owner name = ")
                        No = input("Enter Phone number = ")
                        email = input("Enter E-mail = ")
                        address = input("Enter address = ")
                        cur.execute('''INSERT INTO Owner(OwnerID,ownerName,phoneNo,Email,address)
                                    VALUES(?,?,?,?,?)''',(ID,name,No,email,address))
                        conn.commit()


                else:
                        print("Invalid input")

        #==================================================update data==========================

        elif option == '3':
                update_menu()
                upd = input("Enter option = ")
                if upd== '1':                  
                        ID = int(input("Enter pet ID = "))
                        print("""What you want to update?
                              1- Pet name.
                              2- Pet age.
                              3- Pet Specie
                              4- Pet Gender.
                              5- Pet Breed.
                              6- Pet Owner ID.""")
                        op = input("Enter option = ")
                        if op == '1':
                                name = input("Enter new name = ")
                                cur.execute('''UPDATE Pets SET petName = ? WHERE petID = ?''',(name,ID))
                                conn.commit()
                                print("Updated successfully!")
                        if op == '2':
                                age = int(input("Enter new age = "))
                                cur.execute('''UPDATE Pets SET age = ? WHERE petID = ?''',(age,ID))
                                conn.commit()
                                print("Updated successfully!")
                        if op == '3':
                                specie = input("Enter new specie = ")
                                cur.execute('''UPDATE Pets SET specie = ? WHERE petID = ?''',(specie,ID))
                                conn.commit()
                                print("Updated successfully!")
                        if op == '4':
                                gender = input("Enter new gender = ")
                                cur.execute('''UPDATE Pets SET gender = ? WHERE petID = ?''',(gender,ID))
                                conn.commit()
                                print("Updated successfully!")
                        if op == '5':
                                breed = input("Enter new breed = ")
                                cur.execute('''UPDATE Pets SET breed = ? WHERE petID = ?''',(breed,ID))
                                conn.commit()
                                print("Updated successfully!")
                        if op == '6':
                                ownID = input("Enter new Owner ID = ")
                                cur.execute('''UPDATE Pets SET OwnerID = ? WHERE petID = ?''',(ownID,ID))
                                conn.commit()
                                print("Updated successfully!")
                elif upd == '2':
                        print("Appointment info")
                        ID = input("Enter Appointment ID = ")
                        time = input("Enter new time = ")
                        cur.execute("""UPDATE Appointments SET Time = ? WHERE AppointmentID = ?""",(time,ID))
                        conn.commit()
                        print("Updated successfully!")
                elif upd == '3':
                        print("Bills")
                        ID = input("Enter Bill ID = ")
                        print("""What you want to update?
                              1- Amount.
                              2- Payment status.
                              3- payment method.""")
                        op = input("Enter option = ")
                        if op == '1':
                                amount = input("Enter amount = ")
                                cur.execute('''UPDATE Bills SET amount = ? WHERE billID = ?''',(amount,ID))
                                conn.commit()
                                print("Updates Successfully!")
                        if op == '2':
                                status = input("Enter Payment Status = ")
                                cur.execute('''UPDATE Bills SET paymentstatus = ? WHERE billID = ?''',(status,ID))
                                conn.commit()
                                print("Updates Successfully!")
                        if op == '3':
                                method = input("Enter Payment Method = ")
                                cur.execute('''UPDATE Bills SET paymentmethod = ? WHERE billID = ?''',(method,ID))
                                conn.commit()
                                print("Updates Successfully!")
                elif upd == '4':
                        print("Vaccination info")
                        ID = input("Enter Vaccination ID = ")
                        date = input("Enter date = ")
                        due_date = input("Enter next due date = ")
                        cur.execute('''UPDATE Vaccinations SET vaccinationDate = ?,nextDueDate = ? WHERE vaccinationID = ?''',(date,due_date,ID))
                        conn.commit()
                        print("Updated Succcessfully!")
                else:
                        print("Invalid input")

        #===========================================Dlete Data================================

        elif option == '4':
                dele = input("Enter option = ")
                if dele== '1':
                        print("Pets info")
                        ID = input("Enter pet ID for deletion = ")
                        cur.execute('''DELETE FROM Pets WHERE petID = ''',(ID,))
                        conn.commit()
                        print("Deleted Successfully!")
                elif dele=='2':
                        print("Treatment info")
                        ID = input("Enter Treatment ID for deletion = ")
                        cur.execute('''DELETE FROM Treatments WHERE treatmentID = ''',(ID,))
                        conn.commit()
                        print("Deleted Successfully!")
                elif dele == '3':
                        print("Appointment info")
                        ID = input("Enter Appointment ID for deletion = ")
                        cur.execute('''DELETE FROM Appointments WHERE AppointmentID = ''',(ID,))
                        conn.commit()
                        print("Deleted Successfully!")
                elif dele == '4':
                        print("Medicine info")
                        ID = input("Enter Medicine ID for deletion = ")
                        cur.execute('''DELETE FROM Medicines WHERE medicineID = ''',(ID,))
                        conn.commit()
                        print("Deleted Successfully!")
                elif dele == '5':
                        print("Bills")
                        ID = input("Enter Bill ID for deletion = ")
                        cur.execute('''DELETE FROM Bills WHERE billID = ''',(ID,))
                        conn.commit()
                        print("Deleted Successfully!")
                elif dele == '6':
                        print("Vaccination info")
                        ID = input("Enter Vaccination ID for deletion = ")
                        cur.execute('''DELETE FROM Vaccinations WHERE vaccinationID = ''',(ID,))
                        conn.commit()
                        print("Deleted Successfully!")
                else:
                        print("Invalid input")

                

        conn.close()