#farm harvest calculator

field1 = 120
field2 = 85
field3 = 150
field4 = 95 
field5 = 110

total = field1 + field2 + field3 + field4 + field5
avg = total/5
print("total harvest: ", total, " kg")
print("average per field: ", avg, " kg")

price_PER_kg = 15
earnings = price_PER_kg*total
print("total earnings: ", earnings, " rupees")

bag_capacity = 25
packed_bags = total//bag_capacity
leftovers = total%bag_capacity
print("full bags packed: ", packed_bags)
print("leftover grain: ", leftovers, " kg")

last_harvest = 500
print("Better than last year? : ", total>last_harvest)
print("same as last year? : ", total==last_harvest)
print("atleast as good as last year? : ", total>=last_harvest)

bonus_field = 30
total += bonus_field
print("after bonus crop total kgs I have: ", total, " kg")
saved_crop = 15
total-=saved_crop
print("total kgs after seed reserve: ", total, " kg")
print("final bags packed:", total//bag_capacity)
print("final leftover grain: ", total%bag_capacity)
