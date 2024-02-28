# jason wilder
# index:   books[0]           books[1]       books[2]
books = ("thE sprint book", "getting real", "the four hour workweek",
         "save the pixel", "the five am club")


# list comprehension
f_books = [b for b in books if "f" in b]
print(f_books)

long_titles = [b for b in books if len(b) > 14]
print(long_titles)

numbers = (5, 66, 7, -8, 0, 323, 123, 325, 3, 45, 45645, 4, 3)

bigger_than_60 = tuple(n for n in numbers if n > 60)
print(bigger_than_60)


i = 0
while i < len(books):
    if "the".lower() in books[i].lower():
        print(books[i].upper())
    i += 1
