#Adding in The Catalog
lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.  "
stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.  "
luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown whith cream shade  "
#Prices
stylish_settee_price = 180.50
lovely_loveseat_pric = 254.00
luxurious_lamp_price = 52.15

#Tax
sales_tax = 0.088

#Costemer
costemer_one_total = 0
custemer_one_itemization = ""

costemer_one_total += lovely_loveseat_pric
custemer_one_itemization += lovely_loveseat_description

costemer_one_total +=luxurious_lamp_price
custemer_one_itemization +=luxurious_lamp_description

customer_one_tax = costemer_one_total * sales_tax
costemer_one_total += customer_one_tax

#The receipt
print('Costemer One Items:')
print(custemer_one_itemization)
print('Customer One Total:')
print(costemer_one_total)