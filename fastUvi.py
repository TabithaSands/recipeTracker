from fastapi import FastAPI, Form, Request
from allrecipes import AllRecipes
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory='templates/')


def find_recipe(search_item):
    print(f"========== Searching for {search_item} ==========")
    query_result = AllRecipes.search(search_item)

    # Get:
    # main_recipe_url = query_result[0]['url']
    # detailed_recipe = AllRecipes.get(main_recipe_url)
    return query_result


@app.get("/")
def read_root():
    detailed_recipe = find_recipe("mac and cheese")
    return templates.TemplateResponse('home.html', context={'request': detailed_recipe, 'recipe': detailed_recipe})


@app.get("/form")
def form_post(request: Request):
    result = "Search a recipe"
    return templates.TemplateResponse('form.html', context={'request': request, 'result': result})


@app.post("/form")
def form_post(request: Request, search_item: str = Form(...)):
    result = find_recipe(search_item)
    return templates.TemplateResponse('form.html', context={'request': request, 'result': result})
