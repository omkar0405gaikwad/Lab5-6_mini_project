#Local taxes are accounted for in this dictionary of the format:
# "StateName" : [GroceryTax + LocalTax, ElectronicsTax + LocalTax, ClothingTax + LocalTax]
states = {
    "Mississippi" : [7, 7, 7],
    "Kansas" : [6.5 + 1, 6.5 + 1, 6.5 + 1],
    "Alabama" : [4 + 1, 4 + 1, 4 + 1],
    "Oklahoma" : [4.5 + 1, 4.5 + 1, 4.5 + 1],
    "Georgia" : [0 + 1, 4 + 1, 4 + 1],
    "Massachusetts" : [0, 6.25, 6.25],
    "New York" : [0 + 1, 4 + 1, 4],
    "Ohio" : [0, 5.75 + 1, 5.75 + 1]
}

n_items = int(input("How many items did you purchase? "))
total_cost = 0
cumulative_massachusetts_clothing_cost = 0
cumulative_new_york_clothing_cost = 0