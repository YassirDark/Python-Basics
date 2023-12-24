weight = 1.5

# Ground Shipping

if  weight <= 2:
    ground_shipping_cost = 1.5 * weight + 20
elif weight <= 6:
    ground_shipping_cost = 3.0 * weight + 20
elif weight <= 10:
    ground_shipping_cost = 4.0 * weight + 20
else:
    ground_shipping_cost = 4.75 * weight + 20

print(f'Ground Shipping coast is : {ground_shipping_cost} $')

# Shipping Premium

# Calculate Ground Shipping Premium cost
ground_shipping_premium_cost = 125.0

# Calculate Drone Shipping cost
if weight <= 2:
    drone_shipping_cost = 4.5 * weight
elif weight <= 6:
    drone_shipping_cost = 9.0 * weight
elif weight <= 10:
    drone_shipping_cost = 12.0 * weight
else:
    drone_shipping_cost = 14.25 * weight

print('Drone Shipping cost is : %.3f $ '% drone_shipping_cost)

if drone_shipping_cost >  ground_shipping_cost :
  print('The cheapest method of shipping is : Ground shipping so it will cost you : %.3f $'% ground_shipping_cost)
else:
   print('The cheapest method of shipping is : Drone shipping so it will cost you : %.3f $'%   drone_shipping_cost)

list = []
list.append([4])
print(list)