# authors: Pongs & Wai Wah Ng

def get_retail_item_description():
    """
    Prompt the user to enter the description of a retail item
    :return: the description as string
    """
    retail_item_description = input("enter retail item description: ")
    return retail_item_description


def get_number_of_purchased_items():
    """
    Prompt the user to enter the quantity of the item purchased
    :return: the number of purchased items
    """
    number_of_purchased_items = int(input("enter quantity purchased: "))
    return number_of_purchased_items


def get_price_usd_per_unit():
    """
    Prompt the user to enter the unit price of the item in USD
    :return: unit price in usd
    """
    price_usd_per_unit = float(input("enter price per unit (usd): "))
    return price_usd_per_unit


def get_tax_rate():
    """
    prompts user to input tax rate in floating
    :return: tax rate in floating
    """
    tax_rate = float(input("enter tax (0.00): "))
    return tax_rate


def calculate_subtotal_usd(unit_price_usd, number_purchased):
    """
    calculate subtotal in USD by multiplication of two parameters below
    :param unit_price_usd: unit price of the item
    :param number_purchased: number of purchased item
    :return: subtotal in usd
    """
    return unit_price_usd * number_purchased


def calculate_tax_usd(subtotal_usd, tax_rate_float):
    """
    calculate the tax amount based on the multiplication of the two parameters below
    :param subtotal_usd: subtotal obtained from calculated_subtotal_usd function
    :param tax_rate_float: tax rate obtained from get_tax_rate function
    :return: tax amount in usd
    """
    return subtotal_usd * tax_rate_float


def calculate_total_usd(subtotal_usd, tax_usd):
    """
    calculate the total amount by adding the above two variables
    :param subtotal_usd: subtotal obtained from calculated_subtotal_usd function
    :param tax_usd: tax amount of the item obtained from calculate_tax_usd function
    :return: the total amount in usd
    """
    return subtotal_usd + tax_usd
