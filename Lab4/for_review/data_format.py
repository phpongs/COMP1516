# author: Pongsatorn Phimnualsri, Thomas


def get_book_info():
    """
    get book info from user input.
    :return: store book code in the format "Title/ISBN/Author/Publisher/Year Published/Price(USD)"
    :rtype: str
    """
    title = str.capitalize(input("Book Title: ").strip())
    isbn = int(input("Book ISBN: ").strip())
    author = str.capitalize(input("Book Author Last Name: ").strip())
    publisher = str.capitalize(input("Publisher: ", ).strip())
    yr_published = int(input("Year Published: ").strip())
    price_usd = float(input("Price(USD): ").strip())

    return "%s/%d/%s/%s/%d/%.2f" % (title, isbn, author, publisher, yr_published, price_usd)


def to_csv_format(book_code):
    """
    convert book info to CSV format.
    :param book_code: book info in the format "Title/ISBN/Author/Publisher/Year Published/Price(USD)"
    :type book_code: str
    :return: store book info in CSV format.
    :rtype: str
    """
    return book_code.replace("/", ",")


def to_json_format(csv):
    """
    convert stored CSV of book info to JSON format.
    :param csv: book info to CSV format
    :type csv: str
    :return: store book info in JSON format.
    :rtype: dict
    """
    csv_split = csv.split(",")
    json = {
        "Title": csv_split[0],
        "ISBN": int(csv_split[1]),
        "Author": csv_split[2],
        "Publisher": csv_split[3],
        "Year Published": int(csv_split[4]),
        "Price(USD)": float(csv_split[5]),
    }
    return json


def main():
    """
    main function to get book info, convert to CSV and JSON format then printed it.
    :return: printed of book info and CSV,JSON format of it
    :rtype: str
    """
    book_code = get_book_info()
    csv = to_csv_format(book_code)
    json = to_json_format(csv)

    print(f"\nBook Database")
    print(f"Book Code: {book_code}")
    print(f"CSV: {csv}")
    print(f"JSON: {json}")


if __name__ == '__main__':
    main()
