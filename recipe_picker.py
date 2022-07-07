from autocomplete import autocomplete, number_options, display_numbered_options
from recipe_data import recipes, ingredients


# declare variables

welcome = """"
What would you like to cook today? --- Not sure? 
What do you have available that you would like to cook something with? 
"""

# bring dataset into required data structure



# build search function



# helper functions

def get_string():
    string = input("""
Give me one or more characters of the ingredient you would like to look up and hit enter. 
I'll show you the options.
> 
""")
    return string

def get_ingredient():
    string = get_string()
    selection = autocomplete(string, ingredients)
    while not selection:
        string = input(f'''
    Sorry. There is no ingredient in the database that starts with "{string}".
    Please try again.
    ''')
        selection = autocomplete(string, ingredients)
    numbered_options = number_options(selection)
    print(numbered_options)
    display = display_numbered_options(numbered_options)
    print(f'These are the ingredients that start with "{string}".')
    print(display)
    ingredient = input(f''' 
Pick your ingredient by typing the number that belongs to it, 
or type "n" if you would like to start over.
''')    
    while ingredient != "n" and int(ingredient) not in numbered_options.keys():
        ingredient = input(f'''
    Sorry, "{ingredient}" is not a valid input. Please, try again.
    ''')

    if ingredient == "n":
        return get_ingredient()
    ingredient = numbered_options[int(ingredient)]
    print(f'''
    Great choice. Let's add "{ingredient}" to the search list.
''')
    return ingredient


def construct_search_list():
    picked_ingredients = list()
    ingredient_1 = get_ingredient()
    picked_ingredients.append(ingredient_1)
    ingredient_2 = input("Would you like to add another ingredient (y/n)\n> ")
    while ingredient_2 != "y" and ingredient_2 != "n":
        ingredient_2 = input('Come again? Please type "y" for yes or "n" for no.')
    if ingredient_2 == "y":
        ingredient_2 = get_ingredient()
        picked_ingredients.append(ingredient_2)
    else:
        return picked_ingredients
    ingredient_3 = input("Would you like to add a third and final ingredient (y/n)")
    while ingredient_3 != "y" and ingredient_3 != "n":
        ingredient_2 = input('Come again? Please type "y" for yes or "n" for no.')
    if ingredient_3 == "y":
        ingredient_3 = get_ingredient()
        picked_ingredients.append(ingredient_3)
    return picked_ingredients



# formulate question flow

print(welcome)

search_list = construct_search_list()
print(search_list)


# TESTING

