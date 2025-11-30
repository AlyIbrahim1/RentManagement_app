import sqlite3

conn = sqlite3.connect("data/rent_management.db") # connects to database file
cursor = conn.cursor() # creates a cursor

# creates the database table
cursor.execute("""
    --sql
    CREATE TABLE IF NOT EXISTS renters (
        appartmentNumber INTEGER PRIMARY KEY,
        name TEXT,
        rentAmount INTEGER,
        lastMonthPayed TEXT,
        unpaidMonths INTEGER,
        rentDue INTEGER;
    ) 
""")
conn.commit()

def addRecord(appartmentNumber, name, rentAmount, lastMonthPayed, unpaidMonths, rentDue):
    cursor.execute("""
        --sql 
        INSERT INTO renters VALUES (?,?,?,?,?)
        ;"""
        , 
        (appartmentNumber, name, rentAmount, lastMonthPayed, unpaidMonths, rentDue)
    )
    conn.comit()

def deleteRecord(appartmentNumber):
    cursor.execute(--"""
    --sql
    DELETE FROM renters WHERE appartmentNumber = (?)
    ;
    """
    , appartmentNumber
    )

def clearTable():
    cursor.execute("DROP TABLE renters")
    conn.commit()

conn.close()