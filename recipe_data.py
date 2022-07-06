recipes = [
    ['Mushroom Risotto', 'vegetarian', ['rice', 'mushrooms', 'cheese']], 
    ['Salad Wraps', 'vegetarian', ['salad', 'tortillas', 'tomatoes']], 
    ['Boiled Potatoes', 'vegetarian', ['potatoes', 'butter', 'cheese']], 
    ['Vegetable Quinoa Pot', 'vegetarian', ['quinoa', 'tomatoes', 'eggplant']], 
    ['Lasagna', 'meat', ['minced meat', 'pasta', 'tomatoes']], 
    ['Spaghetti Vongole', 'fish', ['pasta', 'clams', 'cheese']], 
    ['Potatoe Spinach Casserole', 'vegetarian', ['potatoes', 'spinach', 'cream']], 
    ['Grilled Salmon', 'fish', ['salmon', 'rice', 'spinach']], 
    ['Pea Soup', 'vegetarian', ['peas', 'mint', 'vegetable broth']], 
    ['Lamb Stew', 'meat', ['lamb', 'carrots', 'onions']]
]

ingredients = set([ingredient for recipe in recipes for ingredient in recipe[2]])

# TESTING

#print(recipes)
#print(ingredients)