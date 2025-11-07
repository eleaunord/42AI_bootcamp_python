
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

def printing_names():
	for name in cookbook.items() : 
		print(name)
	

def details(recipe_name:str):
	if recipe_name not in cookbook:
		print(f"Recipe '{recipe_name}' not found")
		return
	recipe = cookbook[recipe_name]
	for field, value in recipe.items():
		print(f"{field}:{value}")
			
def delete(recipe_name:str):
	if recipe_name not in cookbook:
		print(f"Recipe '{recipe_name}' not found")
		return
	del(cookbook[recipe_name])
	print(f"Recipe {recipe_name} successfully deleted")

def add():
	new_recipe = input("Please enter recipe name\n").strip()
	if new_recipe in cookbook:
		print("error already exists")
	if not new_recipe : 
		print("can't be empty")
		return 
	print("enter ingredients one per line\n")
	ingredients = []
	while 1 : 
		line = input().strip()
		if not line: 
			break
		ingredients.append(line)
	meal = input("enter meal type\n").strip()
	if not meal :
		print("can't be empty")
		return
	try : 
		prep_time = int (input("enter a prep time :\n").strip())
	except ValueError:
		print("prep time must be an int")
		return
	cookbook[new_recipe] = {
		"ingredients" : ingredients,
		"meal": meal,
		"prep_time" : prep_time,
	}
	print(f"Recipe {new_recipe} added!")

def display_menu():
	print("Welcome list of options :\n")
	print(" 1 : add recipe\n")
	print(" 2 : delete recipe\n")
	print(" 3 : print a recipe\n")
	print(" 4 : print the cookbook\n")
	print(" 5 : quit\n")


def main():
    while True:
        display_menu()
        choice = input("Please enter option\n").strip()
        
        if choice == "1":
            add()
            input("\npress enter to return to menu")
        elif choice == "2":
            name = input("Enter a recipe name to be deleted\n").strip()
            delete(name)
            input("\npress enter to return to menu")
        elif choice == "3":
            name = input("Enter a recipe name to be detailed\n").strip()
            details(name)
            input("\npress enter to return to menu")
        elif choice == "4":
            printing_names()
            input("\npress enter to return to menu")
        elif choice == "5":
            print("Cookbook closed bye")
            return 0
        else:
            print("invalid option please try again")
            input("\npress enter to return to menu")
		
if __name__ == "__main__":
	raise SystemExit(main())