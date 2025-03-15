import sqlite3

def is_user_in_table(user_id: int) -> bool:    # Проверка на наличе пользователя в таблице
    with sqlite3.connect('database_hackaton.db') as con:
        cur = con.cursor()
        cur.execute('SELECT * FROM Users WHERE user_id = ?', (user_id,))

        if cur.fetchone() is None:
            return False
        return True
    




def get_value_db(table: str, id: int) -> str | int:
    
    match table:
        case "Users":
            with sqlite3.connect('database_hackaton.db') as con:
                cur = con.cursor()
                cur.execute(f"SELECT * FROM Users WHERE chat_id = ?", (id,))
            
        case "Cards":
            with sqlite3.connect('database_hackaton.db') as con:
                cur = con.cursor()
                cur.execute(f"SELECT * FROM Cards WHERE user_id = ?", (id,))

    return cur.fetchall()
        

def set_value_db(table: str, id: int, new_value: str | int, column: str | None = None) -> None:

    match table:
        case "Users":
            with sqlite3.connect('database_hackaton.db') as con:
                cur = con.cursor()
                cur.execute(f"UPDATE Users SET {column} = ? WHERE chat_id = ?", (new_value, id))
            
        case "Cards":
            with sqlite3.connect('database_hackaton.db') as con:
                cur = con.cursor()
                cur.execute(f"UPDATE Cards SET {column} = ? WHERE card_id = ?", (new_value, id))
            
			

def create_user(user_id: int, name: str) -> int:    # Шаг 1

    with sqlite3.connect('database_hackaton.db') as con:
        cur = con.cursor()

        cur.execute("INSERT INTO Users (user_id, username) VALUES (?, ?)", (user_id, name))

        last_row_id = cur.lastrowid

    return last_row_id


def create_card(user_id: int, card_name, category, cashback) -> int:    # Шаг 1

    with sqlite3.connect('database_hackaton.db') as con:
        cur = con.cursor()
        cur.execute("INSERT INTO Cards (user_id, card_name, category, cashback) VALUES (?, ?, ?, ?)", (user_id, card_name, category, cashback))

        last_row_id = cur.lastrowid

    return last_row_id
            

# def create(chat_id: int, lvl: str, name: str, private_mode: int | None = None, file_id: str | None = None, file_type: str | None = None) -> int:    # Шаг 2

#     vertex_id = int(get_value_db("Users", "path", chat_id).split("\\")[-1].split(":")[-1])

#     next_vertices = get_value_db("Folders", "next_vertices", vertex_id).split(";")
#     next_vertices = [] if next_vertices[0] == "" else next_vertices

#     if lvl == "fold":
#         cnt_users = get_value_db("Folders", "count_of_users", vertex_id)
#     else:
#         cnt_users = None
#     print("8: ", cnt_users, vertex_id)

#     with sqlite3.connect('database_hackaton.db') as con:
#         cur = con.cursor()
#         if lvl == "fold":
#             cur.execute("INSERT INTO Folders (private_mode, name, autor_id, count_of_users) VALUES (?, ?, ?, ?)", (private_mode, name, chat_id, cnt_users))
#         else:
#             cur.execute("INSERT INTO Files (file_id, name, file_type) VALUES (?, ?, ?)", (file_id, name, file_type))
#         last_row_id = cur.lastrowid
    
        
    # with sqlite3.connect('database_hackaton.db') as con:
    #     cur = con.cursor()
    #     set_value_db("Folders", "next_vertices", vertex_id, ";".join([*next_vertices, f"{'F' if lvl == 'fold' else 'D'}:{last_row_id}"]))
    
    # return last_row_id

