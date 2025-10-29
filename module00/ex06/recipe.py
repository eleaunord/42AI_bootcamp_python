
#!/usr/bin/env python3

cookbook = {
    "Sandwich": {
        "ingredients": ["ham", "bread", "tomatoes", "cheese"],
        "meal": "lunch",
        "prep_time": 10,
    },
    "Cake": {
        "ingredients": ["flour", "sugar", "eggs"],
        "meal": "dessert",
        "prep_time": 60,
    },
    "Salad": {
        "ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
        "meal": "lunch",
        "prep_time": 15,
    },
}


# -------------------------

def print_name_recipes():

	for x in cookbook.items():
		print(x)
	
# -------------------------

def print_details(recipe_name:str):

	for x, obj in cookbook.items():
		if x == recipe_name:
			for y in obj:
				print(f"{y} : {obj[y]}")

# -------------------------

def del_recipe(recipe_name):
	if recipe_name in cookbook:
		del cookbook[recipe_name]
	        print(f"Recipe '{recipe_name}' deleted successfully!")
    else:
        print(f"Recipe '{recipe_name}' not found in the cookbook.")

# -------------------------

def add_recipe():
	name = input("Enter a name :\n").strip()
	if not name:
		print("Name cannot be empty.")
		return
	if name in cookbook:
		print("Recipe already exists")
	
	print("Enter ingredients")
	print()print("(Type one ingredient per line; press Enter on an empty line to finish.)")
	ingredients = []
	while True:
		line = input().strip()
		if not line:
			break
		ingredients.append(line)
	meal = input("Enter a meal type:\n").strip()
	if not meal:
			print("Meal cannot be empty")
			return

	try : 
		prep_time = int(input("Enter a prep time :\n").strip())
	except ValueError:
		print("Preparation time must be an int")
		return
	
	cookbook[name] = {
		"ingredients" : ingredients,
		"meal" : meal,
		"prep_time" : prep_time,
	}
	print(f"Recipe {name} added!")

# -------------------------

def display_menu():
    print("Welcome to the Python Cookbook!")
    print("List of available options:")
    print("1: Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a recipe")
    print("4: Print the cookbook")
    print("5: Quit\n")

# -------------------------

def main():
    while True:
        display_menu()
        choice = input("Please select an option:\n> ").strip()

        if choice == "1":
            add_recipe_from_input()
        elif choice == "2":
            name = input("Please enter a recipe name to delete:\n> ").strip()
            del_recipe(name)
        elif choice == "3":
            name = input("Please enter a recipe name to get its details:\n> ").strip()
            print_details(name)
        elif choice == "4":
            print("All recipes:")
            print_name_recipes()
            print()
        elif choice == "5":
            print("Cookbook closed.")
            break
        else:
            print("Sorry, this option does not exist. Please try again.\n")

    return 0

if __name__== "__main__":
	raise SystemExit(main())