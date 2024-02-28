# authors: Pongs & Wai Wah Ng

import retail_item_modules


def main():
    """
    Based on the inputs from users, program calculate the total amount of a retail item purchased
    and the quantity of the item and tax rate are considered.
    :return: total amount including tax in usd
    """
    # obtain input information
    item_description = retail_item_modules.get_retail_item_description()
    number_purchased = retail_item_modules.get_number_of_purchased_items()
    unit_price_usd = retail_item_modules.get_price_usd_per_unit()
    tax_rate_float = retail_item_modules.get_tax_rate()

    # calculate subtotal, tax, and total in usd based on input
    subtotal_usd = retail_item_modules.calculate_subtotal_usd(unit_price_usd, number_purchased)
    tax_usd = retail_item_modules.calculate_tax_usd(subtotal_usd, tax_rate_float)
    total_usd = retail_item_modules.calculate_total_usd(subtotal_usd, tax_usd)

    # print result
    print("Sales Receipt")
    print("Item Description:", item_description)
    print("Number of Purchased items:", number_purchased)
    print("Unit Price (usd):", unit_price_usd)
    print("Tax Rate:", tax_rate_float)
    print("Subtotal:", subtotal_usd, "(usd)")
    print("Tax:", tax_usd, "(usd)")
    print("Total:", total_usd, "(usd)")


if __name__ == "__main__":  # main guard
    main()

