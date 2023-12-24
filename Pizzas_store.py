print("""
Len's Slice
You work at Len’s Slice, a new pizza joint in the neighborhood. You are going to use your knowledge of Python lists to organize some of your sales data.
""")

#LIST OF TOPPINGS
toppings = ["pepperoni","pineapple","cheese","sausage","olives","anchovies","mushrooms"]
#PRICES
prices = [2,6,1,3,2,7,2]
#Your boss wants you to do some research on 2 euro slices
num_two_dollar_slices = prices.count(2)
#number of pizzas using len()
num_pizzas = len(toppings)
print(f'\t We sell {num_pizzas} different kinds of pizza !')
#list of prices
print('-'*8,'Menu','-'*8)
pizza_and_prices =[[2,"pepperoni"],[6,"pineapple"],[1,"cheese"],[3,"sausage"],[2,	"olives"],[7,"anchovies"],[2,"mushrooms"]]
print(pizza_and_prices)
#list of prices sorted 
pizza_and_prices.sort()
print('-'*8,'Our pizzas offers','-'*8)
#the cheapest pizza
cheapest_pizza = pizza_and_prices[0]
print(f'the cheapest pizza is {cheapest_pizza}!')
#the most expensive pizza
priciest_pizza =pizza_and_prices[-1]
print(f'the priciest pizza is {priciest_pizza}!')

"""It looks like the most expensive pizza from the previous step was our very last "anchovies" slice. Remove it from our pizza_and_prices list since the man bought the last slice.
"""
last_slice = pizza_and_prices.pop(-1)
print(f'the last slice of pizza {last_slice} was bought !!')
print('-'*8,'Menu','-'*8)
print(pizza_and_prices)
print('-'*8,'New Topping : Peppers','-'*8)
pizza_and_prices.insert(4,[2.5 ,"peppers"])
print(pizza_and_prices)
#the the cheapest pizzas
print('-'*8,'The three cheapest :')
three_cheapest = pizza_and_prices[0:3]
print(three_cheapest)
