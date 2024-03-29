
# shopping_cart.py

#from pprint import pprint
import os
import pprint

from dotenv import load_dotenv
import sendgrid
from sendgrid.helpers.mail import * # source of Email, Content, Mail, etc.

load_dotenv()

import datetime

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
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

#print (products)
# pprint(products)

# TODO: write some Python code here to produce the desired output

#
#Clerk inputs
#


#consider using a loop - This allows us to get the question and input as much as possible

total_price = 0
selected_ids = []
Valid_ids = []
for i in products:
    Valid_ids.append(i["id"])

while True:
    Selected_ID = input("Please enter a product ID or Done if there are no more products:")
    if Selected_ID.lower() == "done": #Think I have to use elif
        break
    while Selected_ID not in str(Valid_ids): # either make an elif or add another break
        print ("Invalid ID. Please enter a valid ID.")
        break
    else:
        #matching_products  = [p for p in products if str(p["id"]) == str(Selected_ID)] 
        #matching_product = matching_products[0]
        #total_price = total_price + matching_product ["price"]
        #print("Selected Product: " + matching_product["name"] + " " + str(matching_product ["price"]))
        selected_ids.append(Selected_ID)
        ### NEED TO ADD SOMETHING THAT INVALIDATES ANYTHING BESIDES 1-20 AND DONE - Look at rock paper scissors exercise
#print(matching_product)
#print(type(matching_product))

###NEED TO CREATE LOGIC TO VALIDATE CHOICE### - Should be able to use if loop

#options = matching_products
#if  matching_product not in options:   
#    print ("Invalid Selection. Please enter correct ID")




#this illustrtes we are looking for one product. Not the entire list

# list comprehension will return a list
# # this is because we want the ID selected to match an ID in our product list
#print (matching_products)

# we are comparing different data types - Integer of entering products ID and a string version of 9. These do not match
#print (type(matching_product))

#print(Selected_ID)
#print(type(Selected_ID)) - This value is a string version of the number ID input


#
#Program outputs - Receipt
#
print ("--------------------------------------")
print ("Around the Corner Market")
print ("www.ATCmkt.com")
print ("--------------------------------------")
now = datetime.datetime.now()
print("Checkout Time: " + now.strftime('%b %d %Y %I:%M %p'))
print ("--------------------------------------")
print("Selected Products:")

#need to keep running total within loop  - define variable above loop and within loop after we find matching product we can accumulate value of total price and keep adding product price to total
#print (selected_ids)
for Selected_ID in selected_ids:
    matching_products  = [p for p in products if str(p["id"]) == str(Selected_ID)] 
    matching_product = matching_products[0]
    total_price = total_price + matching_product ["price"]
    print("... " + matching_product["name"] + " " + str('${:,.2f}'.format(matching_product["price"])))
    

tax = (total_price*.0875)
print ("--------------------------------------")
print ("Subtotal: " + str('${:,.2f}'.format(total_price)))
print ("NYC Sales Tax: " + str('${:,.2f}'.format((tax))))
print ("Total: " + str('${:,.2f}'.format(total_price + tax)))# add string format for price
print ("--------------------------------------")
print ("Thank you! Please come again soon!")

# can def function - right at top



#price_usd = " (${0:.2f})".format(p["price"])

#A grocery store name of your choice - Print name
#A grocery store phone number and/or website URL and/or address of choice - Print Url
#The date and time of the beginning of the checkout process, formatted in a human-friendly way (e.g. 2019-06-06 11:31 AM) - ??? How do we know specific date. Look up date time code discuss in class
#The name and price of each shopping cart item, price being formatted as US dollars and cents (e.g. $1.50) - Need to change definition of p
#The total cost of all shopping cart items, formatted as US dollars and cents (e.g. $4.50), calculated as the sum of their prices
#The amount of tax owed (e.g. $0.39), calculated by multiplying the total cost by a New York City sales tax rate of 8.75% (for the purposes of this project, groceries are not exempt from sales tax)
#The total amount owed, formatted as US dollars and cents (e.g. $4.89), calculated by adding together the amount of tax owed plus the total cost of all shopping cart items
#A friendly message thanking the customer and/or encouraging the customer to shop again - Print a friendly message 
#The program should be able to process multiple shopping cart items of the same kind, but need not display any groupings or aggregations of those items (although it may optionally do so).


# adapted from https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/notes/python/packages/sendgrid.md

SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY", "OOPS, please set env var called 'SENDGRID_API_KEY'")
MY_EMAIL_ADDRESS = os.environ.get("MY_EMAIL_ADDRESS", "OOPS, please set env var called 'MY_EMAIL_ADDRESS'")

# AUTHENTICATE

sg = sendgrid.SendGridAPIClient(apikey=SENDGRID_API_KEY)
#Load_env is telling code to pull from env folder. we don't want sensitive info in our code

# COMPILE REQUEST PARAMETERS (PREPARE THE EMAIL)

from_email = Email(MY_EMAIL_ADDRESS)
to_email = Email(MY_EMAIL_ADDRESS)
subject = "Your Receipt from AMC Market"
message_text = ("Hello, This is a message from your AMC Market.See below for your receipt. Thank you for shopping at our Market and come again!" + " " + 
"........." + matching_product["name"] + str('${:,.2f}'.format(matching_product["price"])) + ", " +
"Subtotal: " + str('${:,.2f}'.format(total_price)) + ", " + "NYC Sales Tax: " + str('${:,.2f}'.format((tax)) + ", " + "Total: " + str('${:,.2f}'.format(total_price + tax))))
content = Content("text/plain", message_text)
mail = Mail(from_email, subject, to_email, content)

# ISSUE REQUEST (SEND EMAIL)

response = sg.client.mail.send.post(request_body=mail.get())

# PARSE RESPONSE

pp = pprint.PrettyPrinter(indent=4)

print("----------------------")
print("EMAIL")
print("----------------------")
print("RESPONSE: ", type(response))
print("STATUS:", response.status_code) #> 202 means success
print("HEADERS:")
pp.pprint(dict(response.headers))
print("BODY:")
print(response.body) #> this might be empty. it's ok.)
