import sqlite3

db = 'instance/cars.db'

def schema():
    
    conn = sqlite3.connect(db)

    cursor = conn.cursor()
    
    results = cursor.execute("PRAGMA table_info('car')").fetchall()

    for row in results:
        print(row)

    conn.close()
    
schema()

def init_table():
    conn = sqlite3.connect(db)

    cursor = conn.cursor()

    cursor.execute(f"""CREATE TABLE car ( _manufacturer TEXT NOT NULL, _model TEXT, _price INTEGER);""")

    cursor.close()
    conn.commit()
    conn.close()

#init_table()


def read():
    conn = sqlite3.connect(db)

    cursor = conn.cursor()
    
    results = cursor.execute('SELECT * FROM car').fetchall()

    if len(results) == 0:
        print("Table is empty")
    else:
        for row in results:
            print(row)

    cursor.close()
    conn.close()

def create():
    manufacturer = input("Enter the manufacturer of the car:")
    model = input("Enter the model of the car:")
    price = input("Enter the price of the car:")
    
    conn = sqlite3.connect(db)

    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO car (_manufacturer, _model, _price) VALUES (?, ?, ?);", (manufacturer, model, price))
        
        conn.commit()
        print(f"A new car record {model} has been created")
                
    except sqlite3.Error as error:
        print("Error while executing the INSERT:", error)

    cursor.close()
    conn.close()

def update():
    model = input("Enter the model to update")
    price = input("Enter updated price")

    conn = sqlite3.connect(db)

    cursor = conn.cursor()

    try:
        cursor.execute("UPDATE car SET _price = ? WHERE _model = ?", (price, model))
        if cursor.rowcount == 0:
            print(f"No model {model} was not found in the table")
        else:
            print(f"The row with model {model} the password has been successfully updated")
            conn.commit()
    except sqlite3.Error as error:
        print("Error while executing the UPDATE:", error)
        
    cursor.close()
    conn.close()

def delete():
    model = input("Enter car model to delete")

    conn = sqlite3.connect(db)

    cursor = conn.cursor()

    try:
        cursor.execute("DELETE FROM car WHERE _model = ?", (model,))
        if cursor.rowcount == 0:
            print(f"No model {model} was not found in the table")
        else:
            print(f"The row with model {model} was successfully deleted")
        conn.commit()
    except sqlite3.Error as error:
        print("Error while executing the DELETE:", error)
        
    cursor.close()
    conn.close()

def menu():
    operations = ['c', 'r', 'u', 'd', 's']
    while True:
        operation = input("Enter: (C)reate (R)ead (U)pdate or (D)elete or (S)chema")
        if operation.lower() in operations:
            if operation.lower() == 'c':
                create()
            elif operation.lower() == 'r':
                read()
            elif operation.lower() == 'u':
                update()
            elif operation.lower() == 'd':
                delete()
            elif operation.lower() == 's':
                schema()
        elif len(operation) == 0:
            return
        else:
            print("Please enter c, r, u, or d") 
        
# try:
#     menu()
# except:
#     print("Perform Jupyter 'Run All' prior to starting menu")

menu()