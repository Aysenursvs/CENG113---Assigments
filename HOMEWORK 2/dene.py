def prepareInfo (data, stage):
    #if stage == "categories.txt":
    #   category_file = open("categories.txt", "r")
    #    category_list1 =[]
    #    category_list2 = []
    #    for i in category_file:
    #        name_category = i.rstrip("\n")
    #        name_category = name_category.split(";")
    #        category_list1.append(name_category[0])
    #        category_list2.append(name_category[1])
    #    return category_list1, category_list2
    #else:
        new_file = open(stage, "r")
        list1 = []
        list2 = []
        for i in new_file:
            name =i.rstrip("\n")        #I assigned a variable name and name1 to use rstrip and split.
            name1 = name.rstrip("#")
            name1 = name1.split(";")
            print(name1)   #For testing
            if name1[0] == data:
                if stage == "categories.txt":
                    name1[2] = "a"
                     
                list1.append(name1[1])  # To hold the datas separatly in different lists list1 and list2.
                list2.append(name1[2])
        print(list1)  # For testing
        print(list2)
        return list1, list2

def printMenu(list):    
    nth = 1     # Asigning for number of datas.
    for i in list:      # In this for loop, it printed number of datas. Ex: 1. ..., 2. ... etc.
        print(str(nth) + ".", i)
        nth += 1
    
   


def getUserInput(file):     # To get a input from user and check the input.
    try:
        selection = int(input("Please select the {}: ".format(file))) 
        if selection > 6:                                   
            print("Wrong selection. Please select again!")
            selection = int(input("Please select the {}:".format(file) ))
    except ValueError:
        print("Wrong selection. Please select again!")
        selection = int(input("Please select the {}:".format(file)))
    return selection


print("--------------------------------------------------")
print("Welcome to the store!")
print("--------------------------------------------------")

answer = "y"                                                                                                #Assigning a variable for "Do you want to add another product?" question.
order = 1                                                                                                   #Number of order.
total = 0                                                                                                   #Total price in the first part.
selected_category_list = []                                                                                 #Empty lists out of while loop for final order recipe.
selected_product_list = []
selected_portion_list = []
selected_portion_price_list = []

while answer == "y":                                                                                        #If the user want to add product, then this while loop will print the funtions again.  
        category_names, category_empty_list = prepareInfo(0, "categories.txt")                                     #Call the function for satge of category.
        printMenu(category_names)                                                                           #Print the all categories by calling the function.

        selected_category_index = getUserInput("categories")                                                #Get an input from user to select a category.
        #print(selected_category_index)
        print("--------------------------------------------------")
        print(category_names[selected_category_index - 1])                                                  #Print the name of category.
        print("--------------------------------------------------")
        #selected_category_id = category_ids[selected_category_index - 1]                                   #For testing. No matter.

        product_names, product_codes = prepareInfo("#" + str(selected_category_index), "products.txt")      #Call the function for stage of product.
        printMenu(product_names)                                                                            #Print the all products according to slection of category by calling the function.

        selected_product_index = getUserInput("products")                                                   #Get an input from user to select a product.
        print("--------------------------------------------------")
        print(product_names[selected_product_index - 1])                                                    #Print the name of product by using index.
        print("--------------------------------------------------")
        #selected_product_id = product_codes[selected_product_index - 1]                                    #For testing. No matter.

        portion_size, portion_prices = prepareInfo("#" + str(product_codes[selected_product_index - 1]), "portions.txt")    #Call the function for stage of portions.
        printMenu(portion_size)                                                                             #Print the all portions according to selection of product.

        selected_portion_index = getUserInput("portions")                                                   #Get an input to select a portion.
        print("--------------------------------------------------")
        print(portion_size[selected_portion_index - 1])                                                     #Print the selection of portion by using index.
        print("--------------------------------------------------")
        
        
        total += float(portion_prices[selected_portion_index - 1])                                          #Hold the price of product in the total variable.

        selected_category_list.append(category_names[selected_category_index - 1])                          #Append the selection of user into lists that was defined out of while loop.
        selected_product_list.append(product_names[selected_product_index - 1])
        selected_portion_list.append(portion_size[selected_portion_index - 1])
        selected_portion_price_list.append(portion_prices[selected_portion_index - 1])

        print(f"\nSelected category: {category_names[selected_category_index - 1]}")                        #Result of order.
        print(f"Selected product: {product_names[selected_product_index - 1]}")
        print(f"Selected portion: {portion_size[selected_portion_index - 1]} - ${portion_prices[selected_portion_index - 1]}")
        #print(selected_category_list)                                                                      #For testing.
        #print(selected_product_list)
        #print(selected_portion_price_list)


        answer = input("Do you want to add another product? (y/n): ")                                        # Get an input for the question.
        if answer == "y":                                                                                    # Increase the number of order according to answer of user.
            order += 1

print("Order Recipe")                                                                                       #Print the order table.
print("==============================================================")
for i in range(order):
    #print(i)
    print(selected_category_list[i], "--", selected_product_list[i], "--", selected_portion_list[i], "--", selected_portion_price_list[i])
print("==============================================================")
print("Total:", str(f"{total:.2f}"), "$")