import pyodbc
import tkinter as tk

formatTemp1 = '{0:<7}{1:<20}{2:<15}{3:<13}{4:<20}{5:<15}{6:15}'
formatTemp2 = '{0:<7}{1:<15}{2:<20}{3:<20}{4:<18}{5:<25}'

#Grabs Microsoft Database, extracts * (all) values from Movie_List and prints it
def show_records():
    conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\2019002577\source\repos\assessment_2sol\assessment_2\data\assessment2.accdb;')
    
    cursor = conn.cursor()
    
    cursor.execute('select * from Movie_List')

    print(f'{"ID":<7}{"Movie Name":<20}{"Release Date":<15}{"Genre":<13}{"Maturity Rating":<20}{"Star Rating":<15}{"Views":<15}')
    print(f'{"_":_<96}')

    for row in cursor.fetchall():
        record = f'{row.ID:<7}{row.Movie_Name:<20}{row.Release_Date:<15}{row.Genre:<13}{row.Maturity_Rating:<20}{row.Star_Rating:<15}{row.Views:<15}'

        print(record)

    print('\n\n')
#Grabs Microsoft Database, extracts * from Customer_Details table and prints it
def show_customers():
    conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\2019002577\source\repos\assessment_2sol\assessment_2\data\assessment2.accdb;')
    
    cursor = conn.cursor()
    
    cursor.execute('select * from Customer_Details')
    
    print(f'{"ID":<7}{"Customer Name":<15}{"Membership Type":<20}{"Customer Email":<20}{"Movies Watched":<18}{"Member Since":<25}')
    print(f'{"_":_<93}')

    for row in cursor.fetchall():
        record = f'{row.ID:<7}{row.Customer_Name:<15}{row.Membership_Type:<20}{row.Customer_Email:<20}{row.Movies_Watched:<18}{row.Member_Since:<25}'

        print(record)


#Grabs Database, inserts listed values into database. Commit saves changes
def enter_record():
    ID = e1.get()
    Mname = e2.get()
    Rdate = e3.get()
    Genre = e4.get()
    Mrate = e5.get()
    Srate = e6.get()
    Views = e7.get()
    
    conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\2019002577\source\repos\assessment_2sol\assessment_2\data\assessment2.accdb;')
    
    cursor = conn.cursor()
    
    cursor.execute('INSERT INTO Movie_List VALUES (?,?,?,?,?,?,?)', (ID, Mname, Rdate, Genre, Mrate, Srate, Views))
    conn.commit()

#Frontend tkinter

master = tk.Tk()

# Labels for textboxes
tk.Label(master, text ="ID").grid(row=0)
tk.Label(master, text ="Movie Name").grid(row=1)
tk.Label(master, text ="Release Date").grid(row=2)
tk.Label(master, text ="Genre").grid(row=3)
tk.Label(master, text ="Maturity Rating").grid(row=4)
tk.Label(master, text ="Star Rating").grid(row=5)
tk.Label(master, text ="Views").grid(row=6)

# Textboxes

e1=tk.Entry(master)
e2=tk.Entry(master)
e3=tk.Entry(master)
e4=tk.Entry(master)
e5=tk.Entry(master)
e6=tk.Entry(master)
e7=tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
e5.grid(row=4, column=1)
e6.grid(row=5, column=1)
e7.grid(row=6, column=1)

# Button group

tk.Button(master, text="Show", command = lambda: [show_records(), show_customers()]).grid(row=8, column=1)
tk.Button(master, text="Enter", command=enter_record).grid(row=8, column=0)
tk.Button(master, text='Quit', command=master.quit).grid(row=8, column=2)

tk.mainloop()