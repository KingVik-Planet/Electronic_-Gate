import time

# Electronic shop dictionary data
shops = [
    {
        "name": "Occasion Technology Shop",
        "address": {
            "housenumber": 12,
            "street": "KN 121 Street"
        },
        "craft": "electronics_repair",
        "description": "Occasion Technology Shop: Sells and buys used electronic devices such as telephones, radios, televisions, and computers. No internet access. Accepts cash payments. Wheelchair accessible. Contact: +250 728 294 682.",
        "internet_access": "no",
        "operator": "Seller&buyer",
        "payment": {
            "cards": "no",
            "cash": "yes",
            "credit_cards": "no",
            "debit_cards": "no"
        },
        "phone": "+250 728 294 682",
        "wheelchair": "yes",
        "price_ranges": "rwf 1200 - 5000",
        "latitude": "",
        "longitude": ""
    },
    {
        "name": "ElectroHub",
        "address": {
            "housenumber": 45,
            "street": "KG 14 Ave"
        },
        "craft": "electronics_sales",
        "description": "ElectroHub: Specializes in new and used electronic devices, including smartphones, laptops, and accessories. Free Wi-Fi available. Accepts both cash and card payments. Wheelchair accessible.",
        "internet_access": "yes",
        "operator": "ElectroHub Ltd",
        "payment": {
            "cards": "yes",
            "cash": "yes",
            "credit_cards": "yes",
            "debit_cards": "yes"
        },
        "phone": "+250 728 123 456",
        "wheelchair": "yes",
        "price_ranges": "rwf 2000 - 15000",
        "latitude": "",
        "longitude": ""
    },
    {
        "name": "TechMart",
        "address": {
            "housenumber": 89,
            "street": "KK 23 Rd"
        },
        "craft": "electronics_sales",
        "description": "TechMart: Offers a wide range of electronic gadgets and repair services. Internet access available. Accepts all major payment methods. Wheelchair accessible.",
        "internet_access": "yes",
        "operator": "TechMart Co",
        "payment": {
            "cards": "yes",
            "cash": "yes",
            "credit_cards": "yes",
            "debit_cards": "yes"
        },
        "phone": "+250 728 789 012",
        "wheelchair": "yes",
        "price_ranges": "rwf 3000 - 20000",
        "latitude": "",
        "longitude": ""
    }
]


# Welcome function
def welcome_message():
    print("\nWelcome to our Electronic Search Website!")
    print("What can we do for you today?")
    time.sleep(1)


# Search shops based on user input
def search_shops():
    print("\nPlease select what service you want:")
    print(
        "1. Repair phone\n2. Repair Television\n3. Repair charger\n4. Repair refrigerator\n5. Repair Generator\n6. Repair Laptop\n7. Repair Desktop")
    choice = int(input("Enter the number of your choice: "))

    if choice in range(1, 8):
        amount = int(input("\nEnter your budget (in RWF): "))
        payment_method = input("\nDo you want to pay by 'cash', 'card', or 'momo': ").lower()
        vip_service = input("\nDo you want VIP service (yes/no): ").lower()

        print("\nSearching for the best shop...")
        time.sleep(2)

        # Filter the best shop based on criteria
        for shop in shops:
            if shop["payment"]["cash" if payment_method == "cash" else "cards"] == "yes" and int(
                    shop["price_ranges"].split("-")[0].strip('rwf ')) <= amount:
                print(f"\nThe best shop for your needs is {shop['name']}.")
                next_step(shop)
                return

        print("\nNo shop meets your criteria. Try adjusting your search.")


# Follow-up action
def next_step(shop):
    print("\nWhat would you like to do next?")
    print("1. Call the shop\n2. Visit the shop")
    action = int(input("Enter your choice: "))

    if action == 1:
        print(f"\nHere is the contact number for {shop['name']}: {shop['phone']}")
    elif action == 2:
        address = shop['address']
        print(f"\nHere is the address for {shop['name']}: {address['housenumber']} {address['street']}")

    another_shop()


# Ask if the user wants to search another shop
def another_shop():
    again = input("\nDo you want to search for another shop? (yes/no): ").lower()
    if again == "yes":
        search_shops()
    else:
        print("\nThank you for using our Electronic Search Website. We appreciate your visit!")


# Main function
def main():
    while True:
        welcome_message()
        search_shops()


# Run the program
if __name__ == "__main__":
    main()
