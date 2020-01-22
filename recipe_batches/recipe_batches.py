#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):

  ingredient_amounts = []
  #if ingredient amounts are LESS than those in the recipe amounts, return 0
  if len(recipe) > len(ingredients):
    return 0
  #if ingredient amounts are EQUAL TO or MORE, do division 
  else:
    for x in recipe:
      if recipe.get(x) <= ingredients.get(x):
        ingredient_amounts.append(ingredients.get(x)//recipe.get(x))
      else:
        return 0
  return min(ingredient_amounts)

      #if x < y in ingredients, divide and stash in array of its own
      # if x > y in ingredients, return 0




recipe_batches({ 'milk': 2 }, { 'milk': 200})



if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))