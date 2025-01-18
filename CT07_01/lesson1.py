#Define bins
#glass_bin = []
#plastic_bin = []
#paper_bin = []

# Define the items to be sorted
#items = ["glass bottle", "plastic cup", "paper sheet", "glass jar", "plastic bag", "paper box"]

# Function to sort items into bins
#function sort_items(items):
    #for each item in items:
        #if item contains "glass":
            #add item to glass_bin
        #else if item contains "plastic":
           # add item to plastic_bin
       # else if item contains "paper":
           # add item to paper_bin

# Call the function to sort items
#sort_items(items)

# Output the sorted bins
#print("Glass Bin:", glass_bin)
#print("Plastic Bin:", plastic_bin)
#print("Paper Bin:", paper_bin)

glass_bin = []
plastic_bin = []
paper_bin = []


items = ["glass bottle", "plastic cup", "paper sheet", "glass jar", "plastic bag", "paper box"]


def sort_items(items):
    for item in items:
        if "glass" in item:
            glass_bin.append(item)
        elif "plastic" in item:
            plastic_bin.append(item)
        elif "paper" in item:
            paper_bin.append(item)


sort_items(items)


print("Glass Bin:", glass_bin)
print("Plastic Bin:", plastic_bin)
print("Paper Bin:", paper_bin)
