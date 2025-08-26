def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    If discount_percent is 20% or higher, apply the discount,
    otherwise return the original price.
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price


# Prompt the user to enter the original price and discount percentage
try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Calculate final price using the function
    final_price = calculate_discount(price, discount_percent)

    # Print result
    if discount_percent >= 20:
        print(f"Final price after applying {discount_percent}% discount: {final_price:.2f}")
    else:
        print(f"No discount applied. Original price: {final_price:.2f}")

except ValueError:
    print("Invalid input! Please enter numeric values for price and discount percentage.")
