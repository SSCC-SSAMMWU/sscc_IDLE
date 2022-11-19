import pandas as pd
import sqlite3


conn = sqlite3.connect("../SSCC_BOOKS.db", check_same_thread=False)
conn.row_factory = sqlite3.Row
cur = conn.cursor()

conn.execute(
    "CREATE TABLE IF NOT EXISTS BOOKS_TB (ID INTEGER PRIMARY KEY AUTOINCREMENT, ISBN INTEGER, TITLE TEXT, AUTHOR TEXT, PUBLISHER TEXT, TAG TEXT)"
)

# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)


DF = pd.read_csv("../도서 파일.csv", encoding="utf-8", names=["ID", "ISBN", "TITLE", "AUTHOR", "PUBLISHER", "TAG"])
DF["TITLE"].str.strip()
DF["AUTHOR"].str.strip()
DF["PUBLISHER"].str.strip()
DF["TAG"].str.strip()

DF.to_sql("BOOKS_TB", conn, if_exists="append", index=False);
