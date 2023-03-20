import sqlite3

db_n = input("What name do you want your database to be?")
tab_n = input("What name do you want your table to be?")

db = 'instance/'+db_n+'.db'

def schema():
    
    conn = sqlite3.connect(db)

    cursor = conn.cursor()
    
    results = cursor.execute("PRAGMA table_info('car')").fetchall()

    for row in results:
        print(row)

    conn.close()
    
schema()

def read():
    conn = sqlite3.connect(db)

    cursor = conn.cursor()
    
    results = cursor.execute('SELECT * FROM {tab_n}').fetchall()

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
        cursor.execute("INSERT INTO {tab_n} (_manufacturer, _model, _price) VALUES (?, ?, ?)", (manufacturer, model, price))
        
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
        cursor.execute("UPDATE {tab_n} SET _price = ? WHERE _model = ?", (price, model))
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
        cursor.execute("DELETE FROM {tab_n} WHERE _model = ?", (model,))
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
        
try:
    menu()
except:
    print("Perform Jupyter 'Run All' prior to starting menu")