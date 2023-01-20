from tabulate import tabulate


# ========The beginning of the class==========

class Shoe:
    # The constructor
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # The method to get the total cost of the shoes
    def get_cost(self):
        return self.cost

    # The method to get the quantity of the shoes
    def get_quantity(self):
        return self.quantity

    # The method to set the total cost of the shoes
    def set_quantity(self, quantity):
        self.quantity = quantity
        return self.quantity

    # ========The end of the class==========

    # The string representation of the class
    def __str__(self):
        # Return a string representation
        return "Country: " + self.country + " Code: " + self.code + " Product: " + \
               self.product + " Cost: " + str(self.cost) + " Quantity: " + str(self.quantity)



shoe_list = []


# ==========Functions outside the class==============
# The function to read the file
def read_shoes_data():
    try:
        line_num = 0
        # open the file inventory.txt and read the data from this file
        with open("inventory.txt", "r") as file:
            # Iterate through the file
            for line in file:
                # Skip the first line
                if line_num != 0:
                    # Split the line into a list
                    line = line.split(",")
                    # Create a shoes object with this data
                    shoe = Shoe(line[0], line[1], line[2], float(line[3]), int(line[4]))
                    # Append this object into the shoes list
                    shoe_list.append(shoe)
                line_num += 1
    except IOError:
        print("Error: File does not appear to exist.")
    except ValueError:
        print("Error: File contains invalid data.")
    finally:
        print("\nFile read successfully.\n")
        return shoe_list


# The function to capture new shoes
def capture_shoes():
    # get the data from the user
    country = input('Enter the country: ')
    code = input('Enter the code: ')
    product = input('Enter the product: ')
    cost = float(input('Enter the cost: '))
    quantity = int(input('Enter the quantity: '))
    # create a shoe object
    shoe = Shoe(country, code, product, cost, quantity)
    # append this object inside the shoe list
    shoe_list.append(shoe)
    # This quantity should be updated on the file for this shoe.
    with open("inventory.txt", "w") as file:
        file.write("Country,Code,Product,Cost,Quantity" + "\n")
        for shoe in shoe_list:
            file.write(shoe.country + "," + shoe.code + "," + shoe.product + "," + str(shoe.cost) + "," + str(
                shoe.quantity) + "\n")

    print('\nShoe added successfully.')
    return shoe_list


# The function to view all the shoes in inventorys
def view_all():
    # Table list
    table = []
    # Iterate through the list and print the details of the shoes
    for shoe in shoe_list:
        table.append([shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity])
    print(tabulate(table, headers=["Country", "Code", "Product", "Cost", "Quantity"], tablefmt="grid"))
    return shoe_list


# The function to update the stock quantity
def re_stock():
    # Find the shoe object with the lowest quantity
    lowest = shoe_list[0]
    for shoe in shoe_list:
        if shoe.quantity < lowest.quantity:
            lowest = shoe
    print(f'''\nThe shoe that needs to be re-stocked is', {lowest.product}
It has a quantity of {lowest.quantity}\n''')
    # Ask the user if they want to add this quantity of shoes
    add = input('Do you want to add this quantity of shoes? (y/n): ')

    # Check if the user wants to add this quantity of shoes
    if add == 'y':
        add = int(input('Enter the quantity to add: '))  # get the quantity to add
        lowest.quantity += add  # add the quantity to the shoe object
        print('\nThe new quantity is', lowest.quantity)  # print the new quantity
    else:
        print('\nThe quantity was not updated.')
        # This quantity should be updated on the file for this shoe.
    with open("inventory.txt", "w") as file:
        file.write("Country,Code,Product,Cost,Quantity" + "\n")
        for shoe in shoe_list:
            file.write(shoe.country + "," + shoe.code + "," + shoe.product + "," + str(shoe.cost) + "," + str(
                shoe.quantity) + "\n")
    print("\nFile updated successfully.\n")
    return shoe_list


# The function to search for a shoe
def search_shoe():
    # get the shoe code from the user
    code = input('Enter the code: ')

    # Iterate through the list and find the shoe with the code
    for shoe in shoe_list:
        if shoe.code == code:
            print(f"\nShoe found: {shoe.product}. There are {shoe.quantity} in stock.\n")
            return shoe
    print('\nThe shoe was not found.\n')
    return shoe_list[0]


# The function to calculate the value of items in inventory
def value_per_item():
    # Calculate the total value for each item
    for shoe in shoe_list:
        value = shoe.cost * shoe.quantity
        print('\nThe total stock value of', shoe.product, 'is R', value)


# The function to determine the quantity of shoes in inventory
def highest_qty():
    # determine the product with the highest quantity
    highest = shoe_list[0]
    # Iterate through the list and find the shoe with the highest quantity
    for shoe in shoe_list:
        if shoe.quantity > highest.quantity:
            highest = shoe
    print(f'''\nThe shoe with the highest quantity is {highest.product}.
It has a quantity of {highest.quantity}.\n''')
    return shoe_list


# Main function
if __name__ == '__main__':
    # Loop until the user wants to exit
    while True:
        print('''Main Menu:
    1. Read the file
    2. Capture shoes
    3. View all
    4. Re-stock
    5. Search shoe
    6. Total value per item
    7. Highest quantity
    8. Exit
    ''')
        try:
            choice = int(input('Enter your choice: '))
            if choice == 1:
                read_shoes_data()
            elif choice == 2:
                capture_shoes()
            elif choice == 3:
                view_all()
            elif choice == 4:
                re_stock()
            elif choice == 5:
                search_shoe()
            elif choice == 6:
                value_per_item()
            elif choice == 7:
                highest_qty()
            elif choice == 8:
                print('\nGoodbye!')
                break
            else:
                continue
        except ValueError:  
            print('\nInvalid choice. Please try again!\n')
            continue

# ====================================== REFERENCES ======================================
# Learning how to tabulate data
# https://pypi.org/project/tabulate/

# ========================================================================================


