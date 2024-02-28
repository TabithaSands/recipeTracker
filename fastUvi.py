from typing import Union
from fastapi import FastAPI
from allrecipes import AllRecipes
from fastapi.templating import Jinja2Templates


app = FastAPI()
templates = Jinja2Templates(directory='templates/')


def find_recipe(search_item):
    print(f"========== Searching for {search_item} ==========")
    query_result = AllRecipes.search(search_item)

    # Get:
    main_recipe_url = query_result[0]['url']
    detailed_recipe = AllRecipes.get(main_recipe_url)
    return detailed_recipe


@app.get("/")
def read_root():
    detailed_recipe = find_recipe("mac and cheese")
    return templates.TemplateResponse('home.html', context={'request': detailed_recipe, 'recipe': detailed_recipe})
