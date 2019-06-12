# shopping-cart-project
(Project Description)
Create a receipt based on products, price, and produce the total price of the shopping cart

#Installation
Required to clone or download repository created from https://github.com/eocello10/shopping-cart-project, then navigate into project repository by entering code into command line:
'''sh
cd shopping-cart-project #need to copy folder on local drive
'''

#Usage
Copy and paste products into VS Text code then run the program:
'''py
python shopping_cart-project.py
'''

##Requirements

Selected_ID = input("Please enter a product ID:") - This code asks for user to input a value. The goal is to have user input a value and produce a result.

matching_product  = [p for p in products if p["id"] == Selected_ID] - This is a list comprehension that is required to be generated in order to pull from our products

- we are comparing different data types - Integer of entering products ID and a string version of 9. Have to make them match in order to produce a proper result

print (matching_product)

print("Selected Product: " + matching_product["name"] + " " + str(matching_product ["price"]))

- This concantenantion allows us to combine Text with name of product and with the price of product. Hint: Be careful as have to ensure all of these are same data type (i.e. string)