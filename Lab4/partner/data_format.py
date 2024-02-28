# authors: Thomas Brock and Pong Phimnualsri

def get_book_info():
    """
    Converts the user's inputs about a book into a string.
    :return: Book title, ISBN, Author Surname, Publisher, Year, Price in USD, rounded_price, year_by_string, string
    """
    # User inputs for book, includes changing inputs to strings and floats
    book_title = str.title(input("Enter the book title: ")).strip()
    isbn = str(input("Enter ISBN: ").strip())
    author = str.capitalize(input("Enter author's last name: ")).strip()
    publisher = str.title(input("Enter publisher's name: ")).strip()
    year_published = int(input("Enter publication year: ").strip())
    book_price_usd = float(input("Enter price in USD: "))
    rounded_price = round(book_price_usd, 2)
    rounded_string = f'{rounded_price:.2f}'
    # year_by_string = str(year_published)  # no longer necessary due to line 19

    book_info_string = "%s/%s/%s/%s/%d/%s" % (book_title, isbn, author, publisher, year_published, rounded_string)

    return book_info_string


# csv string
def convert_to_csv_format(book_info_data):
    """
    Converts the inputs into a csv string.
    :return: book_info_csv
    """
    # book_info_csv = (f'{book_title.strip().title()}/{isbn.strip()}/{author.strip().title()}/'
    #                 f'{publisher.strip().title()}/{year_published}/{book_price_usd:.2f}'
    # There are 4 steps -
    # 1 - identify string components
    # 2 - remove / from components
    # 3 - combine with commas
    # 4 - return as a new csv string
    book_info_csv = book_info_data
    return book_info_csv.replace("/", ",")


# json string
def convert_to_json_format(book_info_csv):
    """
    Converts the csv string into a json string.
    :return: book_info_json
    """
    # json string
    # converts the inputs into a json string
    # book_info_json = (('{"book_title":"%s","isbn":"%s","author":"%s",'
    #                  '"publisher":"%s","year_published":%d,"book_price_usd":%.2f}')
    #                 % (book_title.title(), isbn, author.capitalize(),
    #                     publisher.title(), year_published, book_price_usd)
    # There are 4 steps -
    # 1 - separate csv components
    # 2 - identify each component (from 0-5)
    # 3 - re-write as a json
    # 4 - return as a new json string
    book_info_json_hold = book_info_csv.split(",")
    book_json_1 = book_info_json_hold[0]
    book_json_2 = book_info_json_hold[1]
    book_json_3 = book_info_json_hold[2]
    book_json_4 = book_info_json_hold[3]
    book_json_5 = book_info_json_hold[4]
    book_json_6 = book_info_json_hold[5]

    book_info_json = (('{"book_title":"%s","isbn":"%s","author":"%s",'
                      '"publisher":"%s","year_published":%s,"book_price_usd":%s}')
                      % (book_json_1.title(), book_json_2, book_json_3.capitalize(),
                      book_json_4.title(), book_json_5, book_json_6))

    return book_info_json


# Executables
def main():
    """
    main function to get book info, convert to CSV and JSON format then printed it.
    :return: printed of book info and CSV,JSON format of it
    :rtype: str
    """
    book_info_data = get_book_info()
    csv_format_string = convert_to_csv_format(book_info_data)
    book_info_json = convert_to_json_format(csv_format_string)

    print(book_info_data)
    print("CSV Format String:")
    print(csv_format_string)
    print("JSON Format String:")
    print(book_info_json)


if __name__ == '__main__':
    main()
