

inventory = {"Arroz":(500, 34),
             "papa":(4000, 54)
             }
# A function is defined to enter data into the inventory, such as name, price, and quantity.
# In this same function, the tuple is assigned to the dictionary with the price and quantity. These will be the key values.
# In the same function, the data type entries are validated. If the product exists, it is notified.
def add_product():
    comprobar = 0
    while comprobar < 5:
        print("\n**Add product**")
        print("")
        print("_You must enter minimum five products_")
        print("")
        name_product = input("Enter the name of product: ").capitalize().strip()
        if name_product in inventory:
            print("The product already exist.")
            try:
                go_out = input("You want to exit to the menu to verify (s) (n): ").lower().strip()
                if go_out == "s":
                    return
                elif go_out == "n":
                    continue
            except ValueError:
                print("You must enter (s) or (n).")
                continue
        else:
            while True:
                try:
                    product_price = float(input("Enter the price of the product: "))
                    if product_price <= 0:
                        print("You must enter a number higher at ziro.")
                        continue
                except ValueError:
                    print("You must enter numbers.")
                    continue
                break
        while True:
            try:
                product_amount = int(input("Enter the amount: "))
                if product_amount <= 0:
                    print("You must enter a number higher at ziro.")
                    continue
            except ValueError:
                print("You must enter numbers.")
                continue
            break
        inventory[name_product] = (product_price, product_amount)

        comprobar += 1
        print(f"The product {name_product} was added to inventory.")

# This function allows you to look up a product by its name in the dictionary, showing its price and quantity.
#Notify if the product does not exist.
def consult_product(name):
    while True:
        if name in inventory:
            price, amount = inventory[name]
            price_str = str(int(price)) if price == int(price) else str(price)
            print(f"\n{'Name'.ljust(15)}|{'Price'.ljust(12)}|{'Amount'.ljust(20)}")
            print("------------------------------------")
            print(f"{name.ljust(15)}|{price_str.ljust(12)}|{str(amount).ljust(20)}")
            break
        else:
            print("The product does not exist.")
            get_out = input("Get out the menu to add it (s): ").lower().strip()
            if get_out == "s":
                return None
            
              
    

# The function "update_products" allows you to update the price of a product.
def update_product(name, price):
    if name in inventory:
        amount = inventory[name][1]
        inventory[name] = (price, amount)
        print(f"Price of {name} update.")


# This function allows you to update the amount of a product.
def new_amount(name):
    if name in inventory:
        new_amount = int(input("Enter the new amount: "))
        value = inventory[name][0]
        inventory[name] = (value, new_amount)
    print(f"Amount of {name} was changed.")
        
            
               

# This function checks if the  product amount is zero and allows it to deleted.
# If it is not in zero, sends a message indicating that can not to deleted.
def eliminate_product(eliminate):
    amount = inventory[eliminate][1]
    if amount == 0:
        del inventory[eliminate]
        print(f"The product {eliminate} has been removed from inventory.")
    elif amount > 0:
        print(f"The product {eliminate} cannot be deleted, there are still products in the inventory.")



# This function calculates the total value of the inventory.
def value_total():
    value_total = map(lambda value: value[0] * value[1], inventory.values())
    value_total = sum(value_total)
    print(f"\nThe total value of the inventory is: {value_total:.2f} $")
    
    


# We call the function "main()" for to serve as the execution point of the program.
def main():
    while True:
        print("\n*********************")
        print("**Inventory options**")
        print("***********************\n")
        print("1. Add products.")
        print("2. Consult products.")
        print("3. Update the price of a product.")
        print("4. Delete a product.")
        print("5. Calculate the total value of the inventory.")
        print("6. Change amount.")
        print("7. Get out of the inventory.")
        try:
            option = int(input("Enter an option: "))
            if option < 1:
                print("You must enter a number between 1 and 7.")
                continue
            elif option > 7:
                print("You must enter a number between 1 and 7")
                continue
        except ValueError:
            print("You must enter numbers.")
            continue

        match option:
            case 1:
                add_product()
            case 2:
                    print("**Consult product**")
                    name_product = input("\nEnter the name of the product you want to see: ").capitalize().strip()
                    consult_product(name_product)
                    if consult_product is None:
                        break
                    else:
                        continue
            case 3:
                print("**Update price product**")
                product = input("Enter the name of the producto: ").capitalize().strip()
                if not product in inventory:
                        print("")
                        print("The product does not exist, you must enter.")
                        continue
                elif product in inventory:
                    try:
                        new_price = float(input("Enter the new price of the product: "))
                        if new_price <= 0:
                            print("You must enter a number greater than zero.")
                            continue
                    except ValueError:
                        print("You must enter numbers.")
                    update_product(product, new_price)
                        
                               
            case 4:
                eliminate = input("Enter the name of the product you want to delete: ").capitalize().strip()
                if not eliminate in inventory:
                    print("The product does not exist in inventory.")
                    break
                else:
                    eliminate_product(eliminate)
            case 5:
                print("**Total value inventory")
                print(f"\n{'Name'.ljust(15)}|{'Price'.ljust(10)}|{'Amount'.ljust(20)}")
                print("---------------------------------------------")   
                for keys, value in inventory.items():
                    price, amount = value
                    price_str = str(int(price)) if price == int(price) else (price)
                    print(f"{keys.ljust(15)}|{price_str.ljust(10)}|{str(amount).ljust(20)}")
                value_total()
            case 6:
                new = input("Enter the name of the product: ").capitalize().strip()
                if new in inventory:
                    new_amount(new)
                if not new in inventory:
                    print("The product does not exist in inventory, you must enter.")
                    continue
            case 7:
                print("**You have get out of the program**")
                break
main()
