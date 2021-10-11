"""
Pete likes to bake some cakes. He has some recipes and ingredients. Unfortunately he is not good in maths. 
Can you help him to find out, how many cakes he could bake considering his recipes?

Write a function cakes(), which takes the recipe (object) and the available ingredients (also an object) 
and returns the maximum number of cakes Pete can bake (integer). For simplicity there are no units for the amounts 
(e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200). 
Ingredients that are not present in the objects, can be considered as 0.
Examples:

# must return 2
cakes({flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200})
# must return 0
cakes({apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100}, {sugar: 500, flour: 2000, milk: 2000})
"""

def cakes(recipe, available):
    cross = [available[x] // recipe[x] for x in recipe if x in available]
    return 0 if len(cross) != len(recipe) else min(cross) 

print(cakes({'crumbles': 41, 'pears': 51, 'nuts': 5}, {'cream': 2426, 'flour': 6799, 'nuts': 2600, 'apples': 5299, 'crumbles': 8750, 'chocolate': 9844, 'butter': 4892, 'milk': 4347, 'pears': 747, 'oil': 519}))


