with open("isbn.txt", "r", encoding="utf-8") as fh:
    books = fh.readlines()

cnt = 0
for book in books:
    if "\t" in book.strip():
        cnt+=1
        # print(book.strip())
    else:
        if "error" not in book:
            # print("\t")
            cnt += 1
            print(book.strip())

# print(cnt)