"""
You are the Data Analyst at Carly’s Clippers, the newest hair salon on the block. Your job is to go through the lists of data that have been collected in the past couple of weeks. You will be calculating some important metrics that Carly can use to plan out the operation of the business for the rest of the month.

"""

#Variables
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]
total_price = 0
total_revenue = 0

#Loop 1 : Calculate the sum of all hairstules prices 
for price in prices :
  total_price += price
print(f"Total price is : {total_price} euro")
#Loop 2 : Calculate the avrage price 
average_price = total_price / len(prices) 
print(f"Average Haircut Price : {average_price} euro")
#Loop 3 : Use loop white list knowledge
new_prices = [new-5 for new in prices ]
print(f"New Prices :{new_prices} all in euro")
#Loop 4 : the price of the haircut at position * the number of people who got the haircut at position 
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
print(f"Total Revenue : {total_revenue} euro ")
average_daily_revenue = total_revenue / 7
print(f"Average daily revenue : {average_daily_revenue} euro")

#Loop 5 : Advertising all of the haircuts that are under 30 euro.
cust_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]
print(f"Hair styles that cust under 30 :\n{cust_under_30}")
