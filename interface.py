import pyodbc

# Replace with your actual info
server = 'LAPTOP-USGBCF7K'  # or just 'localhost'
database = 'UVAS_VetClinicDB'
        # if using SQL authentication

# For Windows Authentication, use this:
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    f'SERVER={server};'
    f'DATABASE={database};'
    'Trusted_Connection=yes;'     # Remove if using SQL login
)

cur = conn.cursor()
cur.execute('''Select * From Pets''')
for row in cur.fetchall():
        print(row)

conn.close()

