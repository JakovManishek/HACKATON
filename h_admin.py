import sqlite3



def create_db():
    try:
        with sqlite3.connect('database_hackaton.db') as con:
            cur = con.cursor()
    
            cur.execute("""CREATE TABLE IF NOT EXISTS Users (
						user_id INTEGER PRIMARY KEY,
						username TEXT
						)""")
            
            cur.execute("""CREATE TABLE IF NOT EXISTS Cards (
						card_id INTEGER PRIMARY KEY,
						user_id INTEGER,
						card_name TEXT,
						category TEXT,
						cashback REAL
						)""")

        return True
        
    except Exception as ex:
        print(ex)


create_db()