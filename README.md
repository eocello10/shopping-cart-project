# shopping-cart-project
(Project Description)
Create a receipt based on products, price, and produce the total price of the shopping cart

#Installation/Repo Setup
Required to clone or download repository created from https://github.com/eocello10/shopping-cart-project, then navigate into project repository by entering code into command line:
'''sh
cd shopping-cart-project #need to copy folder on local drive
'''
Insert product list based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017 as seen below 
products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] 

#Installation/Usage
reate and activate a new Anaconda virtual environment:

conda create -n shopping-env python=3.7 # (first time only)
conda activate shopping-env
From within the virtual environment, install the pytest package:

# NOTE: we won't need pytest until/unless addressing the optional "Automated Testing" challenge,
# so you can feel free to skip this now and return later...

pip install pytest

After complete you can begin to run the code in your command line by copying and pasting the location of your shopping cart repo on your local drive and open in VS Text code then run the program:

python shopping_cart-project.py


##Requirements
total_price = 0 - Starting point 
Selected_ids = []
Valid_ids = []
for i in products:
    Valid_ids.append(i["id"])
    - Use the for loop in order to make this valid_ids item more dynamic in the below code. Allows me to determine whether something is invalid or not
while True:
    Selected_ID = input("Please enter a product ID or Donec if there are no more products:")
    if Selected_ID.lower() == "done": 
        - This allows me to esnure that if any capital letters are written in done (i.e. DONE or Done) the code will recognize this is done and break to produce the receipt
        break
    while Selected_ID not in str(Valid_ids): # either make an elif or add another break
        print ("Invalid ID. Please enter a valid ID.")
        break
    else:
        selected_ids.append(Selected_ID) - Create an append..
 - This code asks for user to input a value. The goal is to have user input a valid value and produce a result. This code will not allow invalid results(produce a message when this happens). When the user inputs, done, the code will produce a break and produce the receipt
 - Thus, we can move our loop to the display section of our code and create a for Selected_ID in selected_ids: the nthe loop 
    -Create a loop to allow for multiple product IDs to be entered. Must create a break which allows for the loop to end. In our case, use an if statement tas seen in above code

matching_product  = [p for p in products if p["id"] == Selected_ID] - This is a list comprehension that is required to be generated in order to pull from our products

- we are comparing different data types - Integer of entering products ID and a string version of 9. Have to make them match in order to produce a proper result

print (matching_product)

print("Selected Product: " + matching_product["name"] + " " + str(matching_product ["price"]))
- At a certain point you will need to remove this as we do not want to print out the select product each time. Rather we need to see this as part of the receipt
-To format price use the code: '${:,.2f}'.format and this will format any of your prices to two decimals

- This concantenantion allows us to combine Text with name of product and with the price of product. Hint: Be careful as have to ensure all of these are same data type (i.e. string)

- You need to keep running total within loop  - To do this define variable (i.e. total_price) above loop and within loop. After we find matching product we can accumulate value of total price and keep adding product price to total until user selects done
#Code:
for Selected_ID in selected_ids:
    matching_products  = [p for p in products if str(p["id"]) == str(Selected_ID)] 
    matching_product = matching_products[0]
    total_price = total_price + matching_product ["price"]
    print("... " + matching_product["name"] + " " + str('${:,.2f}'.format(matching_product["price"])))

-Prices - Subtotal, Tax, and Total - Need to format using '${:,.2f}'.format'
    - Subtotal = sum of the total prices of the products
    - Tax = (total_price*.0875)
    - Total = Subtotal + Tax 

- Do these steps last:
Print Grocery name, Web address, and the date/time receipt was created (use link to module below)
https://github.com/prof-rossetti/nyu-info-2335-201905/blob/master/notes/python/modules/datetime.md
- To format and make it AM,PM or more the month instead of numbers after you import datetime use the below:
    - now = datetime.datetime.now()
    - print("Checkout Time: " + now.strftime('%b %d %Y %H:%M %p')) - The b,d,Y gives you the month spelled out, the date, and year - The H,M, p gives you the hour and minute along with the AM or PM. 

IMPORTANT: Continue to test your code to ensure proper results are being produced. You can either automate this or run it manually.