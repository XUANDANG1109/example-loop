list1 = []
match_points = [9, 4, 3, 8, 10, 6]
print(match_points[0])
print(match_points[3])
print(match_points[5])
print("The total number of points of these matches is:", match_points[0] + match_points[3] + match_points[5])

# Changing the value
shopping_list = ["orange", "ice-cream", "banana", "chicken", "vegetable"]
print(shopping_list)
shopping_list[4] = "Coca-cola"
print(shopping_list)

# Adding items
shopping_list.append("Cookies")
print(shopping_list)

# Adding an item to a specific location
shopping_list.insert(2,"2 tomatoes")
print(shopping_list)

# Removing an item
shopping_list.remove("2 tomatoes")
print(shopping_list)

shopping_list.pop(2)
print(shopping_list)
