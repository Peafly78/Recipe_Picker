from autocomplete import autocomplete, number_options, display_numbered_options
from recipe_data import recipes, ingredients


# declare variables



# bring dataset into required data structure



# build search function



# helper functions

def get_string():
    string = input("""
What would you like to cook today? --- Not sure? 
What do you have available that you would like to cook something with? 
Give me one or more characters of the ingredient you would like to look up and hit enter. 
I'll show you the options.
> 
""")
    return string


# formulate question flow


string = get_string()
selection = autocomplete(string, ingredients)

while not selection:
    string = input(f'''
    Sorry. There is no ingredient in the database that starts with "{string}".
    Please try again.
    ''')
    selection = autocomplete(string, ingredients)

numbered_options = number_options(selection)
display = display_numbered_options(numbered_options)

print(f'These are the ingredients that start with "{string}".')
print(display)

picked_ingredients = list()

ingredient_1 = input(f''' 
Pick your ingredient by typing the number that belongs to it, 
or type "n" if you would like to start over.
''')

if ingredient_1 == "n":
    # invoke function that gets string / to start over
    pass

elif ingredient_1 not in numbered_options.keys(): # how can I make this a while loop
    ingredient_1 = input(f'''
    Sorry, {ingredient_1} is not a valid input. Please, try again.
    ''')

else:
    ingredient_1 = numbered_options[int(ingredient_1)]
    picked_ingredients.append(ingredient_1)

ingredient_2 = input(f'''
Great choice. Do you want to look at recipes with "{ingredient_1}" (press enter), 
or do you want to add another ingredient? (type "y")
''')

if ingredient_2 == "y":
    # invoke function that gets string / to start over, adding another ingredient to the picked list
    # create helper functions for that
    pass

print(picked_ingredients)


# TESTING