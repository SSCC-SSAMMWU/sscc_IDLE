import sqlite3


conn = sqlite3.connect("SSCC_BOOKS.db", check_same_thread=False)
conn.row_factory = sqlite3.Row
cur = conn.cursor()
# 아쿠아포닉스 전체 데이터 저장
conn.execute(
    "CREATE TABLE IF NOT EXISTS BOOKS_TB (ID INTEGER PRIMARY KEY AUTOINCREMENT, ISBN INTEGER, TITLE TEXT, AUTHOR TEXT, PUBLISHER TEXT, TAG TEXT)"
)

import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


DF = pd.read_csv("../도서 파일.csv", encoding="utf-8", names=["ID", "ISBN", "TITLE", "AUTHOR", "PUBLISHER", "TAG"])
DF["TITLE"].str.strip()
DF["AUTHOR"].str.strip()
DF["PUBLISHER"].str.strip()
DF["TAG"].str.strip()

DF.to_sql("BOOKS_TB", conn, if_exists="append", index=False);


# def InsertData(data):
#     try:
#         cur.execute(
#             'INSERT INTO AQUA_PONICS_TB (ISBN, TITLE, AUTHOR, PUBLISHER, TAG) VALUES (?, ?, ?, ?, ?, ?)',
#             (data.ISBN, data.TITLE, data.AUTHOR, data.PUBLISHER, data.TAG)
#         )
#         conn.commit()
#     except:
#         ERROR_CANT_SAVE_DATA_FROM_DB(error="Posted Data Type Error")
