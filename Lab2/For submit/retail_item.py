# authors: Pongsatorn Phimnualsri, Wai Wah Ng


def main():
    """
    Main function use to request all inputs and do the calculation process for the subtotal and tax in USD.
    :return: print result of the sale receipt
    """
    # get item input from user
    item_name = get_retail_item_description()
    quantity = get_number_of_purchased_items()
    price_usd_per_unit = get_price_usd_per_unit()
    tax_rate = get_tax_rate()

    # calculate subtotal, tax and total
    subtotal_usd = calculate_subtotal_usd(quantity, price_usd_per_unit)
    tax_usd = calculate_tax_usd(subtotal_usd, tax_rate)
    total_usd = calculate_total_usd(subtotal_usd, tax_usd)

    # result
    print("\nSale Receipt:")
    print("Item Description: ", item_name)
    print("Quantity: ", quantity)
    print("Price per Unit(USD): ", price_usd_per_unit)
    print("Tax Rate: ", tax_rate)
    print("Subtotal(USD): ", subtotal_usd)
    print("Tax Amount(USD): ", tax_usd)
    print("Total Amount(USD): ", total_usd)


def get_retail_item_description():
    """
    prompt the user to input retail item description
    :return: retail item description
    """
    item_name = input('Enter retail item description: ')
    return item_name


def get_number_of_purchased_items():
    """
    prompt the user to input quantity purchased
    :return: the quantity purchased
    """
    quantity = int(input('Enter quantity purchased: '))
    return quantity


def get_price_usd_per_unit():
    """
    prompt the user to input item price per unit in USD
    :return: item price per unit in USD
    """
    price_usd_per_unit = float(input('Enter price in usd: '))
    return price_usd_per_unit


def get_tax_rate():
    """
    prompt the user to input tax rate in floating number
    :return: tax rate in floating number
    """
    tax_rate = float(input('Enter tax rate in 0.00 format: '))
    return tax_rate


def calculate_subtotal_usd(quantity, price_usd_per_unit):
    """
    calculates and returns the subtotal amount in USD
    :param quantity: the quantity of item purchased
    :param price_usd_per_unit: price per unit in USD
    :return: the subtotal amount in USD
    """
    subtotal_usd = quantity * price_usd_per_unit
    return subtotal_usd


def calculate_tax_usd(subtotal_usd, tax_rate):
    """
    calculates and returns the tax amount in USD
    :param subtotal_usd: the subtotal amount in USD
    :param tax_rate: the tax rate
    :return: the tax amount in USD
    """
    tax_usd = subtotal_usd * tax_rate
    return tax_usd


def calculate_total_usd(subtotal_usd, tax_usd):
    """
    calculates and returns the total amount in USD
    :param subtotal_usd: the subtotal amount in USD
    :param tax_usd: the tax amount in USD
    :return: the total amount in USD
    """
    total_usd = subtotal_usd + tax_usd
    return total_usd

if __name__ == "__main__":  # main guard
    main()
