selection = int(input("Please select a category: "))
portions_file = open("portions.txt", "r")

read = portions_file.read()


if True:
    for i in read:
        name_po = i.rstrip("\n")
        name_po = name_po.rstrip("#")
        name_po = name_po.split(";")
        if selection == name_po[0]:
            print(name_po[0] + ".", name_po[1])
##################
def prepare_info(data, stage, selection):
    if stage == "categories":
        selected_category = data[int(selection) - 1][1]
        products_in_category = [product for product in data if product[0] == selection]
        return selected_category, products_in_category
    elif stage == "products":
        selected_product = next(product for product in data if product[2] == selection)
        portions_for_product = [portion for portion in data if portion[0] == selection]
        return selected_product, portions_for_product

def print_menu(stage, data):
    print("\nMenu:")
    if stage == "categories":
        print("Select a category:")
        for index, category in enumerate(data, start=1):
            print(f"{index}. {category[1]}")
    elif stage == "products":
        print(f"\nProducts in {data[0]}:")
        for product in data[1]:
            print(f"{product[1]} - {product[2]}")
    elif stage == "portions":
        print(f"\nAvailable portions for {data[0][1]}:")
        for portion in data[1]:
            print(f"{portion[1]} - ${portion[2]}")

def get_user_input(prompt):
    return input(prompt)

def run():
    # Load Data
    categories = load_data("categories.txt")
    products = load_data("products.txt")
    portions = load_data("portions.txt")
    order = []

    # Stage 1: Select Category
    category_stage = "categories"
    category_selection = get_user_input("Enter the number for the desired category: ")
    selected_category, products_in_category = prepare_info(categories, category_stage, category_selection)
    print_menu(category_stage, categories)

    # Stage 2: Select Product
    product_stage = "products"
    product_selection = get_user_input("Enter the code for the desired product: ")
    selected_product, portions_for_product = prepare_info(products, product_stage, product_selection)
    print_menu(product_stage, (selected_category, products_in_category))

    # Stage 3: Select Portion
    portion_stage = "portions"
    print_menu(portion_stage, (selected_product, portions_for_product))
    portion_selection = get_user_input("Enter the number for the desired portion: ")

    # Add Product to Order
    selected_portion = next(portion for portion in portions_for_product if portion[1] == portion_selection)
    order.append((selected_product, selected_portion))

    # Display Order Details
    print("\nOrder Details:")
    for product, portion in order:
        print(f"{product[1]} ({portion[1]}): ${portion[2]}")

    # Calculate and Display Total Cost
    total_cost = sum(float(portion[2]) for _, portion in order)
    print(f"\nTotal Cost: ${total_cost}")

def load_data(file_name):
    data = []
    with open(file_name, 'r') as file:
        for line in file:
            if not line.startswith("#"):
                columns = line.strip().split(";")
                data.append(columns)
    return data

# Run the program
run()

