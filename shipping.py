weight = 41.5

#Ground Shipping
if weight <= 2:
  cost = weight * 1.5 + 20
elif weight > 2 and weight <= 6:
  cost = weight * 3.00 + 20
elif weight > 6 and weight <= 10:
  cost = weight * 4.00 + 20
elif weight > 10:
  cost = weight * 4.75 + 20
else:
  print("Error")
print("Ground shipping: $", cost)


#Premium Ground Shipping
cost_premium = 125
print("Ground shipping premium: $",cost_premium)

#Drone Shipping
if weight <= 2:
  cost_drone = weight * 4.50
elif weight > 2 and weight <= 6:
  cost_drone = weight * 9.00
elif weight > 6 and weight <= 10:
  cost_drone = weight * 12.00
elif weight > 10:
  cost_drone = weight * 14.25
else:
  print("Error")

print("Drone Shipping: $", cost_drone)



