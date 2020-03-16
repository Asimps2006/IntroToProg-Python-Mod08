# ------------------------------------------------------------------------ #
# Title: Assignment 08 - "Product Price Tracker Program"
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2020,Created started script
# RRoot,1.1.2020,Added pseudo-code to start assignment 8
# ASimpson, 03/13/2020, Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Import Modules Here
import sys

# Data -------------------------------------------------------------------- #
strFileName = 'ProductInfo.txt'
lstTable = []  # A list that acts as a 'table' of rows
strChoice = ""  # Captures the user option selection

# Processing -------- Custom Class 4 Product Info Processing -------------- #
class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name

        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        ASimpson, 03/13/2020, Modified code to complete assignment 8
    """

    # --Fields--
    # This is one of few the times a field is used as a global variable
    __counter = 0

    # -- Constructor --
    def __init__(self, product_name: str, product_price: str):
        """" Sets initial values and returns a Product object """
        # -- Attributes --
        self.__product_name = product_name
        self.__product_price = product_price.strip('$')
        # call the private method each time an object is made
        Product.__set_object_count()

    # -- Properties --
    @property  # DON'T USE NAME for this directive!
    def product_name(self):  # (getter or accessor)
        return str(self.__product_name).title()  # Title case

    @property  # DON'T USE NAME for this directive!
    def product_price(self):  # (getter or accessor)
        return float(self.__product_price)  # Float Value

    @product_name.setter  # The NAME MUST MATCH the property's!
    def product_name(self, new_name):  # (setter or mutator)
        # Added a Try/Except statement to capture data input issues
        try:
            # Test to see if the new name is Numeric or not
            if str(new_name).isnumeric() == False:
                # If the revised name isn't a number, change the name to the revised name
                self.__product_name = new_name
            else:
                # Raise an exception and send a message back to the user here
                raise Exception("Names cannot be numbers!! Please try again.")
        except Exception as err:
            # Print the following error handling statements
            print(err)

    @product_price.setter  # The NAME MUST MATCH the property's!
    def product_price(self, new_price):  # (setter or mutator)
        # Creating a variable for Float data conversion hee
        flt_price = 0
        # Needed 2 Try/Except statements here in order to handle data input issues
        try:
            try:
                # Test to see if the input price value can be converted to a FLOAT value
                flt_price = float(new_price)
            except ValueError as v:
                print("Value entered is not a number!! Try Again")
                # See if the Float value is zero here
            if flt_price != 0:
                # if not zero than set the new price here
                self.__product_price = new_price
            else:
                raise Exception("Prices cannot be zero, need a larger number!")
        except Exception as e:
            # Print the following error handling statements
            print(e)

    # -- Methods --
    def __str__(self):
        # Overrided String method here to send a customized value back to the user.
        return self.product_name + ' -  $' + str(self.product_price)

    @staticmethod  # You do not use the self keyword
    def get_object_count():  # This is a PUBLIC static method
        return Product.__counter

    @staticmethod  # You do not use the self keyword
    def __set_object_count():  # This is a PRIVATE and static method
        Product.__counter += 1


# Processing  --------- Open/Close files and Save Data -------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects"""

    # Static methods:
    @staticmethod
    def save_data_to_file(file_name, list_of_rows):
        """ Write the list of TO DO task to the text file

        :param file_name: (string) name of text file:
        :param list_of_rows: (string) name of text file:
        :return: (list) of dictionaries, 'success'
        """
        # Open a file and use a For Loop to write each table row or item to a text file
        File_Object_Write = open(file_name, "w")
        for item in list_of_rows:
            # write the name of the item and the value to the Home Inventory List text file
            File_Object_Write.write(str(item.get("Product Name")) + "," + str(item.get("Price")) + "\n")
        # Close the text file object here
        File_Object_Write.close()
        return 'Success'

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):  # v-> (a list of product objects)
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file
        :param list_of_rows: (list) list of products
        :return: nothing: 'Success'
        """
        # list_of_rows.clear()  # clear current data
        file = open(file_name, "r")  # Open the file Object here
        # Use a for loop to read data from the To Do List text file
        for line in file:
            productName, price = line.split(",")
            # Build Row dictionary here
            row = {"Product Name": productName.strip(), "Price": price.strip()}
            # Append the dictionary row to the List
            list_of_rows.append(row)
        file.close()  # Close the file Object
        # Return the list of rows
        return list_of_rows, 'Success'


# Processing  ------------------------------------------------------------- #
class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def print_current_products_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* Current Product Info: *******")
        print("      |  Product Name     |      Price         ")
        print("     --------------------------------------")
        # Use this for loop to print each row or dictionary into a table for the user
        for item in list_of_rows:
            # Use dictionary .get method to design the table and print for the end user
            print("   ", item.get("Product Name"), item.get("Price"), sep="   |     ")
        print("*******************************************")

    @staticmethod
    def input_new_product_if_already_exists(product_name, list_of_rows):
        """ Check to see if the Product name already exists in the list

        :param product_name: (string) name of the Product:
        :param list_of_rows: (list) list of products
        :return: Boolean value T/F
        """
        product_exists = False  # Set the initial task exists flag to False here
        # Use a for loop to see if the New Task Name is already in the table
        for item in list_of_rows:
            # change the name of the task to all lower case and see if current item is in the list
            if product_name.lower() == item.get("Product Name").lower():
                product_exists = True  # If the 2 Product names match then set this to True
        # If the task already exists in the list return True otherwise return false
        if product_exists is True:
            return True
        else:
            return False

    @staticmethod
    def add_data_to_list(name_of_product, price_of_product, list_of_rows):
        """ Add a task name and priority to the list

        :param name_of_product: (string) name of the Product
        :param price_of_product: (string) Price of the Product
        :param list_of_rows: (list) List of Product Information
        :return: 'success'
        """
        # Create the dictionary row object using the user input values and the next ID value
        dicRow = {"Product Name": name_of_product, "Price": "$" + str(price_of_product)}
        # Append the dictionary row to the List Table
        list_of_rows.append(dicRow)
        return 'Success'


# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def print_intro():
        """  Display a menu of choices to the user

        :return: nothing
        """
        # Introduction, print script name, demonstrate print() statement formatting here
        print("""\t\t\t <<<<<<  Product Name and Price Tracker  >>>>>>
        Hello, this is a simple Product Name and Price Tracker Script that uses the python
        object data to test and set values.  Please enter a menu option below.  
        """)

    @staticmethod
    def print_menu_tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        # Send the User a list of options here using a print statement and fancy formatting
        print('''Menu of Options:
        1) Add a Product Name and Price
        2) Print a Table of Product Names and Prices
        3) Save New Product Info!  
        4) Exit Program
        ''')

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        # User Choice Selection here
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def input_yes_no_choice(optional_message="Add another Product?(Y/N): "):
        """ Gets a yes or no choice from the user, pass in an optional message
        :param optional_message: Pass in a Yes/No Question message
        :return: string
        """
        # Use the Default Message or pass in an optional message, strip white spaces, and make lower case
        return str(input(optional_message)).strip().lower()

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)  # Print optional messages here otherwise print ''
        input('Press the [Enter] key to continue.')

    @staticmethod
    def input_new_product_and_price():
        """ Input a new Product Name and Price, check to see if Product name exists.  If true, try another Product Name!

        :return: nothing
        """
        # Get the User input about the new Product name
        str_product = input("What's the New Product Name?:  ")
        # Call this function to see if the Product Name already exists in the list, if false, add new Product
        if not Processor.input_new_product_if_already_exists(str_product, lstTable):
            while True:
                # Get the User input about the Price of the new product
                str_price = input(" What's the Price of this Product?: ")
                # Call this processing function to create a new Object for this Product
                strNewProductInfo = Product(str_product, str_price)  # <<<Use New Product Name and Price
                print("  New Product Name:>>>   ", strNewProductInfo)  # <<<Use the Over-rided String Function
                # Evaluate the user choice and exit loop if "n" in response
                # I did this in order to use the Setter parts of my new Product Class
                if "n" in IO.input_yes_no_choice("Is the New Product Name & Price correct?  "):
                    strNewName = input("  What is the Revised Product Name?  ")  # <<< Get Revised Product Name here
                    strNewProductInfo.product_name = strNewName  # <<< Use the Product Class here to rename object
                    strNewPrice = input("   What is the Revised Price?  ")  # <<< Get Revised Price here
                    strNewProductInfo.product_price = strNewPrice.strip('$')   # <Use the Product Class to revise object
                    print("    Revised Name & Price:>>>  " + str(strNewProductInfo)) #<< Print Revised Name/Price here
                    # Ask the User if the revised name and price are correct
                    if "y" in IO.input_yes_no_choice("Is the revised Product Name & Price correct now?  "):
                        print("Name and Price updated, exiting to main menu!")
                        Processor.add_data_to_list(strNewProductInfo.product_name, strNewProductInfo.product_price,
                                                   lstTable)  # << Revise the New Product List here
                        FileProcessor.save_data_to_file(strFileName, lstTable) # << call this function to save data
                        break
                    else:
                        print("")
                else:
                    Processor.add_data_to_list(strNewProductInfo.product_name, strNewProductInfo.product_price,
                                               lstTable)  # << Revise the New Product List here
                    FileProcessor.save_data_to_file(strFileName, lstTable) # << call this function to save data
                    break
                break
        else:
            # Let the user know that the given task name already exists using this print statement
            print("The given Product name already exists. Please try again!!")
            print()  # Add a line for looks


# Main Body of Script  ---------------------------------------------------- #
# Step 1 - When the program starts, Load data from ProductInfo.txt.
# Use this Processor function to read a text file and return a table of data
FileProcessor.read_data_from_file(strFileName, lstTable)  # read file data
IO.print_intro()
try:
    while True:
        # Step 2 - Display a menu of choices to the user
        print()  # Adding a line for looks
        IO.print_menu_tasks()  # Shows menu
        strChoice = IO.input_menu_choice()  # Get menu option

        # Step 4 - Process user's menu choice
        if strChoice.strip() == '1':  # Add a new product
            while True:  # Use a While loop to allow for continued data entry
                # Use this IO function to input a new task and priority
                IO.input_new_product_and_price()
                # Evaluate the user choice and exit loop if "n" in response
                if "n" in IO.input_yes_no_choice():
                    print()  # Add a line here for readability
                    # Exit the loop and go to the Main Menu
                    break

        elif strChoice == '2':  # Print the list of product names and prices
            Processor.print_current_products_in_list(lstTable)
            IO.input_press_to_continue()

        elif strChoice == '3':  # Save Data to File
            # Evaluate the user choice and exit loop if "y" in response
            if "y" in IO.input_yes_no_choice("Save this data to file? (y/n) - "):  # Use the user choice IO function
                # If the user enters "y" get the filename and task list table and user the Processor function
                # to write to a text file
                FileProcessor.save_data_to_file(strFileName, lstTable)
                strStatus = "Data Saved!!"  # Pass this message to the IO function below
                IO.input_press_to_continue(strStatus)
            else:
                # In this step we're passing in a message instead of a variable for this function
                IO.input_press_to_continue("Save Cancelled!")
                break
            continue  # to show the menu

        elif strChoice == '4':  # Exit Program
            print("Goodbye!")
            break  # and Exit

        else:
            # Use a print statement to send a reminder to the user
            print('Please choose only 1, 2, or 3!"')
            print()

# Error handling starts here
except Exception as e:
    # Print the following error handling statements
    print("There was a non-specific error!")
    print("Built-In Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')
    # Using the sys library here to get the line number of the line that failed
    exc_type, exc_obj, exc_tb = sys.exc_info()
    # print the line number here
    print("Line No: " + str(exc_tb.tb_lineno))