import json
import sqlite3

conn = sqlite3.connect("SSCC_BOOKS.db", check_same_thread=False)
conn.row_factory = sqlite3.Row
cur = conn.cursor()

def UpdateData(**props):
    cur.execute(props["query"] + " " + (props["option"] if "option" in props else ""))
    conn.commit()

def SelectData(**props):
    cur.execute(props["query"] + " " + (props["option"] if "option" in props else ""))
    __re__ = []
    for row in cur.fetchall():
        if len(row["TITLE"]) >= 97:
            __re__.append({
                "ID": row["ID"],
                "ISBN": row["ISBN"],
                "TITLE": row["TITLE"][:90] + "...",
                "AUTHOR": row["AUTHOR"],
                "PUBLISHER": row["PUBLISHER"],
                "TAG": row["TAG"]
            })
        else:
            __re__.append(row)
    return __re__

# def InsertData():
#     try:
#         cur.execute(
#             'INSERT INTO BOOKS_TB (ISBN, TITLE, AUTHOR, PUBLISHER, TAG) VALUES (?, ?, ?, ?, ?)',
#             (   )
#         )
#         conn.commit()
#         print("")
#     except:
#         print("")
