from .models import Recipe, Ingredient
import random


def generate_plan():
    recipes = Recipe.objects.all()
    raw_plan = []
    if len(recipes) < 8:
        random_integers = random.sample(range(len(recipes)), len(recipes))
    else:
        random_integers = random.sample(range(len(recipes)), 8)

    for number in random_integers:
        raw_plan.append(recipes[number])
        if len(raw_plan) == 8:
            break

    return raw_plan
