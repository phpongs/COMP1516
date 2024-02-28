# authors: Thomas Brock and Pongsatorn Phimnualsri


def get_book_info():
    """
    Converts the user's inputs about a book into a string.
    :return: store book code in the format "Title/ISBN/Author/Publisher/Year Published/Price(USD)"
    """
    title = str.title(input("Book Title: ").strip())
    isbn = int(input("Book ISBN: ").strip())
    author = str.title(input("Book Author Last Name: ").strip())
    publisher = str.title(input("Publisher: ").strip())
    year_published = int(input("Year Published: ").strip())
    price_usd = float(input("Price(USD): ").strip())

    return "%s/%d/%s/%s/%d/%.2f" % (title, isbn, author, publisher, year_published, price_usd)


def to_csv_format(book_info):
    """
    convert book info to CSV format.
    :param book_info: book info in the format "Title/ISBN/Author/Publisher/Year Published/Price(USD)"
    :return: store book info in CSV format.
    csv =
    "Title,ISBN,Author,Publisher,Year Published,Price(USD)"
    """
    return book_info.replace("/", ",")


def to_json_format(csv):
    """
    convert stored CSV of book info to JSON format.
    :param csv: book info to CSV format
    :return: store book info in JSON format.
    book_json =
    {
        "Title": Book Title
        "ISBN": Book ISBN
        "Author": Book Author Last Name
        "Publisher": Book Publisher
        "Year Published": Year Published
        "Price(USD)": Price in USD
    }
    """
    csv_split = csv.split(",")
    json_title = csv_split[0]
    json_isbn = int(csv_split[1])
    json_author = csv_split[2]
    json_publisher = csv_split[3]
    json_year_published = int(csv_split[4])
    json_price_usd = float(csv_split[5])

    book_json = (
        '{"Title": "%s","ISBN": "%d","Author": "%s","Publisher": "%s","Year Published": %d,"Price(USD))": %.2f}'
        % (json_title, json_isbn, json_author, json_publisher, json_year_published, json_price_usd)
        )
    return book_json


def main():
    """
    main function to get book info, convert to CSV and JSON format then printed it.
    :return: printed of book info and CSV,JSON format of it
    """
    book_info = get_book_info()
    csv = to_csv_format(book_info)
    json = to_json_format(csv)

    print(f"\nBook Database")
    print(f"Book Info:\n{book_info}\n")
    print(f"CSV Format String:\n{csv}\n")
    print(f"JSON Format String:\n{json}\n")


if __name__ == '__main__':
    main()
